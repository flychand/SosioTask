from django.shortcuts import render, redirect
from .models import Member
import datetime
#from datetime import datetime

# Create your views here.

def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/index.html', context)

def create(request):
    member = Member(fullname=request.POST['fullname'], food=request.POST['food'],clothes=request.POST['clothes'],housekeeping=request.POST['housekeeping'],medicine=request.POST['medicine'],fun=request.POST['fun'])

    F=member.food = request.POST['food']
    C=member.clothes = request.POST['clothes']
    H=member.housekeeping = request.POST['housekeeping']
    M=member.medicine = request.POST['medicine']
    F=member.fun = request.POST['fun']
    
    total=member.total=int(F)+int(C)+int(H)+int(M)+int(F)
    datte=member.datte=datetime.date.today()
    
    #print(datte)
    
    
    member.save()
    return redirect('/')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.fullname = request.POST['fullname']
    member.food = request.POST['food']
    member.clothes = request.POST['clothes']
    member.housekeeping = request.POST['housekeeping']
    member.medicine = request.POST['medicine']
    member.fun = request.POST['fun']
    member.save()
    return redirect('/crud/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')
