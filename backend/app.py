from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db

app = Flask(__name__)
# Set app configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://raguri:y3nyDpdCpSYzVCi3ngwxt7DF0lTexCn6@dpg-cj8ukuukntus73ebbbbg-a.oregon-postgres.render.com/payfast_5m1t?sslmode=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
app.config['SECRET_KEY'] = b'\xbe\xd7b\x87\xdbF\x1e\xcf\xc1\xa7\xb7\x12\xc5Y\xe7\xd9\xa6\x86\xc7PH\xbea'

# Initialize extensions
db.init_app(app)
CORS(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


# Import blueprints and register them
from users import users
from inventory import inventory
from sales import sales

app.register_blueprint(inventory)
app.register_blueprint(users)
app.register_blueprint(sales)

# The Home Route
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to PayFast'})

if __name__ == "__main__":
    app.run()




