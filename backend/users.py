from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import FlushError
from flask import make_response, jsonify, request, session, Blueprint, redirect, url_for
from models import Profile, User, db
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, unset_jwt_cookies
from flask_bcrypt import Bcrypt

users = Blueprint("users", __name__)
bcrypt = Bcrypt()

@users.route('/post_admin', methods=['POST'])
def post_admin():
    email = request.json.get('email')
    password = request.json.get('password')
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(
            username=request.json.get('username'),
            email=email,
            password=hashed_password,
            role=request.json.get('role'),
        )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg":"success"})

@users.route('/post_manager', methods=['POST'])
@jwt_required()
def post_manager():
    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)
    if user.role != 'shopowner':
        return make_response(jsonify({"msg": "Not authorized to access this"}))
    
    email = request.json.get('email')
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'Email already exists'})
    password = request.json.get('password')
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_manager = User(
        username=request.json.get('username'),
        email=email,
        password=hashed_password,
        role='manager'
    )
    new_profile = Profile(
        firstname='',
        lastname='',
        location='',
        profile_pic='',
        user=new_manager  
    )
    try:
        db.session.add(new_manager)
        db.session.commit()
        db.session.add(new_profile)
        db.session.commit()
        return jsonify({'message': 'Manager registered successfully'})
    except (IntegrityError, FlushError):
        db.session.rollback()
        return jsonify({'message': 'Error: Manager registration failed'}), 500
    
@users.route('/post_cashier', methods=['POST'])
@jwt_required()
def post_cashier():
    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)
    if user.role != 'shopowner' and user.role != 'manager':
        return make_response(jsonify({"msg": "Not authorized to access this"}))

    email = request.json.get('email')
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'Email already exists'})
    password = request.json.get('password')
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_cashier = User(
        username=request.json.get('username'),
        email=email,
        password=hashed_password,
        role='cashier'
    )
    new_profile = Profile(
        firstname='',
        lastname='',
        location='',
        profile_pic='',
        user=new_cashier  
    )
    try:
        db.session.add(new_cashier)
        db.session.commit()
        db.session.add(new_profile)
        db.session.commit()
        return jsonify({'message': 'Cashier registered successfully'})
    except (IntegrityError, FlushError):
        db.session.rollback()
        return jsonify({'message': 'Error: Cashier registration failed'}), 500
    
@users.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'Email already exists'})

    password = request.json.get('password')
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(
        username=request.json.get('username'),
        email=email,
        password=hashed_password,
        role='shopowner'
    )
    
    new_profile = Profile(
        firstname='',
        lastname='',
        location='',
        profile_pic='',
        user=new_user  # Associate the new_profile with the new_user
    )
    
    db.session.add(new_user)
    db.session.commit()
    db.session.add(new_profile)
    db.session.commit()
    token = create_access_token(identity=new_user.id)
    metadata = {
            "email": new_user.email,
            "role": new_user.role
        }
    return make_response(jsonify({
            "access_token": token,
            "metadata": metadata
        }), 200)
    
@users.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or "email" not in data or "password" not in data:
        return make_response(jsonify({"message": "Missing email or password"}), 400)

    email = data["email"]
    password = data["password"]
    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        token = create_access_token(identity=user.id)
        metadata = {
            "email": user.email,
            "role": user.role
        }
        return make_response(jsonify({
            "access_token": token,
            "metadata": metadata
        }), 200)
    else:
        return make_response(jsonify({"message": "Invalid email or password"}), 400)

# Logout Route
@users.route('/logout', methods = ["GET"])
def logout():
    response = jsonify(detail = "Logout successful")
    unset_jwt_cookies(response)
    return response

@users.route('/profile', methods = ["GET"])
@jwt_required()
def profile():
    current_user_id = get_jwt_identity()
    user = Profile.query.filter_by(id=current_user_id).first()
    if user:
        user_dict = {
                    'firstname': user.firstname,
                    'lastname': user.lastname,
                    'location': user.location,
                    'profile_pic': user.profile_pic,
                }
        return make_response(
            jsonify(user_dict, 200)
        )

@users.route('/patch_user/<int:id>', methods =['PATCH'])
@jwt_required()
def patch_user():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    if user:
        if request.method == 'PATCH':
            profile_list = ['firstname', 'lastname', 'location']
        for attribute in profile_list:
            value = request.json.get(attribute)
            setattr(user, attribute, value)

        db.session.commit()
        response = make_response(
            profile_dict = {
                'firstname': user.firstname,
                'lastname': user.lastname,
                'location': user.location,
            }
        )
        return response


@users.route('/cashiers', methods=['GET'])
@jwt_required()
def cashiers():
    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)
    if user.role != 'manager':
        return jsonify({'message': 'Access restricted. Only managers can access this route.'}), 403
    if request.method == 'GET':
        cashiers = User.query.all()
        cashier_list = []
        for cashier in cashiers:
            cashier = {
                'username': cashier.username,
                'password': cashier.password
            }
            cashier_list.append(cashier)

        
        return make_response(
            jsonify(cashier_list, 200)
        )
        
@users.route('/cashier/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@jwt_required()
def cashier(id):
    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)
    if user.role != 'manager':
        return jsonify({'message': 'Access restricted. Only managers can access this route.'}), 403
    
    if request.method == 'GET':
        cashier = User.query.get(id)
        if not cashier:
            return jsonify({'message': 'Cashier not found'}), 404
        cashier = {
                    'profile_id': cashier.profile_id,
                    'email': cashier.email,
                    'username': cashier.username,
                    'password': cashier.password
                }
        return make_response(
            jsonify(cashier, 200)
        )
    
    if request.method == 'PATCH':
        cashier = User.query.get(id)
        if not cashier:
            return jsonify({'message': 'Cashier not found'}), 404
        cashier_list = ['username', 'password']
        for attribute in cashier_list:
            value = request.json.get(attribute)
            setattr(cashier, attribute, value)

        db.session.commit()
        response = make_response(
            cashier_dict = {
                'username': cashier.username,
                'password': cashier.password
            }
        )
        return response
    
    if request.method == 'DELETE':
        cashier = User.query.get(id)
        if not cashier:
            return jsonify({'message': 'Cashier not found'}), 404
        db.session.delete(cashier)
        return {"Cashier deleted": True}
    
#Admins can access the managers
@users.route('/managers', methods=['GET'])
@jwt_required()
def managers():
    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)
    if user.role != 'admin' and user.role != 'shopowner':
        return jsonify({'message': 'Access restricted. Only admins can access this route.'}), 403

    if request.method == 'GET':
        managers = User.query.all()
        manager_list = []
        for manager in managers:
            manager_data = {
                'username': manager.username,
                'password': manager.password
            }
            manager_list.append(manager_data)

        return make_response(
            jsonify(manager_list),
            200
        )
                
@users.route('/post_profile', methods=['POST'])
@jwt_required()
def post_profile():

    new_profile =Profile(
            firstname=request.json.get('date_of_purchase'),
            lastname=request.json.get('lastname'),
            location=request.json.get('location'),
            profile_pic=request.json.get('profile_pic')
            
    )
    db.session.add(new_profile)
    db.session.commit()
    return make_response(
        jsonify({"msg": "success"}),200
    )

@users.route('/patch_profile', methods=['PATCH'])
@jwt_required()
def patch_profile():
    current_user_id = get_jwt_identity()
    
    user = User.query.get(current_user_id)
    if user is None:
        return make_response(jsonify({"msg": "User not found"}), 404)
    
    profile = user.profile  # Assuming you have a relationship set up between User and Profile
        
    if 'firstname' in request.json:
        profile.firstname = request.json.get('firstname')
    if 'lastname' in request.json:
        profile.lastname = request.json.get('lastname')
    if 'location' in request.json:
        profile.location = request.json.get('location')
    if 'profile_pic' in request.json:
        profile.profile_pic = request.json.get('profile_pic')
    
    db.session.commit()
    
    return make_response(
        jsonify({"msg": "success"}), 200
    )


