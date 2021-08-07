#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from google.cloud.datastore.client import _determine_default_project
from app.utils.responses import response_with
from app.utils import responses as resp
from app.main import db

from flask import jsonify
from app.model.zzcosmo import Movie, Imdb
from app.model.zzdatastore import UserDa, UserDaSchema
from app.model.zzfirestore import UserFS

nosql_routes = Blueprint("zznosql_routes", __name__)


#export GOOGLE_APPLICATION_CREDENTIALS="/run/media/ruan/data2/workspace/tmp/flask/z_api/conf/gcp/appquadabra-datastore.json"  
#export GOOGLE_APPLICATION_CREDENTIALS="/run/media/ruan/data2/workspace/tmp/flask/z_api/conf/gcp/database-firestore.json"  
#PATH_DATASTORE_CREDENTIALS = '/run/media/ruan/data2/workspace/tmp/flask/z_api/conf/gcp/appquadabra-datastore.json'

############### COSMO
@nosql_routes.route('/cosmo', methods=['POST'])
def create_cosmo():
    try:
        imdb = Imdb(imdb_id="12340mov", rating=4.2, votes=7.9)
        body = request.get_json()
        # Add object to movie and save
        movie = Movie(imdb=imdb, **body).save()
        return response_with(resp.SUCCESS_201, value={"book": movie})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@nosql_routes.route('/cosmo', methods=['GET'])
def get_cosmo_list():
    movies = Movie.objects()
    return response_with(resp.SUCCESS_200, value={"books": movies})


@nosql_routes.route('/cosmo/<string:var>', methods=['GET'])
def get_cosmo_detail(var):
    movie = Movie.objects(title=var).first()
    return response_with(resp.SUCCESS_200, value={"book": movie})


############### DATASTORE
@nosql_routes.route('/datastore', methods=['POST'])
def create_datastore():
    try:
        ##user = UserDa(service_account_json_path=PATH_DATASTORE_CREDENTIALS, namespace='custom')
        #user = UserDa(namespace='custom')
        x = {}
        user = UserDa(namespace='custom')
        user.username = 'komla'
        #user.username = 'ruan'
        user.save()
        return response_with(resp.SUCCESS_201, value={"usr": x})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

import json
import datetime


def jsonDefaultParser(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


@nosql_routes.route('/datastore', methods=['GET'])
def get_datastore_list():
    #user = UserDa(service_account_json_path=PATH_DATASTORE_CREDENTIALS, namespace='custom').get_obj('username')
    #user = UserDa(namespace='custom')
    #user = UserDa(namespace='custom').get_obj('username','komla')
    from google.cloud import datastore
    datastore_client = datastore.Client()
    docs = datastore_client.query(kind='user', namespace='custom').fetch()
    #for doc in docs:
        #print(doc.key.username)
        #print(doc)
        
    l = list(docs)
    
    jsonString = json.dumps(l, default=jsonDefaultParser)
    
    userDa = UserDaSchema(many=True)
    #data = a.dump(jsonString)
    data = userDa.loads(jsonString)
    
    #user = {}
    return response_with(resp.SUCCESS_200, value={"usr": data})

@nosql_routes.route('/datastore/<string:var>', methods=['GET'])
def get_datastore_detail(var):
    #user = UserDa(service_account_json_path=PATH_DATASTORE_CREDENTIALS, namespace='custom').get_obj('username','komla')
    user = UserDa(namespace='custom').get_obj('username','komla')
    jsonString = json.dumps(user.__dict__, default=jsonDefaultParser)
    a = UserDaSchema().loads(jsonString)
    return response_with(resp.SUCCESS_200, value={"usr": a})




############### FIRESTORE
@nosql_routes.route('/firestore', methods=['POST'])
def create_firestore():
    try:
        x = {}
        u = UserFS()
        u.name = "jon"
        u.age = 50
        u.save()
        print(u.__dict__)
        jsonString = json.dumps(u.__dict__)
        return response_with(resp.SUCCESS_201, value={"usr": jsonString})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@nosql_routes.route('/firestore', methods=['GET'])
def get_firestore_list():
    x = {}
    user_list = UserFS.collection.fetch()
    #l = list(user_list)
    #print(l)
    #jsonString = json.dumps()
    userdata = { "usr":[]}


    for user in user_list:
        usr = {}
        usr["id"]=user.id
        usr["age"]=user.age
        usr["name"]=user.name
        userdata["usr"].append(usr)
        
    jsonString = json.dumps(userdata)
    return response_with(resp.SUCCESS_200, value={"usr": jsonString})

@nosql_routes.route('/firestore/<string:var>', methods=['GET'])
def get_firestore_detail(var):
    x = {}
    #a = UserFS()
    #u = UserFS.collection.get(a.key)
    
    user = UserFS.collection.filter('name', '==', 'tom').get()
    return response_with(resp.SUCCESS_200, value={"usr": user.to_dict()})
