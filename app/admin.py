from django.contrib import admin
# from .models import Manager
# from .models import Employee
from .models import Project
from .models import Task
from .models import Payment
# Register your models here.
# admin.site.register(Manager)
# admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Payment)


