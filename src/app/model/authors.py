#!/usr/bin/python
# -*- coding: utf-8 -*-

from app.main import db
#from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from app.model.books import BookSchema
from app.main import ma



class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    avatar = db.Column(db.String(20), nullable=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    books = db.relationship('Book', backref='Author', cascade="all, delete-orphan")

    def __init__(self, first_name, last_name, books=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.books = books

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True

    id = fields.Number(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    avatar = fields.String(dump_only=True)
    created = fields.String(dump_only=True)
    books = fields.Nested(BookSchema, many=True, only=['title','year','id'])

class AuthorSchemaShort(ma.SQLAlchemySchema):
    class Meta:
        model = Author
        load_instance = True

    id = fields.Number(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)




