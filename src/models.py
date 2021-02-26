import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}



class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username =Column(String(120), unique=True, nullable=False)
    firstname =Column(String(120), unique=False, nullable=False)
    lastname =Column(String(120), unique=True, nullable=False)
    email =Column(String(120), unique=True, nullable=False)

    Comments =relationship('Comment', backref='User', lazy=True)
    Posts =relationship('Post', backref='User', lazy=True)
    Followers =relationship('Post', backref='User', lazy=True)   
   

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
        }


class Comment(Base):
    __tablename__ = 'Comment'
    id =Column(Integer, primary_key=True)
    comment_text =Column(String(500), unique=True, nullable=False)
    autor_id =Column(Integer,ForeignKey('User.id'),
        nullable=False)  
    post_id =Column(Integer,ForeignKey('Post.id'),
        nullable=False)

    def __repr__(self):
        return '<Comment %r>' % self.id

    def serialize(self):
        return {
           "comment_text": self.comment_text,
            "autor_id": self.autor_id,
            "post_id": self.post_id,
            
        }

class Post(Base):
    __tablename__ = 'Post'
    id =Column(Integer, primary_key=True)
    user_id =Column(Integer,ForeignKey('User.id'),
        nullable=False)
    comments =relationship('Comment', backref='Post', lazy=True)
    medias =relationship('Media', backref='Post', lazy=True)
    users =relationship('User', backref='Post', lazy=True)

    def __repr__(self):
        return '<Post %r>' % self.Id

    def serialize(self):
        return {
            "user_from_id": self.Id,
            "user_to_id": self.user_id,                    
        }

class Media(Base):
    __tablename__ = 'Media'
    id  =Column(Integer, primary_key=True)
    type_ =Column(String(80), unique=False, nullable=False)
    url =Column(String(120), unique=False, nullable=False)
    post_id =Column(Integer,ForeignKey('Post.id'),
        nullable=False)

  

    def __repr__(self):
        return '<Media %r>' % self.id

    def serialize(self):
        return {
            "type": self.type_,    
            "url": self.url, 
            "post_id": self.post_id,                 
        }

class Follower(Base):
    __tablename__ = 'follower'
    id  =Column(Integer, primary_key=True)
    user_from_id  =Column(Integer,ForeignKey('User.id'),
        nullable=False)
    user_to_id =Column(Integer,ForeignKey('User.id'),
        nullable=False)
  

    def __repr__(self):
        return '<Follower %r>' % self.user_from_id

    def serialize(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id,                    
        }
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

