from django.urls import path
from . import views
app_name='loginPage'

urlpatterns=[path("",views.login,name='login'),
path("login",views.authenticate,name="receive"),
path("login/<int:e_id>",views.employeeIndividualPage,name='Employee'),
path("login/updateEmployee/<int:e_id>",views.updateEmployee,name="updateEmployee"),
path("login/newUserPage",views.newUserPage,name='newUserPage'),
path('login/createNewUser',views.createNewUser,name='createNewUser'),
path('login/logout',views.logout,name='logout'),
path('login/deleteUser/<int:e_id>',views.deleteUser,name='deleteUser'),
path('login/empolyeesPage',views.employeesPage,name='employeesPage'),]