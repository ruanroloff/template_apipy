import os

from flask import Blueprint, request, url_for, current_app
from app.utils.responses import response_with
from app.utils import responses as resp
from app.logic import authors
from app.main import db
#from app.utils.file import secure_filename, allowed_file

from flask_jwt_extended import jwt_required


logic_routes = Blueprint("logic_routes", __name__)
           


@logic_routes.route('/', methods=['GET'])
@jwt_required()
def get_author_list():
    author = authors.get_author_list()
    return response_with(resp.SUCCESS_200, value={"authors": author})

@logic_routes.route('/<int:author_id>', methods=['GET'])
def get_author_detail(author_id):
    author = authors.get_author_detail(author_id)
    return response_with(resp.SUCCESS_200, value={"author": author})
