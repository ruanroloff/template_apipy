import os
from flask import Blueprint, request, url_for, current_app
from app.utils.responses import response_with
from app.utils import responses as resp
from app.model.authors import Author, AuthorSchema
from app.main import db


def get_author_list():
    fetched = Author.query.all()
    author_schema = AuthorSchema(many=True, only=['first_name', 'last_name', 'id'])
    authors = author_schema.dump(fetched)
    return authors


def get_author_detail(author_id):
    fetched = Author.query.get_or_404(author_id)
    author_schema = AuthorSchema()
    author = author_schema.dump(fetched)
    return author
