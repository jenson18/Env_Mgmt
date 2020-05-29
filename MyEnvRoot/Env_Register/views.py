from django.shortcuts import render,redirect
from . forms import EnvForm
from . models import EnvList_New
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, admin_only

# Create your views here.

def login_page(request):
    print("inside login function")
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/Env/list/')
        else:
            print("inside else for user login function")
            messages.error(request, 'Incorrect Username or Password')

    context = {}
    return render(request,"Env_register/Login.html",context)

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','Guest'])
def env_list(request):

    context={'Env_List':EnvList_New.objects.all()}
    return render(request,"Env_Register/Env_List.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
#@login_required(login_url='login')
def env_form(request,id=0):
    if request.method =="GET":
        if id==0:
            form =EnvForm() #create an object of the form we created
        else:
            env=EnvList_New.objects.get(pk=id)
            form = EnvForm(instance=env)
        return render(request,"Env_Register/Env_form.html",{'form':form})
    else:
        if id==0:
            form =EnvForm(request.POST)
        else:
            env = EnvList_New.objects.get(pk=id)
            form = EnvForm(request.POST,instance=env)
        if form.is_valid():

            form.save()

        return  redirect('/Env/list/')



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
#@login_required(login_url='login')
def env_delete(request,id):
    env = EnvList_New.objects.get(pk=id)
    env.delete()
    return  redirect('/Env/list/')