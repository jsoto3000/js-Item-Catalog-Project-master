# Adding dummy data to database, this will add categories to the database
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# You can add items by just uncommenting the items below.

# Category : Spanish Coffees
cat1 = Category(id=1, name="Spanish Coffee")
session.add(cat1)
session.commit()

item1 = Item(name="Bustelo",
             description="Dark Roast",
             price="5.99",
             category=cat1)
session.add(item1)
session.commit()

item2 = Item(name="Pico",
             description="Medium Roast",
             price="1.99",
             category=cat1)
session.add(item2)
session.commit()


# Category : Fast Foods
cat2 = Category(id=2, name="Italian Coffee")
session.add(cat2)
session.commit()


item = Item(name="Nero", description="Dark Roast", price="4.99", category=cat2)
session.add(item)
session.commit()

item = Item(name="Bianco", description="Light", price="4.99", category=cat2)
session.add(item)
session.commit()


# Category : Beverages
cat3 = Category(id=3, name="French Coffee")
session.add(cat3)
session.commit()


item = Item(name="Soire",
            description="Dark Roast",
            price="1.99",
            category=cat3)
session.add(item)
session.commit()

item = Item(name="Ca Va",
            description="Medium Roast",
            price="Rs. 20.99",
            category=cat3)
session.add(item)
session.commit()


# Category : Main Course
cat4 = Category(id=4, name="British Tea")
session.add(cat4)
session.commit()

item = Item(name="Earl Grey",
            description="Classic",
            price="6.99",
            category=cat4)
session.add(item)
session.commit()

item = Item(name="Green Tea", description="Diet", price="6.99", category=cat4)
session.add(item)
session.commit()


print("Categories added!")

