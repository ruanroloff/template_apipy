#!/usr/bin/python
# -*- coding: utf-8 -*-

from app.main import db
#from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from app.main import ma




class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    def __init__(self, title, year, author_id=None):
        self.title = title
        self.year = year
        self.author_id = author_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class BookSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Book
        load_instance = True

    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    year = fields.Integer(required=True)
    author_id = fields.Integer()
