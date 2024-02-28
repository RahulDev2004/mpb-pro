from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# Create your views here.

url = "mongodb://localhost:27017"
client = MongoClient(url, server_api=ServerApi('1'))

db = client.myprobuddy
db_user = db.users
db_courses = db.courses


def signup(request):
    if request.user.is_authenticated:
        print("logedin")
        return redirect('home')
    elif request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username,email,password)
        if User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists():messages.info(request, 'Username and Email already exists')
        elif User.objects.filter(username=username).exists():messages.info(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():messages.info(request, 'Email already exists')
        else:
            user = User.objects.create_user(username, email, password)
            db_user.insert_one({"username":username,"email":email,"password":password})
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("home")
        return redirect("signup")
    else:return render(request,'signup.html')

def signin(request):
    if request.user.is_authenticated:return render(request,'index.html')
    elif request.method == 'POST':    
        username = request.POST["username"]
        password = request.POST["password"]
        if '@' in username:username = User.objects.get(email=username.lower()).username
        user = authenticate(request, username=username, password=password)
        if user:login(request, user)
        else:messages.info(request, 'User not found')
        return redirect("signin")
    else:return render(request,'signin.html')

def signout(request):
    if request.user.is_authenticated:logout(request)
    return redirect('signin')

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def members(request):
    return render(request, 'members.html')

def members_page(request):
    return render(request, 'members-page.html')

def freelancers(request):
    return render(request, 'freelancers.html')

def groups(request):
    return render(request, 'groups.html')

def group_profile(request):
    return render(request, 'group-profile.html')

def courses(request):
    courses = {}
    for i in db_courses.find():
        courses[i['oid']] = {"course_category":i['course_category'],
            "course_title":i['course_title'],
            "course_rating":i['course_rating'],
            "course_contains":i['course_contains'],
            "course_enrolled":i['course_enrolled'],
            "course_author":i['course_author'],
            "course_price":i['course_price'],
            "course_image":i['course_image'],
            "course_duration":i['course_duration']
        }
    return render(request, 'courses.html',{'courses':db_courses.find()})

def create_courses(request):
    return render(request, 'courses.html')

def courses_page(request):
    return render(request, 'courses-page.html')

def shop(request):
    return render(request, 'shop.html')

def product(request):
    return render(request, 'product.html')

def blog(request):
    return render(request, 'blog.html')

def blog_page(request):
    return render(request, 'blog-page.html')

def events(request):
    return render(request, 'events.html')

def event(request):
    return render(request, 'event.html')
