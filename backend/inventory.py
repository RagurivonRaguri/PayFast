from flask import make_response, jsonify, request, session, Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from models import Product, User, Suppliers, db

inventory = Blueprint("inventory", __name__)

@inventory.route('/products', methods=['GET'])
def products():
    if request.method == 'GET':
        products = Product.query.all()
        product_list = []
        for product in products:
            product_dict = {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'cost': product.cost,
                'quantity': product.quantity,
                'images': product.image,
                'category_id': product.category_id,
            }
            product_list.append(product_dict)

        return make_response(
            jsonify(product_list), 200
        )

@inventory.route('/add_product', methods=['POST'])
@jwt_required()
def add_product():
    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)
    if user.role == 'shopowner' or user.role == 'manager':
        if request.method == 'POST':
            new_product = Product(
                    name=request.json.get('name'),
                    description=request.json.get('description'),
                    cost=float(request.json.get('cost')),  # Convert to float
                    quantity=int(request.json.get('quantity')),  # Convert to integer
                    image="",
                    category_id=int(request.json.get('category_id')),  # Convert to integer
                    suppliers_id=int(request.json.get('suppliers_id')),  # Convert to integer
                    users_id=current_user_id
                )
            db.session.add(new_product)
            db.session.commit()
            return make_response(
                jsonify({"msg": "Addition was successful!"}), 200
            )
    return make_response(
                jsonify({"msg": "Authorisation required!"}), 200
            )
@inventory.route('/product/<int:id>', methods=['PATCH','DELETE'])
@jwt_required()
def product(id):
    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)
    if user.role == 'shopowner' or user.role == 'manager':
        if request.method == 'PATCH':
            product = Product.query.filter_by(id=id).first()
            attribute_list = ['name', 'description', 'cost', 'quantity']
            data = request.get_json()  # Use get_json() to retrieve JSON data
            for attribute in attribute_list:
                if attribute in data:
                    setattr(product, attribute, data[attribute])  # Use data[attribute]
            db.session.commit()

            return make_response(
                jsonify({"msg": "Successfully updated"}),
                200
            )
        
        if request.method == 'DELETE':
            product = Product.query.filter_by(id=id).first()
            db.session.delete(product)
            db.session.commit()
            return make_response(
                jsonify({"msg": "Successfully deleted"}),
                200
            )
        
    else:
        return make_response(
            jsonify({"msg": "Authorization Failed"}),
            401
        )
         

@inventory.route('/suppliers', methods=['GET'])
@jwt_required()
def suppliers():
    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)
    if user.role == 'shopowner' or user.role == 'manager':
        if request.method == 'GET':
            suppliers = Suppliers.query.all()
            supplier_list = []
            for supplier in suppliers:
                supplier_dict = {
                    'id': supplier.id,
                    'name': supplier.name,
                }
                supplier_list.append(supplier_dict)

            return make_response(
                jsonify(supplier_list), 200
            )
        else:
            return make_response(
                jsonify({"msg": "Method not allowed"}),
                405
            )
    else:
        return make_response(
            jsonify({"msg": "Authorization Failed"}),
            401
        )
    
@inventory.route('/supplier/<int:id>', methods=['PATCH','DELETE'])
@jwt_required()
def supplier(id):
    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)
    if user.role == 'manager' or user.role == 'shopowner':
        if request.method == 'PATCH':
            supplier = Suppliers.query.filter_by(id=id).first()
            attribute_list =['name']
            for attribute in attribute_list:
                value = request.get[attribute]
                setattr(supplier, attribute,value)
            db.session.commit()

            return make_response(
                jsonify({"msg": "Successfully updated"}),
                200
                )
        
        if request.method == 'DELETE':
            supplier = Suppliers.query.filter_by(id=id).first()
            db.session.delete(supplier)
            return make_response(
                jsonify({"msg": "Successfully deleted"}),
                200
            )
        
    else:
        return make_response(
            jsonify({"msg": "Authorization Failed"}),
            401
        )


# # Upload Route
# @inventory.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' in request.files:
#         file = request.files['image']
#         image_url = handle_image_upload(file)
#         return jsonify({'imageUrl': image_url})
#     return jsonify({'error': 'No file found'}), 400
