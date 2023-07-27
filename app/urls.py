from . import views
from django.urls import path

urlpatterns= [
    path('',views.landingpage),
    path('AddProject',views.AddProject),
    path('AddTask',views.AddTask),
    path('AddPayment',views.AddPayment),
    path('projects/page/<int:page_number>/',views.get_projects),
    path('tasks/page/<int:page_number>/',views.get_tasks),
    path('payments/page/<int:page_number>/',views.get_payments),
    path('update_project/<int:id>/', views.update_project),
    path('delete_project/<int:id>/', views.delete_project),
    path('update_task/<int:id>/', views.update_task),
    path('delete_task/<int:id>/', views.delete_task),
    path('update_payment/<int:id>/', views.update_payment),
    path('delete_payment/<int:id>/', views.delete_payment),
    path('signin/',views.signin,name="User Sign In"),
    path('signout/',views.signout,name="User Sign Out"),
    path('signup/',views.signup,name="User Sign UP"),
    path('changepass/',views.user_change_pass,name='changepass'),
]   