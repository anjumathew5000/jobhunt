from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Student

# Create your views here.

def index(request):
    return HttpResponse("<h1>hello</h1>")
def reg(request):
    return render(request,'reg.html')
def regdata(request):
    if request.method=='POST':
        name=request.POST.get('na')
        age=request.POST.get('age')
        email=request.POST.get('email')
        obj=Student(name=name,age=age,email=email)
        obj.save()
        return HttpResponse('created')

def regtable(request):
    data=Student.objects.all()
    print(data)
    return render(request,'regtable.html',{'data':data})
def deleteobject(request,dataid):
    d=Student.objects.filter(id=dataid)
    d.delete()
    return redirect(regtable)
