from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from .info import add_user, delete_user, view_users


def main(request):
    if request.POST:
        usr_Name = request.POST['usrName']
        pswd = request.POST['pswd']
        try:
            person = Person.objects.get(userName=usr_Name, password=pswd)
            add_user(person)
            view_users()
            return render(request, "main/main.html", {
                'usrName': person.userName,
                'name': person.name,
                'pswd': person.password,
                'email': person.email,
                'phone': person.phone,
            })
        except Person.DoesNotExist:
            return render(request, "main/main.html", {
                'usrName': 11,
                'name': None,
                'pswd': None,
                'email': None,
                'phone': None,
            })

    else:
        return render(request, "main/main.html", {
            'usrName': None,
            'name': None,
            'pswd': None,
            'email': None,
            'phone': None,
        })


def register(request):
    return render(request, "main/register.html", {
    })


def add(request):
    person = Person()
    person.name = request.POST['name']
    person.email = request.POST['email']
    person.phone = request.POST['phone']
    person.userName = request.POST['usrName']
    person.password = request.POST['pswrd']
    person.save()
    return redirect('/')


def check_usr(request):
    try:
        usr_Name = request.GET['usrName']
        person = Person.objects.get(userName=usr_Name)
        return HttpResponse("exist")
    except Person.DoesNotExist:
        return HttpResponse('None')


def check_mail(request):
    try:
        usr_mail = request.GET['usrMail']
        person = Person.objects.get(email=usr_mail)
        return HttpResponse("exist")
    except Person.DoesNotExist:
        return HttpResponse('None')


def log_out(request):
    usr_name = request.GET['usrName']
    person = Person.objects.get(userName=usr_name)
    delete_user(person)
    view_users()
    return redirect('/')


