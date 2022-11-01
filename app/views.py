from ast import Pass
from atexit import register
import email
from email import message
from tabnanny import check
from turtle import title
from unicodedata import category
from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect,HttpResponse
from random import randint
from .models import Postuser, Registeruser, UserMaster, Query
from django.contrib import auth
# from django.views.decorators.cache import cache_control

# Create your views here.
# Login page rendering
def LoginPage(request):
    return render(request, "app/Login.html")

# check data in database and login
def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = UserMaster.objects.filter(Email = email, Password = password)
        if user:
            message = "Sucessfully Registered"
            request.session['user'] = email;
            # return HttpResponse(request.session['user'])
            return render(request, "app/Index.html", {"msg": message})
        else:
            message = "Email and password should be correct"
            return render(request, "app/Login.html", {"msg": message})
    else:
        message = "Invalid credentials"
        return render(request, "app/Login.html", {"msg": message})


# sigup page rendering
def SignupPage(request):
    return render(request, "app/Signup.html")

def SearchProduct(Request):
    data = Postuser.objects.get('')



# Signup/Insert the data in to database
def Register(request):
    if request.method == 'POST':
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mobile = request.POST['mobile']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(Email = email)

        if user:
            message = "User already exists"
            return render(request, "app/Signup.html", {'msg': message})
        else:
            if password == cpassword:
                otp = randint(100000, 999999)
                new_user = UserMaster.objects.create(Email=email, Mobile=mobile, Password=password, Otp=otp)
                newcand = Registeruser.objects.create(user_id=new_user, Firstname=fname, Lastname=lname)
                return render(request, "app/Otp.html", {"email":email})
    else:
        print("done")

# render OTP page
def OTPPage(request):
    return render(request, "app/Otp.html")

# validation using OTP
def OTPVerify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.filter(Email = email, Otp=otp)

    if user:
        message = "Successfully registered!!! login"
        return render(request, "app/Login.html", {"msg": message})
    else:
        message = "Registered properly"
        return render(request, "app/Signup.html", {"msg": message})

# render create Post
def PostCardPage(request):
    return render(request, "app/post_card_form.html")

# insert product in to database
def ProductPage(request):
    user_data = request.session['user']
    # return HttpResponseRedirect(user_data)
    user_detail = UserMaster.objects.get(Email=user_data)
    user = user_detail.id  # type: ignore
    if request.method == "POST":
        category = request.POST['category']
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['images']
        newpost = Postuser.objects.create(user_id_id=user, category=category, title=title, description=description, price=price, img=image)
        return redirect('showdata')
    else:
        return redirect('login')
    

# render contactPage
def ContactPage(request):
    return render(request, "app/contact_us.html")

# render showpage
def ProductCard(request):
    return render(request, "app/showpost.html")

#show data in the show page
def ShowProductData(request):
    show = Postuser.objects.all()
    # return HttpResponse(show)
    return render(request,"app/showpost.html",{'key1':show}) 

# render searchpage
# def SearchPage(request):
#     return render(request, "app/Search_bar.html")

# logout session
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect('login')
    else:
        return redirect('already')
# after logout if you see logout btn and click on it then this will be shown
def AlreadyLogout(request):
    return render(request, "app/Alreadylogout.html")

# render Query Page
def QueryPage(request):
    return render(request, "app/Query.html")

# query insert in to database
def Queries(request):
    user_data = request.session['user']
    user_detail = UserMaster.objects.get(Email=user_data)
    user = user_detail.id  # type: ignore

    if request.method == "POST":
        query_title = request.POST['query_title']
        query = request.POST['query']

        send = Query.objects.create(user_id_id=user, q_title=query_title, query=query)

        message = "Query has been sent"
        return render(request, "app/Query.html", {"query":message})
    else:
        return HttpResponse("database has issue")

# index page poster will be shown when website opens
def Index(request):
    return render(request, "app/Index.html")

# Render DetailView
def DetailView(request, pk):
    Data = get_object_or_404(Postuser, pk=pk)
    return render(request, "app/Detail_view.html", {"data": Data})

# get Detail page
def Detailprocess(request, pk):
    pass



























        

    
    




        





