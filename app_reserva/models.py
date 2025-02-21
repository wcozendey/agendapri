from django.db import models
from app_agenda.models import RegUser
from app_services.models import Services

class Reserva(models.Model):
    id_reserv = models.AutoField(primary_key=True)
    reserv_client = models.ForeignKey(RegUser, on_delete=models.CASCADE)
    service_client = models.ForeignKey(Services, on_delete=models.CASCADE)
    date_reserv = models.DateField()