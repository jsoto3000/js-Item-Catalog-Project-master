""" Making classes to store database """
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# `User` class to store data of a user
class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key= True)
    name = Column(String(250), nullable = False)
    email = Column(String(250), nullable=False)
    image = Column(String(250))

    @property
    def serialize(self):
        return{
            'name'  : self.name,
            'email' : self.email,
            }

# `Category` class to store data of a category
class Category(Base):
    __tablename__ = 'Category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
       }
 

# `Item` class to store data of a Item
class Item(Base):
    __tablename__ = 'Item'

    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    category_id = Column(Integer,ForeignKey('Category.id'))
    category = relationship(Category)
    user_id = Column(Integer,ForeignKey('User.id'))
    user = relationship(User)
    
    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'         : self.id,
           'description'         : self.description,   
           'price'         : self.price,
           'category'         : self.category_id,
           'user_id'    : self.user_id
       }

# creating database file
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.create_all(engine)
