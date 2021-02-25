from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentRegistration
from .models import Users


# Create your views here.

def index(request):
    if request.method == 'POST':
        data = request.POST
        student_data = Users.objects.create(
            name=data['name'],
            email=data['email'],
            password=data['password'],
        )
        return redirect('show')

    return render(request, 'index.html')


def viewinfo(request):
    data = Users.objects.all()
    return render(request, 'show.html', {'data': data})


def update_data(request, id):
    if request.method =='POST':
        pi = Users.objects.get(id=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = Users.objects.get(id = id)
        fm = StudentRegistration(instance=pi)
    return render(request,'update.html', {"form":fm})


def delete(request, id):
    sid = Users.objects.get(id=id)
    sid.delete()
    return redirect('/show')
