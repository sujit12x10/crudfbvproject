from django.shortcuts import render,redirect
from testApp.models import EmployeeForm
from testApp.forms import EmployeeForm1

# Create your views here.

def retrieve_view(request):
    employees = EmployeeForm.objects.all()
    return render(request,'testApp/home.html',{'employees':employees})

def create_view(request):
    form = EmployeeForm1()   
    if request.method == "POST":
        form = EmployeeForm1(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testApp/create.html',{'form':form})

def delete_view(request,id):
    employee = EmployeeForm.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    employee = EmployeeForm.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm1(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testApp/update.html',{'employee':employee})
