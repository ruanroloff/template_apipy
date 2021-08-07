
from app.main import app

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
#from flask import Flask
from marshmallow import Schema, fields


# Create an APISpec
spec = APISpec(
    title="Swagger User",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


#from app.model.authors import AuthorSchema


# Optional security scheme support
api_key_scheme = {"type": "apiKey", "in": "header", "name": "X-API-Key"}
spec.components.security_scheme("ApiKeyAuth", api_key_scheme)



from flask import jsonify
from flask_swagger import swagger

from app.route.authors import get_author_list

from app.route import authors









# Register the path and the entities within it
with app.test_request_context():
    spec.path(view=authors.get_author_list)


#### GENERATE SWAGGER
#import json
#print(json.dumps(spec.to_dict(), indent=2))
#print(spec.to_yaml())





from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = '/api/author/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger/v1/author.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint, name='myview2')

