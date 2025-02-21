from django.urls import path, include
from app_services import urls
from . import views
from app_services.views import add_serv
from app_services.views import serv_list
from app_services.views import serv_edit
from app_services.views import serv_delete
from app_reserva.views import addreserva
from app_reserva.views import listReservation
from app_reserva.views import deletReserv





urlpatterns = [
    #URL'S CLIENT
    path('addcli/',views.addcli, name='addcli'),
    path('',views.home, name='home'),

    path('list/',views.client_list, name='client_list'),

    path('editclient/<int:id>',views.editclient, name='edit_client'),

    path('deleteclient/<int:id>/', views.deleteclient, name='delete_client'),
    
    #URL'S SERVICE

    path('addserv/', add_serv, name='addserv'),
    
    path('servs/', serv_list, name='listaserv'),
    
    path('servedit/<int:id>',serv_edit, name='serv_edit'),
    
    path('deleteserv/<int:id>/', serv_delete, name='serv_delete'),

    path('accounts/', include('django.contrib.auth.urls')),
    
    #URL's RESERVATION
    
    path('reserv/', addreserva, name='addreserva'),
    path('listreserv/', listReservation, name='listReservation'),
    #path('deletReserv/<int:id>/', views.deletReserv, name='delet_Reserv'),
    path('deleteReserv/<int:id>/', deletReserv, name='delete_reserv'),


]

