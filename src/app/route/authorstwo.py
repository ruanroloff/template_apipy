#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, request, url_for, current_app

from app.utils.responses import response_with
from app.utils import responses as resp
from app.model.authors import Author, AuthorSchema
from app.main import db, app
from flask_jwt_extended import jwt_required
import os


from flask_restx import Resource, Api
from flask_restx import fields




author_routesx = Blueprint("api_routes", __name__)
authors_api = Api(author_routesx)
#api = Api(app)
#authors_api = Api(app)



@authors_api.route('/hello')
class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}


