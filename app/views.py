from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User, Group
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# Create your views here.

url = "mongodb+srv://pro_user:rkwyrUiPnjjBsssg@cluster0.edxis.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url, server_api=ServerApi('1'))

db = client.mpb
db_user = db.users
db_courses = db.courses
db_blogs = db.blogs

def auth_user(request, redirect_route):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='amrish').exists():return redirect ("amrish-"+redirect_route)
        elif request.user.groups.filter(name='buddy').exists():return redirect ("buddy-"+redirect_route)
    else: return redirect(redirect_route)


def signup(request):
    if request.user.is_authenticated:
        auth_user(request, "home")

    elif request.method=="POST":
        username = request.POST['su-username']
        email = request.POST['su-email']
        password = request.POST['su-password']
        if User.objects.filter(username=username).exists():messages.info(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():messages.info(request, 'Email already exists')
        else:
            user = User.objects.create_user(username, email, password)
            user = db_user.insert_one({"username":username, "email":email, "role":"buddy", "password":password})
            user = authenticate(request, username=username, password=password)
            group = Group.objects.all().filter(name="buddy").first()
            user = User.objects.get(username=username)
            user.groups.add(group)
            login(request, user)
            return redirect("/buddy")
        return redirect("signup")
    
    return render(request,'signup.html')

def ajaxsigningin(request):
    print('ajaxsigningin')

def signin(request):
    if request.user.is_authenticated:
        auth_user(request, "home")   
        
    elif request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        print(username,password)
        if '@' in username:username = User.objects.get(email=username.lower()).username
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user:
                print(username,"Signed In")
                login(request, user)
                if username=="amrish":return redirect("amrish-home")
                return redirect("home")
            else:
                messages.info(request, 'Wrong Username or Email or Password')
        else:
            print("user not found")
            messages.info(request, 'User not Found')
        return redirect("signin")
    else:return render(request,'signin.html')

def signout(request):
    if request.user.is_authenticated:logout(request)
    return redirect('/home')

def index(request):
    if request.user.is_authenticated:
        auth_user(request, "home")
    else:return render(request,'home.html')

def home(request):
    if request.user.is_authenticated:
        auth_user(request, "home")   

    return render(request, 'home.html')

def courses(request):
    if request.user.is_authenticated:auth_user(request, "courses")

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

def course_page(request):
    if request.user.is_authenticated:auth_user(request, "view-course")
    context={'course':db_courses.find_one({"oid":"designing-a-low-prototype-in-figma-3-months"})}
    return render(request,'courses-page.html',context)

def view_course(request,id):
    context={'course':db_courses.find_one({"oid":id})}
    return render(request,'courses-page.html',context)

def blogs(request):
    return render(request, 'blogs.html')

def blog_page(request):
    # blog={'blog':db_courses.find_one({"oid":id})}
    return render(request, 'blogs-page.html')

def blogs_create(request):
    if request.method=="POST":
        title = request.POST['title']
        content = request.POST['content']
        db_blogs.insert_one({"title":title,"content":content})
        return redirect('blogs')
    else:
        return render(request, 'amrish/blogs-create.html')

def events(request):
    return render(request, 'events.html')

def event_page(request):
    return render(request, 'event.html')
