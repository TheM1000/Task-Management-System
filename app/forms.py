from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django.forms import ModelForm
from  django import forms
from .models import Payment, Project, Task
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User






class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

        widgets = {
            'project_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Give name to your project'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'This is where you describe about project'}),
            # 'project_status': forms.RadioSelect(attrs={'class':'form-control','placeholder':'check if the project is completed'}),
            'project_date': forms.DateTimeInput(attrs={'class':'form-control','placeholder':'Enter date when project started'}),
            'pbudget': forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Amount allocated for the project'}),
            'pend_date': forms.DateTimeInput(attrs={'class':'form-control','placeholder':'Expected end date? YYYY-MM-DDD HH-MM-SS'}),
            'ptotalcost': forms.NumberInput(attrs={'class':'form-control,checkbox-inline','placeholder':'Expected cost'}),

        }

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
    
            
        widgets = {
            'project': forms.Select(attrs={'class':'form-control'}),
            'task_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name the task'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'This is where you describe about the task'}),
            'task_hour': forms.NumberInput(attrs={'class':'form-control','placeholder':'Expected hours to complete the task'}),
            'task_cost': forms.NumberInput(attrs={'class':'form-control','placeholder':'Expected pay'}),
            'task_status': forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'task_priority': forms.TextInput(attrs={'class':'form-control','placeholder':'State the urgency of the task'}),
            'employee': forms.Select(attrs={'class':'form-control,checkbox-inline'}),

        }

class AddPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields= '__all__'

        widgets = {
            'Task': forms.Select(attrs={'class':'form-control'}),
            'pay_amount': forms.NumberInput(attrs={'class':'form-control','placeholder':'Amount to be paid'}),
            'pay_date': forms.DateInput(attrs={'class':'form-control','placeholder':'paid on YYYY-MM-DD'}),
            # 'pay_status': forms.CheckboxInput(attrs={'class':'form-control','placeholder':'payment status'}),
            'pay_type': forms.TextInput(attrs={'class':'form-control','placeholder':'means of payment'}),
            'transaction_no': forms.NumberInput(attrs={'class':'form-control','placeholder':'fill if paid online'}),
            'cheque_no': forms.NumberInput(attrs={'class':'form-control','placeholder':'fill if paid through cheque'}),

        }

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['review']
# class UploadForm(forms.Form):
#     file= forms.FileField()

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

      
class UserUpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_status']
    
            
        widgets = {
            
            'task_status': forms.NullBooleanSelect(attrs={'class':'form-control'}),
            
        }
