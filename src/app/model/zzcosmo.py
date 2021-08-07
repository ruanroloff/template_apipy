#!/usr/bin/python
# -*- coding: utf-8 -*-

from app.main import app
from marshmallow import fields
from app.main import ma

from flask_mongoengine import MongoEngine


db = MongoEngine(app)

class Director(db.DynamicDocument):
    pass

class Cast(db.DynamicEmbeddedDocument):
    pass

class Imdb(db.EmbeddedDocument):
    imdb_id = db.StringField()
    rating = db.DecimalField()
    votes = db.IntField()

class Movie(db.Document):
    title = db.StringField(required=True)
    year = db.IntField()
    rated = db.StringField()
    director = db.ReferenceField(Director)
    cast = db.EmbeddedDocumentListField(Cast)
    poster = db.FileField()
    imdb = db.EmbeddedDocumentField(Imdb)
