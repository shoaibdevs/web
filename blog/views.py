from django.shortcuts import render, redirect 
from .models import GeeksModel 
from .forms import GeeksForm 
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AuthUser
from .forms import LoginForm

# Create your views here.

@login_required(login_url='/login/')
def data_views(request):

    if request.method == "POST":
        form = GeeksForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/table')
            except:
                pass
    else:
        form = GeeksForm()

    return render(request,'admin/add.html',{'form':form})

@login_required(login_url='/login/')
def show_views(request):

    news = GeeksModel.objects.all()

    return render(request,"admin/table.html",{'news':news})


@login_required(login_url='/login/')
def edit_views(request, id):

    students = GeeksModel.objects.filter(id=id)

    return render(request,'edit.html', {'students':students})

@login_required(login_url='/login/')
def update_views(request, id):

    students = GeeksModel.objects.filter(id=id)
    form = GeeksForm(request.POST or None, instance = students)

    if form.is_valid():
        form.save()
        return redirect("/show")

    return render(request, 'edit.html', {'form': form})

@login_required(login_url='/login/')
def delete_views(request, id):

    students = GeeksModel.objects.get(id=id)
    students.delete()

    return redirect("/table")

@login_required(login_url='/login/')
def panel_views(request):
    return render(request, 'admin/adminbase.html')

@login_required(login_url='/login/')
def signup_views(request):
    if request.method =='POST':
         username = request.POST['username']
         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         email = request.POST['email']
         password = request.POST['password']
         #password1 = request.POST['password1']

         user = User.objects.create_user(username = username , first_name = first_name, last_name = last_name , email = email, password = password  )#, password2 = password2 ,  password2 = password2
         user.save()
         return redirect('/')

    else:
        return render(request, 'admin/signup.html',)

@login_required(login_url='/login/')
def user_show(request):
    marks_data = AuthUser.objects.all()
        
    return render(request, 'admin/user.html', {'marks_data' : marks_data})



def login_views(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/panel')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'admin/login.html', {'form': form})


def logout_views(request):
    logout(request)
    return redirect('/login')


