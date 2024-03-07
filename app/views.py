from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User, Group
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
# Create your views here.

url = "mongodb+srv://pro_user:rkwyrUiPnjjBsssg@cluster0.edxis.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url, server_api=ServerApi('1'))

db = client.mpb
db_users = db.users
db_courses = db.courses
db_events = db.events
db_blogs = db.blogs

def timenow():
    return int(str(datetime.datetime.now()).replace(":","").replace("-","").replace(" ","").split('.')[0][:-2])

def convert_event_datetime(date_string, time_string):
    def format_date(date_string):
        mon=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
        date=str(date_string).replace(" – "," ").replace(",","").lower().split(" ")
        if date[2] not in mon:
            date[0]=str(mon.index(date[0])+1)
            date[3]=str(mon.index(date[3])+1)
            if len(date[0])==1:date[0]=int("0"+date[0])
            if len(date[3])==1:date[3]=int("0"+date[3])
        elif date[0] in mon and date[2] in mon:
            date[0]=mon.index(date[0])+1
            date[2]=mon.index(date[2])+1
        if len(str(date[1]))==1:date[1]="0"+str(date[1])
        elif len(str(date[3]))==1:date[3]="0"+str(date[3])
        start_date = int(str(date[-1])+str(date[0])+str(date[1]))
        end_date = int(str(date[-1])+str(date[2])+str(date[3]))
        return start_date, end_date
    
    def format_time(time_string):
        time_string=str(time_string)
        time_string=time_string.split(" - ")
        time_string[0]=time_string[0].split(" ")
        if time_string[0][1]=="pm":
            time_string[0][0]=str(int(time_string[0][0].split(":")[0])+12)+time_string[0][0].split(":")[1]
        else:
            time_string[0][0]=time_string[0][0].split(":")[0]+time_string[0][0].split(":")[1]
        time_string[1]=time_string[1].split(" ")
        if time_string[1][1]=="pm":
            time_string[1][0]=str(int(time_string[1][0].split(":")[0])+12)+time_string[1][0].split(":")[1]
        else:
            time_string[1][0]=time_string[1][0].split(":")[1]+time_string[1][0].split(":")[1]
        
        if len(time_string[0][0])==3:
            time_string[0][0]="0"+time_string[0][0]
        
        start_time=time_string[0][0]
        end_time=time_string[1][0]

        return start_time, end_time    
    
    start_time,end_time=format_time(time_string)
    start_date,end_date=format_date(date_string)
    
    start = int(str(start_date)+str(start_time))
    end = int(str(end_date)+str(end_time))
    
    return start, end


def signup(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='amrish').exists():return redirect ("amrish-home")
        elif request.user.groups.filter(name='buddy').exists():return redirect ("buddy-home")

    elif request.method=="POST":
        username = request.POST['su-username']
        email = request.POST['su-email']
        password = request.POST['su-password']
        if User.objects.filter(username=username).exists():messages.info(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():messages.info(request, 'Email already exists')
        else:
            user = User.objects.create_user(username, email, password)
            user = authenticate(request, username=username, password=password)
            group = Group.objects.all().filter(name="buddy").first()
            user = User.objects.get(username=username)
            user.groups.add(group)
            login(request, user)
            db_users.insert_one({"username":username, "email":email, "role":"buddy", "courses":[], "last_update":timenow(),"password":password})
            return redirect("/buddy")
        return redirect("signup")

    return render(request,'signup.html')

def ajaxsigningin(request):
    print('ajaxsigningin')

def signin(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='amrish').exists():return redirect ("amrish-home")
        elif request.user.groups.filter(name='buddy').exists():return redirect ("buddy-home")


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
        if request.user.groups.filter(name='amrish').exists():return redirect ("amrish-home")
        elif request.user.groups.filter(name='buddy').exists():return redirect ("buddy-home")

    else:return render(request,'home.html')

def home(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='amrish').exists():return redirect ("amrish-home")
        elif request.user.groups.filter(name='buddy').exists():return redirect ("buddy-home")
    for i in db_courses.find():
        print(i["last_update"])
    # print(i["last_update"])
    def get_last_course():
        last_course={}
        t=0
        for i in db_courses.find():
            if t<i["last_update"]:
                t=i["last_update"]
                last_course={"course_title":i["course_title"],"course_image":i["course_image"],"course_rating":i["course_rating"],"course_category":i["course_category"],"course_contains":i["course_contains"],"course_enrolled":i["course_enrolled"],"course_author":i["course_author"],"course_price":i["course_price"],"oid":i["oid"]}
        return last_course
    
    def get_popular_course():
        popular_course={}
        t=0
        for i in db_courses.find():
            if t<int(i["course_enrolled"]):
                t=int(i["course_enrolled"])
                popular_course={"course_title":i["course_title"],"course_image":i["course_image"],"course_rating":i["course_rating"],"course_category":i["course_category"],"course_contains":i["course_contains"],"course_enrolled":i["course_enrolled"],"course_author":i["course_author"],"course_price":i["course_price"],"oid":i["oid"]}
        return popular_course
    # return render(request, 'home.html')
    return render(request, 'home.html',{"last_course":get_last_course(),"popular_course":get_popular_course()})

def courses(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='amrish').exists():return redirect ("amrish-home")
        elif request.user.groups.filter(name='buddy').exists():return redirect ("buddy-home")

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
    if request.user.is_authenticated:
        if request.user.groups.filter(name='amrish').exists():return redirect ("amrish-home")
        elif request.user.groups.filter(name='buddy').exists():return redirect ("buddy-home")

    context={'course':db_courses.find_one({"oid":"designing-a-low-prototype-in-figma-3-months"})}
    return render(request,'courses-page.html',context)

def view_course(request,id):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='amrish').exists():return redirect ("amrish-home")
        elif request.user.groups.filter(name='buddy').exists():return redirect ("buddy-home")

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






def trial(request):
    return render(request, 'trial.html')

def c_data(request):
    c_data=request.POST.get('c_data')
    data=str(c_data).split("<br>")
    content=""
    for i in data:
        i.strip()
        content+='<p class="about-event-box__text">'+i+'</p>'
    price=420
    context={"content":content,"price":"Rs:"+str(price)}
    return JsonResponse(context)