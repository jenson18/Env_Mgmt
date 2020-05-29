
from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('Env/',views.env_form,name='Env_insert'), #get & post request for insert operations
    path('<int:id>/',views.env_form,name='Env_update'), #get & post request for udpate operations
    path('list/',views.env_list,name='Env_list'), #get request to retrive & display all records
    path('delete/<int:id>/',views.env_delete,name='Env_delete'),
    path('logout/', views.logout_user, name='logout'),
]