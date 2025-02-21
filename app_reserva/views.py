from django.shortcuts import render, redirect
from .models import Reserva
from django.http import HttpResponse
from app_agenda.models import RegUser
from app_services.models import Services


def addreserva(request):
    clientes = RegUser.objects.all()
    servicos = Services.objects.all()
    
    if request.method == 'POST':
        client_id = request.POST.get('cliente')
        serv_id = request.POST.get('service')
        date_reserv = request.POST.get('data')
        
        cliente = RegUser.objects.get(id_user=client_id)
        servico = Services.objects.get(id_serv=serv_id)
        
        
        reserv = Reserva(reserv_client=cliente, service_client=servico, date_reserv=date_reserv) #TROQUEI NOME DO BANCO DE DADOS VERIFICAR PARA SALVAR O CODIGO DO CLIENTE E O NOME PARA APRENSENTAR NA LISTA DE RESERVAS
        print(reserv)
        reserv.save()
        
    return render(request,'addreserva.html', {'clientes':clientes, 'servicos':servicos})

def listReservation(request):
    if request.method == 'GET':
        listreserv = Reserva.objects.all().order_by('date_reserv')
        
        return render(request, 'listReservation.html', {'lstreserv':listreserv})
    
def deletReserv(request, id):
    
    try:
        reserv = Reserva.objects.get(id_reserv=id)
        print(id)
        reserv.delete()
        
        return redirect('listReservation')
    
    except Reserva.DoesNotExist:
        
        return HttpResponse('RESERVATION NOT FOUND', status=404)