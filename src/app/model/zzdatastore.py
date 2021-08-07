import datetime


from app.main import app
from datastore_entity import DatastoreEntity, EntityValue


from marshmallow import fields, Schema, EXCLUDE

class UserDa(DatastoreEntity):

    # specify a default value of 'None'
    username = EntityValue(None)
    # or provide no argument to imply 'None'
    password = EntityValue()
    # default value of 1
    active = EntityValue(1)
    date_created = EntityValue(datetime.datetime.utcnow())
    login_attempts = EntityValue(0)

    # specify the name of the entity kind.
    # This is REQUIRED. Raises ValueError otherwise
    __kind__ = "user"

    # optionally add properties to exclude from datastore indexes
    __exclude_from_index__ = ['password']

    # call the super class here
    def __init__(self, **kwargs):
        super(UserDa, self).__init__(**kwargs)



class UserDaSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    username = fields.String()
    password = fields.String(allow_none=True)
    active = fields.Integer()
    date_created =  fields.DateTime()
    login_attempts = fields.Integer()

