from django.db import models
# from django.contrib.models.auth import User

class File(models.Model):
    file = models.FileField(upload_to='files')
