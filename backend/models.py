from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    location = db.Column(db.String())
    profile_pic = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='profile')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String())
    username = db.Column(db.String())
    password = db.Column(db.String())
    role = db.Column(db.String())
    profile = db.relationship('Profile', back_populates='user')
   
    def check_password(self, password):
        return self.password == password
    

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    products = db.relationship('Product', backref='categories.id')
        
    
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    cost = db.Column(db.Integer())
    quantity = db.Column(db.Integer())
    image = db.Column(db.String())
    category_id = db.Column(db.Integer(), db.ForeignKey('categories.id'))
    suppliers_id = db.Column(db.Integer(), db.ForeignKey("suppliers.id"))
    users_id = db.Column(db.Integer(), db.ForeignKey("users.id"))
    sales = db.relationship("Sales", backref="products")
    orders = db.relationship("Orders", backref="products")

class Sales(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    date_of_purchase = db.Column(db.DateTime, server_default=func.now())
    total_amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer(), db.ForeignKey('products.id'))
    
class Orders(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    date_of_order = db.Column(db.DateTime, server_default=func.now())
    total_amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer(), db.ForeignKey('products.id'))
    order_fulfilled = db.Column(db.Boolean())

class Suppliers(db.Model):
    __tablename__ = 'suppliers'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    products = db.relationship('Product', backref="suppliers")