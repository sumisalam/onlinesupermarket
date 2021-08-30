from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from adminapp.models import  *
from django.contrib.auth import logout



# Create your views here.



def index(request):
    return render(request,"index.html")
def signup(request):
    if request.method=="POST":
        nm=request.POST.get('name')
        ad=request.POST.get('address')
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        username=request.POST.get('username')
        ps=request.POST.get('psw')

        obj1=login()
        obj1.username=username
        obj1.password=ps
        obj1.role="client"
        obj1.save()

        obj2=register()
        obj2.name=nm
        obj2.address=ad
        obj2.email=em
        obj2.phone=ph
        obj2.username=username
        obj2.password=ps
        obj2.log=obj1
        obj2.save()
        return HttpResponse("account created")


    else:
        return render(request,"register.html")
def signin(request):
    if request.method=="POST":

        un = request.POST.get('username')
        ps = request.POST.get('password')
        if login.objects.filter(username=un, password=ps).exists():
            obj = login.objects.filter(username=un, password=ps)
            for i in obj:
                r=i.role
                lid=i.id
                request.session['sid']=lid
                if r=="client":
                    reg=register.objects.get(log_id=lid)
                    name=reg.name

                    return render(request,"clienthome.html",{'name':name})
                elif r=="admin":
                    return render(request,"adminhome.html")
                else:
                    return HttpResponse("Error")
        else:
            error= 'Invalid login data'
            return render(request, "login.html",{'error':error})
    else:
        return render(request, "login.html")

    #todisplay all products
def display(request):
    obj = products.objects.all()
    for i in obj:

        return render(request, "product.html", {'obj': obj})


def product(request,id): #displaydetailspageofeach
    p = products.objects.get(id=id)
    return render(request, "details.html", {"p": p})



def detail(request,id):
    p = products.objects.get(id=id)
    nm = p.name
    w = p.price
    loginid = request.session['sid']
    reg = register.objects.get(log_id=loginid)
    if request.method=="POST":
        qt=request.POST.get('qty')
        c = int(qt) * int(w)

        obj=details1()
        obj.proname=nm
        obj.price=w
        obj.quantity=qt
        obj.total=c
        obj.img = p.img
        obj.user = reg.name
        obj.uid = reg
        obj.pid = p

        obj.save()



        return cart1(request)
    else:

        return render(request, "details.html", {'p': p})

def cart1(request):
    loginid = request.session['sid']
    ord = details1.objects.filter(uid_id=loginid)
    p=[]
    for i in ord:
        prod=products.objects.get(id=i.pid_id)
        p.append(prod)
    suma=[]
    for j in ord:
        suma.append(j.total)
    c=(sum(suma))

    return  render(request,"cart.html",{"ord":ord,'p':p,'c':c,})



def payment(request):
    loginid = request.session['sid']
    ord = details1.objects.filter(uid_id=loginid)
    suma = []
    for j in ord:
        suma.append(j.total)
    c = (sum(suma))

    return HttpResponse("payment successful")

def remove(request,id):

    ord = details1.objects.get(id=id)
    ord.delete()
    return render(request, "cart.html", {'ord': ord})

def log(request):
    if request.method=="POST":
        logout(request)
        return redirect('/')












