import os
#from os import environ, path
#from dotenv import load_dotenv

class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    #SQLALCHEMY_ECHO = True    
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:XXX@00.000.0.00:3306/dbusers3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    SECRET_KEY = os.urandom(32)
    SECURITY_PASSWORD_SALT = os.urandom(12).hex()
    #app.config['SECRET_KEY'] = SECRET_KEY
    #SECRET_KEY="powerful secretkey"
    #WTF_CSRF_SECRET_KEY="a csrf secret key"

    # Create a new gmail account to run activate a user. (The account needs to be able to send email)
    # mail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = '**@gmail.com'
    MAIL_PASSWORD = '***'
    MAIL_DEFAULT_SENDER = '***@gmail.com'

    UPLOAD_FOLDER = '/path/to/the/uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    ###MONGO DB
    #MONGOALCHEMY_DATABASE = "dbbook"
    MONGODB_SETTINGS = {
        'db': 'dbbook',
        'host': 'mongodb://cdbmongo:***@cdbmongo.mongo.cosmos.azure.com:10255/dbbook?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cdbmongo@'
    }   
        

class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://<db_url>:<port>/<db_name>"
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'JWT-SECRET'
    SECRET_KEY= 'SECRET-KEY'
    SECURITY_PASSWORD_SALT= 'SECRET-KEY-PASSWORD'
    MAIL_DEFAULT_SENDER= '<mail_sender>'
    MAIL_SERVER= '<mail_smtp_host>'
    MAIL_PORT= '<mail_port>'
    MAIL_USERNAME= '<mail_username>'
    MAIL_PASSWORD= '<mail_password>'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True
    UPLOAD_FOLDER= '<upload_folder>'

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@/appdb?unix_socket=/cloudsql/database-316500:us-central1:dbtest"


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
