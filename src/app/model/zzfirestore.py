from fireo import models as mdl

class UserFS(mdl.Model):
    name = mdl.TextField()
    age = mdl.NumberField()

    class Meta:
        collection_name = "my_user"
