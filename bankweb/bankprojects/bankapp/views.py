from django.contrib import auth, messages
from django.contrib.auth.models import User


from django.shortcuts import render, redirect

from bankapp.form import ACForm
from bankapp.models import Form


# Create your views here.

def homepage(request):
    return render(request, 'index.html')


def Register(request):
    if request.method == 'POST':
        username=request.POST['Username']
        password=request.POST['Password']
        Cpassword=request.POST['Cpassword']
        if  password == Cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username Taken")
                return redirect('/')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
        else:
            messages.info(request,'password not matched')
            return render(request,'Register.html')
        return render(request,'login.html')
    return render(request,'Register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']


        auth_user = auth.authenticate(username=username,password=password)
        if auth_user is not None:
            auth.login(request,auth_user)
            return render(request,'formpage.html')
        else:
            messages.error(request,"Incorrect username or password")
            return render(request,'login.html')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def formpage(request):
    return render(request,"formpage.html")

def form(request):
    if request.method == 'POST':
        Name = request.POST.get('Name',)
        DOB = request.POST.get('DOB')
        Phone = request.POST.get('Phone')
        Age = request.POST.get('Age')
        gender = request.POST.get('gender')
        Email = request.POST.get('Email')
        Address = request.POST.get('Address')
        District = request.POST.get('District')
        Branches = request.POST.get('Branches')
        Account_type = request.POST.get('Account_type')
        Material = request.POST.get('Material')
        form = Form(Name=Name, DOB=DOB, Phone=Phone, Age=Age, gender=gender, Email=Email, Address=Address,
                    District=District, Branches=Branches, Account_type=Account_type, Material=Material)
        form.save()
        form = ACForm(request.POST)
        if form.is_valid():
            return render(request,'success.html')
    else:
        return render(request,'form.html')
    return render(request,"form.html")


def service(request):
    return render(request,"service.html")

def success(request):
     return render(request,'success.html')


