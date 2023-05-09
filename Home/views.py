from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from Home.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")
ap=client['Appointments']
cardiology=ap.Detail
pediatrics=ap.Details
gastroenterology=ap.Details
psychology=ap.Details
dermatology=ap.Details
sc=client['Diagnostictests']
pulmonaryFuctionTest=sc.details
endoscopy=sc.details
bloodTest=sc.details
urineTest=sc.details
im=client['Imagingtests']
ultraSound=im.de
xray=im.de
ctscan=im.de
kemo=client['Chemotherapy']
Chemotherapy=kemo.kee
def index(request):
    if request.user.is_anonymous:
        return redirect('two')
  
    return render(request,"index.html")
def about(request):
    if request.user.is_anonymous:
        return redirect('two')
    return render(request,"about.html")
def logo(request):
    if request.user.is_anonymous:
        return redirect('two')
    return render(request,'logo.html')

def tests(request):
    if request.user.is_anonymous:
        return redirect('two')
    return render(request,'tests.html')
def come(request):
    if request.user.is_anonymous:
        return redirect('two')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')

        a=Cardiology(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        b={"name":name,"email":email,"phone":phone,"desc":desc}
        ap.cardiology.insert_one(b)
        a.save()
        messages.success(request,'your Appointment has been Booked') 
    return render(request,"contact.html")
def Logout(request):
    logout(request)
    return redirect('two')
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            context = {'error_message': 'This username or email is already used'}
            return render(request, 'signup2.html', context=context)
        else:
            my_user = User.objects.create_user(username, email, password)
            my_user.save()
            return redirect('two')

    return render(request, 'signup2.html')
def loginin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("wrong user name or password")

    return render(request,"signin.html")
def profile(request):
    return render(request,"profile.html")
def come2(request):
    if request.user.is_anonymous:
        return redirect('two')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        ped=Pediatrics(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        ped.save()
        b1={"name":name,"email":email,"phone":phone,"desc":desc}
        ap.pediatrics.insert_one(b1)
        messages.success(request,'your Appointment has been Booked') 
    return render(request,"pe.html")
def come3(request):
    if request.user.is_anonymous:
        return redirect('two')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        g=Gastroenterology(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        g.save()
        b2={"name":name,"email":email,"phone":phone,"desc":desc}
        ap.gastroenterology.insert_one(b2)
        messages.success(request,'your Appointment has been Booked') 
    return render(request,"ga.html")
def come4(request):
    if request.user.is_anonymous:
        return redirect('two')
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        ps=Psychology(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        ps.save()
        b3={"name":name,"email":email,"phone":phone,"desc":desc}
        ap.psychology.insert_one(b3)
        messages.success(request,'your Appointment has been Booked') 
    return render(request,"ps.html")
def come5(request):
    if request.user.is_anonymous:
        return redirect('two')
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        de=Dermatology(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        de.save()
        b4={"name":name,"email":email,"phone":phone,"desc":desc}
        ap.dermatology.insert_one(b4)
        messages.success(request,'your Appointment has been Booked') 
    return render(request,"de.html")

def scan1(request):
    if request.user.is_anonymous:
        return redirect('two')

    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        
        bt=BloodTest(name=name,age=age,phone=phone,desc=desc,date=datetime.today())
        bt.save()
        b11={"name":name,"age":age,"phone":phone,"desc":desc}
        sc.bloodTest.insert_one(b11)
        messages.success(request,'your test has been Booked!') 
    return render(request,"bloodtest.html")

def scan2(request):
    if request.user.is_anonymous:
        return redirect('two')

    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')

        cs=CtScan(name=name,age=age,phone=phone,desc=desc,date=datetime.today())
        cs.save()
        b111={"name":name,"age":age,"phone":phone,"desc":desc}
        im.ctscan.insert_one(b111)
        messages.success(request,'your Appointment has been Booked!') 
    return render(request,"ctscan.html")

def scan3(request):
    if request.user.is_anonymous:
        return redirect('two')

    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')

        k=Kemotheraphy(name=name,age=age,phone=phone,desc=desc,date=datetime.today())
        k.save()
        b1411={"name":name,"age":age,"phone":phone,"desc":desc}
        kemo.Chemotherapy.insert_one(b1411)
        messages.success(request,'your Appointment has been Booked!') 
    return render(request,"kemotheraphy.html")

def scan4(request):
    if request.user.is_anonymous:
        return redirect('two')

    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')

        xr=XRay(name=name,age=age,phone=phone,desc=desc,date=datetime.today())
        xr.save()
        b222={"name":name,"age":age,"phone":phone,"desc":desc}
        im.xray.insert_one(b222)
        messages.success(request,'your Appointment has been Booked!') 
    return render(request,"xray.html")


def scan5(request):
    if request.user.is_anonymous:
        return redirect('two')

    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')

        end=Endoscopy(name=name,age=age,phone=phone,desc=desc,date=datetime.today())
        end.save()
        b12={"name":name,"age":age,"phone":phone,"desc":desc}
        sc.endoscopy.insert_one(b12)
        messages.success(request,'your Appointment has been Booked!') 
    return render(request,"endoscopy.html")


def scan6(request):
    if request.user.is_anonymous:
        return redirect('two')

    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')

        ut=UrineTest(name=name,age=age,phone=phone,desc=desc,date=datetime.today())
        ut.save()
        b14={"name":name,"age":age,"phone":phone,"desc":desc}
        sc.urineTest.insert_one(b14)
        messages.success(request,'your Appointment has been Booked!') 
    return render(request,"urinetest.html")

def scan7(request):
    if request.user.is_anonymous:
        return redirect('two')

    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')

        us=UltraSound(name=name,age=age,phone=phone,desc=desc,date=datetime.today())
        us.save()
        b333={"name":name,"age":age,"phone":phone,"desc":desc}
        im.ultrasound.insert_one(b333)
        messages.success(request,'your Appointment has been Booked!') 
    return render(request,"ultrasound.html")


def scan8(request):
    if request.user.is_anonymous:
        return redirect('two')

    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')

        pt=PulmonaryFuctionTest(name=name,age=age,phone=phone,desc=desc,date=datetime.today())
        pt.save()
        b13={"name":name,"age":age,"phone":phone,"desc":desc}
        sc.pulmonaryFuctionTest.insert_one(b13)
        messages.success(request,'your Appointment has been Booked!') 
    return render(request,"pulmonaryfunctiontest.html")

def management(request):
    cardiology=Cardiology.objects.all()
    pediatrics=Pediatrics.objects.all()
    gastroenterology=Gastroenterology.objects.all()
    psychology=Psychology.objects.all()
    dermatology=Dermatology.objects.all()
    bloodTest=BloodTest.objects.all()
    ctScan=CtScan.objects.all()
    kemotheraphy=Kemotheraphy.objects.all()
    xRay=XRay.objects.all()
    urineTest=UrineTest.objects.all()
    ultraSound=UltraSound.objects.all()
    pulmonaryFuctionTest=PulmonaryFuctionTest.objects.all()
    
    context={"cardiology":cardiology,"pediatrics":pediatrics,"gastroenterology": gastroenterology,"psychology":psychology,"dermatology":dermatology
         , "bloodTest":bloodTest,"ctScan":ctScan, " kemotheraphy": kemotheraphy,"xRay":xRay, "urineTest":urineTest,"ultraSound":ultraSound,
         "pulmonaryFuctionTest":pulmonaryFuctionTest  }
    return render(request,"management.html",context)