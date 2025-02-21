from django.shortcuts import render, redirect
from app_services.models import Services
from django.http import HttpResponse
 
def add_serv(request):
    if request.method =='GET':
        reg_serv = Services.objects.all()
        
        return render(request, 'addserv.html')
    
    elif request.method == "POST":
        name_serv = request.POST.get('name_serv').title()
        price_serv = request.POST.get('price_serv')
        min_serv = request.POST.get('min_serv')
        
        #Check Duplicate
        
        if Services.objects.filter(name_serv = name_serv).exists():
            message = 'Service Duplicate'
            return render (request, "addserv.html", {'message': message})
        
        
        serv = Services(
            name_serv = name_serv,
            price_serv = price_serv,
            min_serv = min_serv,
        )
        
        serv.save()
        return render (request, "addserv.html")
   
def serv_list(request):    
    if request.method =='GET':        
        
        servlist = Services.objects.all().order_by('name_serv')
        
        return render (request, 'servlist.html', {'servs':servlist})
    
def serv_edit(request,id):
    
    if request.method == 'GET':
        
        serv  = Services.objects.get(id_serv=id)
        return render(request, 'edit_serv.html',{'serv':serv})
    
    if request.method == 'POST':
        serv = Services.objects.get(id_serv=id)
        attname = request.POST.get('name_serv')
        attprice = request.POST.get('price_serv')
        attminserv = request.POST.get('min_serv')
        
        #check duplicat SERV
        duplicate_servName = Services.objects.filter(name_serv=attname).exclude(id_serv=id).first()
        
        if duplicate_servName:
            
            message = 'Service Duplicate'
            return render(request, "addserv.html", {'message': message})
        else:
            serv.name_serv = attname
            serv.price_serv = attprice
            serv.min_serv = attminserv
            serv.save()
            
            return redirect('listaserv')
        
def serv_delete(request, id):
    
    try:
        service=Services.objects.get(id_serv=id)
        service.delete()
               
        return redirect('listaserv')
    
    except RegUser.DoesNotExist:
        return HttpResponse("Serviço não encontrado.", status=404)