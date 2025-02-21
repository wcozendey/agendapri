from django.db import models


class RegUser(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    birthday = models.TextField(max_length=5)
    telephone = models.IntegerField()
    
    def __str__(self):
        return self.name
    
