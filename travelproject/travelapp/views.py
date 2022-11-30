
from django.shortcuts import render
from.models import Place
from.models import Persons

# Create your views here


def demo(request):
    obj=Place.objects.all()
    obj1=Persons.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})


#def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    z=x+y
#    a=x-y
#    b=x*y
#    c=x/y
 #   return render(request,"result.html",{'add':z,'sub':a,'mul':b,'div':c})