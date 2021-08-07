#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Blueprint, request, url_for, current_app
from app.utils.responses import response_with
from app.utils import responses as resp
from app.model.authors import Author, AuthorSchema
from app.main import app, db
from flask_restx import Api, Resource, Namespace, fields


nine_routesx = Blueprint("api_nine", __name__)

api_nine = Api(nine_routesx, 
		  version = "1.0", 
		  title = "Name Recorder", 
		  description = "Manage names of various users of the application")

namespace = api_nine.namespace('names', description='Manage names')

my_model = api_nine.model('Name Model', {
    'name': fields.String(description='The name', required=True),
    'type': fields.String(description='The object type', enum=['A', 'B']),
    'age': fields.Integer(min=0),
})


class Person(fields.Raw):
    def format(self, value):
        return {'name': value.name, 'age': value.age}


@api_nine.route('/resource/<id>', endpoint='resource')
@api_nine.doc(params={'id': 'An ID'})
class MyResource(Resource):
    @api_nine.doc(model=my_model)
    def get(self, id):
        ''' 
        TODO 
        eg: return {"name": "string","type": "A","age": id}
        '''
        return {}

    @api_nine.doc(model=my_model, body=Person)
    def post(self, id):
        ''' 
        TODO 
        '''
        return {}