from django.shortcuts import render,redirect
from . models import *
from .form import empform
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def index(request):
    emp = Employee.objects.all()
    return render(request,'index.html',{'model':emp})

def add_employee(request):
    try:
        form = empform
        if request.method =='POST':
            form = empform(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request,'Employee Created SuccessFully')
                return redirect('/')
    except Exception as e:
        print(e)
    return render(request,'add_emp.html',{'form':form})

def remove_employee(request,id):
    a = Employee.objects.get(id = id)
    a.delete()
    messages.info(request,'Employee Delete SuccessFully')
    return redirect('/')

def filter_employee(request):
    try:
        emp = Employee.objects.all()
        if request.method =='POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            dep = request.POST['dep']
            role = request.POST['role']
            print(dep)
            print(role)

            if fname:
                emp = Employee.objects.filter(first_name__icontains=fname)
            elif lname:
                emp = Employee.objects.filter(last_name__icontains=lname)
            elif dep:
                emp = Employee.objects.filter(dep__name__icontains=dep)
            elif role:
                emp = Employee.objects.filter(role__name__icontains=role)
            else:
                messages.info(request,'No Data Found')
                return redirect('/filter')     

    except Exception as e:
        print(e)



    return render(request,'filter.html',{'model':emp})
def update(request,id):
    emp = Employee.objects.get(id = id)
    form = empform(instance=emp)
    if request.method == 'POST':
            form = empform(request.POST,instance=emp)
            if form.is_valid():
                form.save()
                messages.info(request,'User Update SuccessFully')
                return redirect('/')
    return render(request,'upd_emp.html',{'form':form})
                
    return redirect('/')