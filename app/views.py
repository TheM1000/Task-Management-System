from ast import Pass
import email
import math
from django.shortcuts import render, redirect
from multiprocessing import AuthenticationError, context
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from app.forms import AddProjectForm,AddTaskForm,AddPaymentForm
from .models import *
from .forms import CreateUserForm, UserUpdateTaskForm
from django.contrib import messages
from django.conf import settings
# Create your views here.

@login_required
def index(request):
   
    return render(request,'index.html')

@login_required
def AddProject(request):
    AddProject_form = AddProjectForm()

    if request.method == "POST":
        AddProject_form = AddProjectForm(request.POST)

        if AddProject_form.is_valid():
            AddProject_form.save()
            return redirect('/')
    return render(request,'AddProject.html',{'AddProject_form': AddProject_form})

@login_required
def AddTask(request):
    AddTask_form = AddTaskForm()

    if request.method == "POST":
        AddTask_form = AddTaskForm(request.POST)

        if AddTask_form.is_valid():
            AddTask_form.save()
            return redirect('/')
    return render(request,'AddTask.html',{'AddTask_form': AddTask_form})

@login_required
def AddPayment(request):
    AddPayment_form = AddPaymentForm()

    if request.method == "POST":
        AddPayment_form = AddPaymentForm(request.POST)

        if AddPayment_form.is_valid():
            AddPayment_form.save()
            return redirect('/')
    return render(request,'AddPayment.html',{'AddPayment_form': AddPayment_form})

@login_required
def get_projects(request, page_number):
    page_size = 5
    if page_number <1:
        page_number = 1
    project_count = Project.objects.count()
    last_page = math.ceil(project_count / page_size)

    pagination = {
        'previous_page': page_number-1,
        'current_page': page_number,
        'next_page': page_number+1,
        'last_page': last_page
    }
    projects=Project.objects.all()[(page_number-1)* page_size:page_number*page_size]
    return render(request,'Projects.html',{'projects':projects,'pagination': pagination})

# @login_required
# def get_tasks(request, page_number, **kwargs):
    
#     page_size = 2
#     if page_number <1:
#         page_number = 1
#     task_count = Task.objects.count()
#     last_page = math.ceil(task_count / page_size)

#     pagination = {
#         'previous_page': page_number-1,
#         'current_page': page_number,
#         'next_page': page_number+1,
#         'last_page': last_page
#     }

#     print(Task.objects.all())
#     tasks=Task.objects.all()[(page_number-1)* page_size:page_number*page_size]
#     return render(request,'Tasks.html',{'tasks':tasks,'pagination': pagination})

@login_required
def get_tasks(request, page_number, **kwargs):
    # context['tasks']=context['tasks'].filter(complete=False).count()
    
    page_size = 5
    if page_number <1:
        page_number = 1
    task_count = Task.objects.count()
    last_page = math.ceil(task_count / page_size)

    pagination = {
        'previous_page': page_number-1,
        'current_page': page_number,
        'next_page': page_number+1,
        'last_page': last_page
    }

    tasks = None
    if request.user.is_superuser:
        tasks = Task.objects.all()
    else:
        tasks=Task.objects.filter(employee=request.user).all()[(page_number-1)* page_size:page_number*page_size]
    return render(request,'Tasks.html',{'tasks':tasks,'pagination': pagination})

@login_required
def get_payments(request, page_number):
    page_size = 5
    if page_number <1:
        page_number = 1
    payment_count = Payment.objects.count()
    last_page = math.ceil(payment_count / page_size)

    pagination = {
        'previous_page': page_number-1,
        'current_page': page_number,
        'next_page': page_number+1,
        'last_page': last_page
    }
    payments=Payment.objects.all()[(page_number-1)* page_size:page_number*page_size]
    return render(request,'Payments.html',{'payments':payments,'pagination': pagination})

@login_required
def update_project(request,id):
    project = Project.objects.get(pk=id)

    if request.method == "POST":
        project_form = AddProjectForm(request.POST, instance=project)

        if project_form.is_valid():
            project_form.save()
            return redirect('/projects/page/1/'.format(id))
    project_form = AddProjectForm(instance=project)
    return render(request,'update_project.html',{'project_form': project_form})

@login_required
def delete_project(request, id):
    project = Project.objects.get(pk=id)
    project.delete()

    return redirect('/')

@login_required
def update_task(request,id):
    task = Task.objects.get(pk=id)
    task_form = AddTaskForm(instance=task)
    if request.method == "POST":
        if request.user.is_superuser==True:
            task_form = AddTaskForm(request.POST, instance=task)
        else:
            task_form = UserUpdateTaskForm(request.POST, instance=task)

        if task_form.is_valid():
            task_form.save()
            return redirect('/tasks/page/1/'.format(id))
        else:
            print(task_form.errors)
        #     print("Hello",request.POST["task_status"])
        #     print("Hello",request.POST["project"])
        #     print("Hello",request.POST["task_name"])
            
        #     bul=request.POST["task_status"]
        #     if bul:
        #         print("Hello",request.POST["task_status"])
        #         task_form.save()
        #         return redirect('/tasks/page/1/'.format(id))
            
    
    return render(request,'update_task.html',{'task_form': task_form})

@login_required
def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()

    return redirect('/')

@login_required
def update_payment(request,id):
    payment = Payment.objects.get(pk=id)

    if request.method == "POST":
        payment_form = AddPaymentForm(request.POST, instance=payment)

        if payment_form.is_valid():
            payment_form.save()
            return redirect('/payments/page/1/'.format(id))
    payment_form = AddPaymentForm(instance=payment)
    return render(request,'update_payment.html',{'payment_form': payment_form})

@login_required
def delete_payment(request, id):
    payment = Payment.objects.get(pk=id)
    payment.delete()

    return redirect('/')

def signin(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Please enter valid details')
    return render(request,'signin.html',{'form': form})

def signout(request):
    logout(request)
    return redirect('/')

def signup(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
    
            form.save()
            
            user =form.cleaned_data.get('username')
            password =form.cleaned_data.get('password')
            email =form.cleaned_data.get('email')
            subject ='Welcome to Apex Task Management System'
            message ='Hi please collect your account details from the Service Desk'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject,message,from_email,recipient_list,fail_silently=False)
            messages.success(request,'Account has been created for'+ user)
            
            
            
            
            return redirect('/signin')
    context = {'form':form}
    return render(request,'signup.html',context)
@login_required
def landingpage(request):
    project_count = Project.objects.count()
    task_count = Task.objects.count()
    payment_count = Payment.objects.count()
    completed_projects=Project.objects.filter(project_status=True).count()
    completed_tasks=Task.objects.filter(task_status=True).count()
    completed_payments=Payment.objects.filter(pay_status=True).count()
    incomplete_projects=Project.objects.filter(project_status=False).count()
    incomplete_tasks=Task.objects.filter(task_status=False).count()
    incomplete_payments=Payment.objects.filter(pay_status=False).count()
       
    return render(request,'landingpage.html', {'project_count':project_count, 'task_count':task_count,'payment_count':payment_count,'completed_projects':completed_projects,'completed_tasks':completed_tasks,'completed_payments':completed_payments,'incomplete_projects':incomplete_projects,'incomplete_tasks':incomplete_tasks,'incomplete_payments':incomplete_payments})

#change password with old password

def user_change_pass(request):
    if request.method == "POST":
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
          fm.save()
          return HttpResponseRedirect('/signin/')
    else:
     fm = PasswordChangeForm(user=request.user)
    return render(request,'changepass.html',{'form':fm})


