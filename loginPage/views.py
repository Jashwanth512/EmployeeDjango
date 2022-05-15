from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .models import AdminPassword,AdminUsername,Users
from django.shortcuts import redirect

def getPresentUsers():
    employees=[]
    for e in (Users.objects.all()):
        employees.append([e.id,e.name,e.phonenumber,e.email])
    return employees

def employeesPage(request):
    employees=getPresentUsers()
    return render(request,"employees.html",{'employees':employees})
    

def login(request):
    return render(request,"login.html")

def authenticate(request):
    storedusername=AdminUsername.objects.all().values()[0]['username']
    storedpassword=AdminPassword.objects.all().values()[0]['password']
    USERNAME=request.POST.get("username")
    PASSWORD=request.POST.get("password")
    if storedusername==USERNAME and storedpassword==PASSWORD:
        return redirect('login/empolyeesPage',foo='bar')
        # employees=getPresentUsers()
        # return render(request,"employees.html",{'employees':employees})
    else:
        return render(request,'incorrectCreds.html')

def employeeIndividualPage(request,e_id):
    j=Users.objects.get(pk=e_id)
    return render(request,'Employee.html',{'employee':j})

def updateEmployee(request,e_id):
    employeeID=e_id
    updatedName=request.POST.get('empName')
    updatedNum=request.POST.get('empNum')
    updatedEmail=request.POST.get('empEmail')
    q=Users.objects.get(pk=employeeID)
    q.name=updatedName
    q.phonenumber=updatedNum
    q.email=updatedEmail
    q.save()
    # return redirect()
    employees=getPresentUsers()
    return render(request,"employees.html",{'employees':employees})

def newUserPage(request):
    return render(request,'newUser.html')

def createNewUser(request):
    Name=request.POST.get('Name')
    PhoneNumber=request.POST.get('Number')
    Email=request.POST.get('Email')
    q=Users(name=Name,phonenumber=PhoneNumber,email=Email)
    q.save()
    employees=getPresentUsers()
    return render(request,'employees.html',{'employees':employees})

def logout(request):
    return render(request,'login.html')

def deleteUser(request,e_id):
    u=Users.objects.get(pk=e_id)
    u.delete()
    employee=getPresentUsers()
    return render(request,'employees.html',{'employees':employee})