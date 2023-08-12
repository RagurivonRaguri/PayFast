from models import db, Product, Category, Orders, Sales, User, Profile, Suppliers
from app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

profiles = [{
  "id": 1,
  "firstname": "Dennis",
  "lastname": "Mwai",
  "location": "Nairobi",
  "profile_pic": "http://dummyimage.com/131x100.png/ff4444/ffffff",
  "user_id": 1
}, {
  "id": 2,
  "firstname": "Karolina",
  "lastname": "Fullun",
  "location": "Jalatrang",
  "profile_pic": "http://dummyimage.com/246x100.png/dddddd/000000",
  "user_id": 2
}, {
  "id": 3,
  "firstname": "Ariadne",
  "lastname": "Leat",
  "location": "Chinch'ŏn",
  "profile_pic": "http://dummyimage.com/160x100.png/5fa2dd/ffffff",
  "user_id": 3
}, {
  "id": 4,
  "firstname": "Davis",
  "lastname": "Bradley",
  "location": "Canauay",
  "profile_pic": "http://dummyimage.com/185x100.png/5fa2dd/ffffff",
  "user_id": 4
}, {
  "id": 5,
  "firstname": "Austin",
  "lastname": "Ikinya",
  "location": "Garissa",
  "profile_pic": "http://dummyimage.com/207x100.png/ff4444/ffffff",
  "user_id": 5
}, {
  "id": 6,
  "firstname": "Lincoln",
  "lastname": "Muraguri",
  "location": "Nairobi",
  "profile_pic": "http://dummyimage.com/207x100.png/ff4444/ffffff",
  "user_id": 6
}]

users = [{
  "id": 1,
  "email": "dennis7@gmail.com",
  "username": "cboome0",
  "password": "password",
  "role": "cashier",
}, {
  "id": 2,
  "email": "ngarforth1@google.com.hk",
  "username": "kmceneny1",
  "password": "qE2`|7C57fEcM$",
  "role": "manager",
}, {
  "id": 3,
  "email": "nfoukx2@elegantthemes.com",
  "username": "nsafont2",
  "password": "lR8_SCimbb",
  "role": "manager",
}, {
  "id": 4,
  "email": "brad3@gmail.com",
  "username": "ethunders3",
  "password": "password",
  "role": "manager",
}, {
  "id": 5,
  "email": "austin34@gmail.com",
  "username": "rbuttwell4",
  "password": "password",
  "role": "shopowner",
},{
  "id": 6,
  "email": "lincoln12@gmail.com",
  "username": "raguri",
  "password": "password",
  "role": "admin",
}]

sales = [{
  "id": 1,
  "date_of_purchase": "2018-10-17 07:47:16",
  "total_amount": 449,
  "user_id": 1,
  "product_id": 1
}, {
  "id": 2,
  "date_of_purchase": "2020-11-18 05:10:53",
  "total_amount": 464,
  "user_id": 1,
  "product_id": 1
}, {
  "id": 3,
  "date_of_purchase": "2017-12-03 22:27:19",
  "total_amount": 2803,
  "user_id": 1,
  "product_id": 1
}, {
  "id": 4,
  "date_of_purchase": "2017-12-04 20:59:07",
  "total_amount": 2473,
  "user_id": 3,
  "product_id": 4
}, {
  "id": 5,
  "date_of_purchase": "2020-03-07 06:03:42",
  "total_amount": 2478,
  "user_id": 2,
  "product_id": 5
}, { 
    "id": 6,
    "date_of_purchase": "2020-08-01 09:30:00",
    "total_amount": 1800,
    "user_id": 2,
    "product_id": 5
 },{
     "id": 7,
     "date_of_purchase": "2023-08-02 14:15:00",
     "total_amount": 2235,
     "user_id": 4,
     "product_id": 7
 }, {
     "id": 8,
     "date_of_purchase": "2023-08-03 18:00:00",
     "total_amount": 2322,
     "user_id": 1,
     "product_id": 8
 },{
     "id": 9,
      "date_of_purchase": "2023-08-03 18:00:00",
      "total_amount": 5532,
      "user_id": 5,
      "product_id": 9
 },{
      "id": 10,
        "date_of_purchase": "2023-08-04 12:30:00",
        "total_amount": 440,
        "user_id": 5,
        "product_id": 6
 },{
     "id": 11,
      "date_of_purchase": "2023-08-06 09:20:00",
      "total_amount": 445,
      "user_id": 1,
      "product_id": 11
 }, {
     
        "id": 12,
        "date_of_purchase": "2023-08-07 14:10:00",
        "total_amount": 3530,
        "user_id": 2,
        "product_id": 12
 },{
     "id": 13,
        "date_of_purchase": "2022-08-07 14:11:00",
        "total_amount": 35630,
        "user_id": 3,
        "product_id": 13
 }]
     


orders = [{
  "id": 1,
  "date_of_order": "2020-10-14 14:34:30",
  "total_amount": 52,
  "user_id": 1,
  "product_id": 1,
  "order_fulfilled": True
}, {
  "id": 2,
  "date_of_order": "2021-05-30 20:58:47",
  "total_amount": 778,
  "user_id": 2,
  "product_id": 2,
  "order_fulfilled": False
}, {
  "id": 3,
  "date_of_order": "2017-08-30 16:28:16",
  "total_amount": 239,
  "user_id": 3,
  "product_id": 3,
  "order_fulfilled": True
}, {
  "id": 4,
  "date_of_order": "2022-08-02 00:00:47",
  "total_amount": 103,
  "user_id": 4,
  "product_id": 4,
  "order_fulfilled": True
}, {
  "id": 5,
  "date_of_order": "2022-09-27 15:22:36",
  "total_amount": 64,
  "user_id": 5,
  "product_id": 5,
  "order_fulfilled": False
}, {
    "id": 6,
  "date_of_order": "2020-09-27 15:15:36",
  "total_amount": 46,
  "user_id": 6,
  "product_id": 6,
  "order_fulfilled": False
}]

categories = [{
  "id": 1,
  "name": "sweets"
}, {
  "id": 2,
  "name": "stationery"
}, {
  "id": 3,
  "name": "oils"
}, {
  "id": 4,
  "name": "toys"
}, {
  "id": 5,
  "name": "cutlery"
},{"id": 6,
  "name": "electronics"
},{"id": 7,
   "name": "clothing"
}, {
   "id": 8,
    "name": "books"
}, {
   "id": 9,
   "name": "beauty"
}, {
     "id": 10,
    "name": "home decor"
}, {
      "id": 11,
      "name": "sports equipment"
}, {
    "id": 12,
    "name": "jewelry"
},{
  "id": 13,
  "name": "pet supplies"
}]

suppliers = [{
  "id": 1,
  "name": "ante"
}, {
  "id": 2,
  "name": "mauris"
}, {
  "id": 3,
  "name": "sed"
}, {
  "id": 4,
  "name": "in"
}, {
  "id": 5,
  "name": "nisi"
},{
    "id":6,
    "name":"alv"
},{
    "id":7,
    "name":"vyb"
},{
    "id":8,
    "name":"kart"
},{
    "id":9,
    "name":"bev"
},{
    "id":10,
    "name":"mili"
  }, {
      "id":11,
      "name":"jet"
}, {
    "id":12,
    "name":"kartelo"
}]
    
products = [
    {
  "id": 1,
  "name": "Muffin Batt - Choc ",
  "description": "Reconstruction of eyelid involving lid margin, partial-thickness",
  "cost": 400,
  "quantity": 45,
  "image": "https://www.amummytoo.co.uk/wp-content/uploads/2020/02/chocolate-orange-muffins-6.jpg",
  "category_id": 1,
  "suppliers_id": 1,
  "users_id": 1
    }, {
  "id": 2,
  "name": "id",
  "description": "elit proin risus praesent lectus vestibulum quam sapien",
  "cost": 667,
  "quantity": 65,
  "image": "http://dummyimage.com/101x100.png/cc0000/ffffff",
  "category_id": 2,
  "suppliers_id": 2,
  "users_id": 2
}, {
  "id": 3,
  "name": "turpis",
  "description": "vestibulum eget vulputate ut ultrices vel augue vestibulum",
  "cost": 613,
  "quantity": 16,
  "image": "http://dummyimage.com/245x100.png/5fa2dd/ffffff",
  "category_id": 3,
  "suppliers_id": 3,
  "users_id": 3
}, {
  "id": 4,
  "name": "amet",
  "description": "platea dictumst maecenas ut massa quis augue luctus tincidunt",
  "cost": 681,
  "quantity": 97,
  "image": "http://dummyimage.com/205x100.png/dddddd/000000",
  "category_id": 4,
  "suppliers_id": 4,
  "users_id": 4
}, {
  "id": 5,
  "name": "consectetuer",
  "description": "mattis odio donec vitae nisi",
  "cost": 855,
  "quantity": 51,
  "image": "http://dummyimage.com/232x100.png/ff4444/ffffff",
  "category_id": 12,
  "suppliers_id": 5,
  "users_id":4
},{ 
    "id": 6,
    "name": "Smartphone X",
    "description": "High-end smartphone with advanced features",
    "cost": 1000,
    "quantity": 20,
    "image": "http://dummyimage.com/245x100.png/5fa2dd/ffffff", 
    "category_id": 10,
    "suppliers_id": 10,
    "users_id": 3
},{     
   "id": 7,
      "name": "T-shirt Basic",
      "description": "Comfortable and stylish basic t-shirt",
       "cost": 20,
      "quantity": 100,
      "image": "http://dummyimage.com/205x100.png/dddddd/000000",  # Replace with the dummy image URL
      "category_id": 7,
      "suppliers_id": 3,
      "users_id": 4

},{
     "id": 8,
     "name": "Book: The Adventures of AI",
     "description": "An exciting AI-themed book for tech enthusiasts",
     "cost": 25,
     "quantity": 50,
     "image": "http://dummyimage.com/160x100.png/5fa2dd/ffffff",  # Replace with the dummy image URL
     "category_id": 8,
     "suppliers_id": 8,
     "users_id": 6
},{
    "id": 9,
    "name": "Home Decor Set",
    "description": "Elegant home decor set for modern living rooms",
    "cost": 150,
    "quantity": 25,
    "image": "http://dummyimage.com/300x200.png/ffcc00/ffffff",
    "category_id": 9,
    "suppliers_id": 9,
    "users_id": 1
},{
     "id": 10,
    "name": "Wireless Headphones",
    "description": "High-quality wireless headphones for immersive sound experience",
    "cost": 120,
    "quantity": 30,
    "image": "http://dummyimage.com/200x150.png/0099cc/ffffff",
    "category_id": 10,
    "suppliers_id": 10,
    "users_id": 6
},{
     "id": 11,
    "name": "Laptop Stand",
    "description": "Ergonomic laptop stand for comfortable working",
    "cost": 35,
    "quantity": 40,
    "image": "http://dummyimage.com/250x150.png/33cc33/ffffff",
    "category_id": 11,
    "suppliers_id": 11,
    "users_id": 1
},{
    "id": 12,
    "name": "Yoga Mat",
    "description": "Premium quality yoga mat for yoga and fitness enthusiasts",
    "cost": 40,
    "quantity": 50,
    "image": "http://dummyimage.com/300x200.png/ff9900/ffffff",
    "category_id": 12,
    "suppliers_id": 12,
    "users_id": 2
},{
    "id": 13,
    "name": "Outdoor Backpack",
    "description": "Durable outdoor backpack for adventure seekers",
    "cost": 80,
    "quantity": 15,
    "image": "http://dummyimage.com/220x150.png/9900cc/ffffff",
    "category_id": 11,
    "suppliers_id": 11,
    "users_id": 3
},{
    "id": 14,
    "name": "Plant Collection",
    "description": "Assorted indoor plants to add greenery to your home",
    "cost": 50,
    "quantity": 25,
    "image": "http://dummyimage.com/180x200.png/ff6633/ffffff",
    "category_id": 1,
    "suppliers_id": 4,
    "users_id": 4
},{
    "id": 15,
    "name": "Bluetooth Speaker",
    "description": "Portable Bluetooth speaker for music lovers on the go",
    "cost": 60,
    "quantity": 60,
    "image": "http://dummyimage.com/210x150.png/ff3300/ffffff",
    "category_id": 1,
    "suppliers_id": 5,
    "users_id": 5
},{
    "id": 16,
    "name": "Canvas Art",
    "description": "Stunning canvas art to decorate your living space",
    "cost": 90,
    "quantity": 10,
    "image": "http://dummyimage.com/300x300.png/9933ff/ffffff",
    "category_id": 6,
    "suppliers_id": 1,
    "users_id": 6
},{
    "id": 17,
    "name": "Gaming Mouse",
    "description": "High-performance gaming mouse for gamers",
    "cost": 70,
    "quantity": 20,
    "image": "http://dummyimage.com/180x180.png/00cc99/ffffff",
    "category_id": 7,
    "suppliers_id": 6,
    "users_id": 1
},{
    "id": 18,
    "name": "Coffee Maker",
    "description": "Premium coffee maker for coffee enthusiasts",
    "cost": 150,
    "quantity": 10,
    "image": "http://dummyimage.com/250x180.png/ffcc33/ffffff",
    "category_id": 8,
    "suppliers_id": 1,
    "users_id": 5
},{
    "id": 19,
    "name": "Fitness Tracker",
    "description": "Smart fitness tracker to monitor your health and activity",
    "cost": 100,
    "quantity": 30,
    "image": "http://dummyimage.com/220x220.png/009999/ffffff",
    "category_id": 6,
    "suppliers_id": 12,
    "users_id": 5
},{
    "id": 20,
    "name": "Desk Organizer",
    "description": "Stylish desk organizer to keep your workspace tidy",
    "cost": 25,
    "quantity": 40,
    "image": "http://dummyimage.com/200x180.png/996633/ffffff",
    "category_id": 2,
    "suppliers_id": 10,
    "users_id": 2
}]

with app.app_context():
    # # Drop the tables then create the tables to avoid duplicates
    db.drop_all()
    db.create_all()


     #Add users to the database
    for user_data in users:
      hashed_password = bcrypt.generate_password_hash(user_data["password"]).decode('utf-8')
      user = User(
          id=user_data["id"],
          email=user_data["email"],
          username=user_data["username"],
          password=hashed_password,
          role=user_data["role"]
      )
      db.session.add(user)
      db.session.commit()

    #Add profiles to the database
    for profile_data in profiles:
        profile = Profile(
            id=profile_data["id"],
            firstname=profile_data["firstname"],
            lastname=profile_data["lastname"],
            location=profile_data["location"],
            profile_pic=profile_data["profile_pic"],
            user_id=profile_data["user_id"]
        )
        db.session.add(profile)
        db.session.commit()
   
    for supplier_data in suppliers:
        supplier = Suppliers(
        id = supplier_data["id"],
        name = supplier_data["name"]
        )
        db.session.add(supplier)
        db.session.commit()

    # Add categories to the database
    for category_data in categories:
        category = Category(
            name=category_data["name"]
        )
        db.session.add(category)
        db.session.commit()

    # Add products to the database
    for product_data in products:
        product = Product(
            id=product_data["id"],  # Assuming 'id' is part of the Product model
            name=product_data["name"],
            description=product_data["description"],
            cost=product_data["cost"],
            quantity=product_data["quantity"],
            image=product_data["image"],
            category_id=product_data["category_id"],
            suppliers_id=product_data["suppliers_id"],
            users_id=product_data["users_id"]
        )
        db.session.add(product)
        db.session.commit()

    # Add orders to the database
    for order_data in orders:
        order = Orders(
            id=order_data["id"],  # Assuming 'id' is part of the Order model
            date_of_order=order_data["date_of_order"],
            total_amount=order_data["total_amount"],
            user_id=order_data["user_id"],
            product_id=order_data["product_id"],
            order_fulfilled=order_data["order_fulfilled"]
        )
        db.session.add(order)
        db.session.commit()

    # #Add sales to the database
    # for sale_data in sales:
    #     sale = Sales(
    #         id=sale_data["id"],  # Assuming 'id' is part of the Sale model
    #         date_of_purchase=sale_data["date_of_purchase"],
    #         total_amount=sale_data["total_amount"],
    #         user_id=sale_data["user_id"],
    #         product_id=sale_data["product_id"]
    #     )
    #     db.session.add(sale)

    # Commit the changes to the database
    db.session.commit()
    print('Seeded successfully')
