#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, request, url_for, current_app
from app.utils.responses import response_with
from app.utils import responses as resp
from app.model.authors import Author, AuthorSchema, AuthorSchemaShort
from app.main import db
#from app.utils.file import secure_filename, allowed_file

from flask_jwt_extended import jwt_required
import os

author_routes = Blueprint("author_routes", __name__)
           
@author_routes.route('/', methods=['POST'])
#@jwt_required
def create_author():
    try:
        data = request.get_json()
        author_schema = AuthorSchema()
        author = author_schema.load(data)
        result = author_schema.dump(author.create())
        return response_with(resp.SUCCESS_201, value={"author": result})
    except Exception as e:
        return response_with(resp.INVALID_INPUT_422, value={"exception": str(e)})        
    
@author_routes.route('/avatar/<int:author_id>', methods=['POST'])
#@jwt_required
def upsert_author_avatar(author_id):
    try:
        file = request.files['avatar']
        #if file and allowed_file(file.filename):
        #    filename = secure_filename(file.filename)
        #    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        get_author = Author.query.get_or_404(author_id)
        #get_author.avatar = url_for('uploaded_file', filename=filename, _external=True)
        get_author.avatar = "test"
        db.session.add(get_author)
        db.session.commit()
        author_schema = AuthorSchema()
        author, error = author_schema.dump(get_author)
        return response_with(resp.SUCCESS_200, value={"author": author})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

az_schema = AuthorSchema(many=True, only=['first_name', 'last_name', 'id'])

@author_routes.route('/', methods=['GET'])
def get_author_list():
    """A  author endpoint.
    ---
    get:
      description: Get a list of authors
      security:
        - ApiKeyAuth: []
      responses:
        200:
          content:
            application/json:
              schema: AuthorSchemaShort
    """
    fetched = Author.query.all()
    #author_schema = AuthorSchema(many=True, only=['first_name', 'last_name', 'id'])
    author_schema = AuthorSchemaShort(many=True)
    authors = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"authors": authors})

@author_routes.route('/<int:author_id>', methods=['GET'])
def get_author_detail(author_id):
    fetched = Author.query.get_or_404(author_id)
    author_schema = AuthorSchema()
    author = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"author": author})

@author_routes.route('/<int:id>', methods=['PUT'])
#@jwt_required
def update_author_detail(id):
    data = request.get_json()
    get_author = Author.query.get_or_404(id)
    get_author.first_name = data['first_name']
    get_author.last_name = data['last_name']
    db.session.add(get_author)
    db.session.commit()
    author_schema = AuthorSchema()
    author = author_schema.dump(get_author)
    return response_with(resp.SUCCESS_200, value={"author": author})

@author_routes.route('/<int:id>', methods=['PATCH'])
def modify_author_detail(id):
    data = request.get_json()
    get_author = Author.query.get(id)
    if data.get('first_name'):
        get_author.first_name = data['first_name']
    if data.get('last_name'):
        get_author.last_name = data['last_name']
    db.session.add(get_author)
    db.session.commit()
    author_schema = AuthorSchema()
    author, error = author_schema.dump(get_author)
    return response_with(resp.SUCCESS_200, value={"author": author})

@author_routes.route('/<int:id>', methods=['DELETE'])
def delete_author(id):
    get_author = Author.query.get_or_404(id)
    db.session.delete(get_author)
    db.session.commit()
    return response_with(resp.SUCCESS_204)