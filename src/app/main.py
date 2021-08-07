#################
#### imports ####
#################
import os
from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_mail import Mail
from flask_jwt_extended import JWTManager

# local imports
from config import app_config



################
#### config ####
################
config_name = os.getenv('FLASK_ENV', 'development')


app = Flask(__name__, instance_relative_config=True, static_url_path = '/static')
app.config.from_object(app_config[config_name])


bcrypt = Bcrypt(app)

#login_manager = LoginManager()
#login_manager.init_app(app)

###test
#login_manager.login_view = 'user.login'

#app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
#mail = Mail(app)


#from app.model.user import User
#from app.model.usertwo import User


#@login_manager.user_loader
#def load_user(user_id):
    # sqlalchemy query
    #return User.query.filter(User.id == int(user_id)).first()





def create_app():
        
    
    from app.route.authors import author_routes
    app.register_blueprint(author_routes, url_prefix='/author/1/')

    from app.route.books import book_routes
    app.register_blueprint(book_routes, url_prefix='/book/1/')

    from app.route.users import user_routes
    app.register_blueprint(user_routes, url_prefix='/user/1/')

    ####business split
    from app.route.authorslogic import logic_routes
    app.register_blueprint(logic_routes, url_prefix='/logic/1/')

    from app.route.zznosql import nosql_routes
    app.register_blueprint(nosql_routes, url_prefix='/nosql/1/')

    
    
    #### new swagger
    #from app.route.authorstwo import author_routesx as authors_api
    #app.register_blueprint(authors_api, url_prefix='/api/1')

    #from app.route.authorsnine import nine_routesx as api_nine
    #app.register_blueprint(api_nine, url_prefix='/nine/1')
   
    #db.init_app(app)
    #ma.init_app(app)
    
    return app

