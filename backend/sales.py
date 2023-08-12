from flask import make_response, jsonify, request, Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from models import User, Sales, Product
from app import db

sales = Blueprint("sales", __name__)

@sales.route('/sales')
@jwt_required()
def get_sales():
    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)
    if user.role == 'shopowner':
        sales_data = []
        sales = Sales.query.all()
        for sale in sales:
            sale_info = {
                "date_of_purchase": sale.date_of_purchase,
                "total_amount": sale.total_amount,
                "user_id": sale.user_id,
                "product_id": sale.product_id
            }
            sales_data.append(sale_info)
        return jsonify(sales_data)
    else:
        return jsonify({"message": "You do not have the necessary permissions to access this resource."}), 403
    


from datetime import datetime

@sales.route('/post_sales', methods=['POST'])
@jwt_required()
def post_sales():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if user.role != 'cashier' and user.role != 'shopowner':
        return make_response(jsonify({"msg": "Not authorized"}))
    
    if request.method == 'POST':
        data = request.json  

        # Convert Unix timestamp to datetime
        date_of_purchase_unix = data.get('date_of_purchase')
        date_of_purchase = datetime.fromtimestamp(date_of_purchase_unix)
        total_amount = data.get('total_amount')
        product_ids = data.get('product_ids')

        if product_ids is None or not isinstance(product_ids, list):
            return make_response(jsonify({"msg": "Invalid product_ids data"}), 400)

        new_sales_entries = []
        for product_id in product_ids:
            new_sales = Sales(
                date_of_purchase=date_of_purchase,
                total_amount=total_amount,
                user_id=current_user_id,
                product_id=product_id,
            )
            new_sales_entries.append(new_sales)

        db.session.add_all(new_sales_entries)  # Use add_all to add multiple objects
        db.session.commit()

        for product_id in product_ids:
            product = Product.query.filter_by(id=product_id).first()
            if product:
                product.quantity -= 1

        db.session.commit()  # Commit the product quantity changes

        return make_response(jsonify({"msg": "success"}), 200)
        
            

            
