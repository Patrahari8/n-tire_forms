from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def topic_table(request):
    if request.method=='POST':
        TN=request.POST['tn']
        to=topic.objects.get_or_create(topic_name=TN)[0]
        to.save()
        tod=topic.objects.all()
        d={'tod':tod}
        return render(request,'topic_data.html',d)
    return render(request,'topic_table.html')

def webpage_insert(request):
    qsto=topic.objects.all()
    d1={'qsto':qsto}
    if request.method=='POST':
        TN=request.POST['tn']
        tt=topic.objects.get(topic_name=TN)
        N=request.POST['n']
        U=request.POST['u']
        Wo=webpage.objects.get_or_create(topic_name=tt,name=N,url=U)[0]
        Wo.save()
        Wod=webpage.objects.all()
        d={'Wod':Wod}
        return render(request,'webpage_data.html',d)
    return render(request,'webpage_insert.html',d1)

def ar_insert(request):
    qswo=webpage.objects.all()
    d1={'qswo':qswo}
    if request.method=='POST':
        N=request.POST['n']
        no=webpage.objects.get(pk=N)
        A=request.POST['a']
        D=request.POST['d']
        E=request.POST['e']
        Ao=access_records.objects.get_or_create(name=no,author=A,date=D,email=E)[0]
        Ao.save()
        arod=access_records.objects.all()
        d={'arod':arod}
        return render(request,'ar_data.html',d)
    return render(request,'ar_insert.html',d1)