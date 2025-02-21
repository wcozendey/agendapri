from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import RegUser

from django.contrib.auth.decorators import login_required



def home(request):

    return render(request, 'index.html')


@login_required()
def addcli(request):

    if request.method=='GET':

        Reg_user = RegUser.objects.all()

        return render(request, "addclient.html")
    

    elif request.method=="POST":

        name=request.POST.get("name").title()

        birthday=request.POST.get("birthday")
        

        telephone=request.POST.get("telephone")
        
        #Check line none
        
        if not name or not birthday or not telephone:
            message = 'empty is not correct'
            return render(request, 'addclient.html', {'message':message})

        #Check Format Birthday
        import re
        if not re.match(r'\d{2}/\d{2}', birthday):
            message = 'Please insert format correct in birthday DD/MM'
            return render(request, "addclient.html", {'message': message})
        
        
        
        #Check interger Number
        
        if not telephone.isdigit():
            message = 'Please only number in telephone'
            return render(request, 'addclient.html',{'message':message})

        #check Duplicate

        if RegUser.objects.filter(telephone=telephone).exists():

            message = 'Client Duplicate'

            return render(request, "addclient.html", {'message': message})
        

        client = RegUser(
            
            name =name,
            birthday = birthday,
            telephone = telephone
        )
        
        client.save()
        message = 'Client Save'
        return render(request, "addclient.html", {'message':message})
    
    

@login_required()    
def client_list(request):
    
    if request.method =='GET':
        
        clientlist = RegUser.objects.all().order_by('name')
        return render (request, 'client_list.html', {'clients':clientlist})


@login_required()
def editclient(request, id):
    
    if request.method =='GET':
            
        client = RegUser.objects.get(id_user=id)
        return render (request, 'editclient.html',{'client':client})
    

    if request.method == 'POST':
        
        client = RegUser.objects.get(id_user=id)
        
        attname = request.POST.get('name').title()
        attbirthday = request.POST.get('birthday')
        atttelephone = request.POST.get('telephone')
        
        
        #check Diplicate

        
        if RegUser.objects.filter(telephone=atttelephone).exclude(id_user=id).first():
            message = 'Client Duplicate'
            return render(request, "editclient.html", {'message': message, 'client': {'name': attname, 'birthday': attbirthday, 'telephone': atttelephone}})
        
        
        
        else:
            client.name = attname
            client.birthday = attbirthday
            client.telephone = atttelephone
            client.save()
            message= 'Client Update Successfully'
            
            return redirect('client_list')
    

@login_required()    

def deleteclient(request, id):

    try:

        client = RegUser.objects.get(id_user=id)
        print(id)
        client.delete()
        
        
        
        message= "Client deleted"
        
        clients = RegUser.objects.all()

        return render(request, 'client_list.html',{'clients': clients, 'message': message})
    
        


    except RegUser.DoesNotExist:

        return HttpResponse("Usuário não encontrado", status=404)