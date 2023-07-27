from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

# class Manager(models.Model):

#     man_name=models.CharField('Manager Name',max_length=50)
#     man_email=models.EmailField()
#     man_password=models.CharField(max_length=10)

#     def __str__(self):
#         return self.man_name

# class Employee(models.Model):
#     emp_name=models.CharField('Empoyee Name',max_length=50)
#     emp_email=models.EmailField()
#     emp_password=models.CharField(max_length=10)
#     emp_phnumber=models.BigIntegerField()
#     emp_qualification=models.CharField(max_length=200)

#     def __str__(self):
#         return self.emp_name
class Project(models.Model):
    project_name=models.CharField('Project Name',max_length=120)
    description=models.TextField('Description')
    project_status=models.BooleanField('Project Status',default=False)
    project_date=models.DateTimeField('Start Date',editable=True,auto_now=True)
    pbudget=models.PositiveIntegerField('Budget',null=True)
    pend_date=models.DateTimeField('End Date',null=True,blank=True)
    ptotalcost=models.PositiveIntegerField('Total Cost',null=True)
    # tasks=models.ManyToManyField(Task)

   
    def __str__(self):
        return self.project_name

class Task(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE, null=True)
    task_name=models.CharField('Task Name',max_length=120,default="")
    description=models.TextField('Description',default="")
    task_hour=models.PositiveIntegerField(null=True)
    # Assigned_Date=models.DateTimeField('Assigned Date',null=False,blank=False,default="")
    # Submitted_Date=models.DateTimeField('Submitted Date',editable=False,auto_now=True)
    task_cost=models.PositiveIntegerField(null=True)
    task_status=models.BooleanField('Completed?',default=False)
    task_priority=models.CharField('Task Priority',max_length=50)
    employee=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.task_name
    


    

class Payment(models.Model):
    # pay_name=models.CharField('Payment To',max_length=100,default="")
    Task = models.OneToOneField(Task, on_delete=models.CASCADE)
    pay_amount=models.PositiveIntegerField()
    pay_date=models.DateField()
    pay_status=models.BooleanField(default=False)
    pay_type=models.CharField('Payment Through',max_length=100)
    transaction_no=models.BigIntegerField(null=True, blank=True)
    cheque_no=models.BigIntegerField(null=True, blank=True)
    def __str__(self):
         return self.Task


