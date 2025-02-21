from django.db import models

class Services(models.Model):
    id_serv = models.AutoField(primary_key=True)
    name_serv = models.CharField(max_length=255)
    price_serv = models.DecimalField(max_digits=10, decimal_places=2)
    min_serv = models.DecimalField(max_digits=10, decimal_places=0)
    
    def __str__(self):
        return self.name_serv