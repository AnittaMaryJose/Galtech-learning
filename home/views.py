from django.shortcuts import render,HttpResponse
from . models import UserProfile
from . models import courses
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . models import Lessons,Video,Reviews
from django.shortcuts import render,get_object_or_404
 

# Create your views here.
def index(request):
    return render(request,'index.html')
def cart(request):
    return render(request,'cart.html')





def coursedetails(request, slug):
    course = get_object_or_404(courses, slug=slug)
    if request.method == 'POST' and 'submit' in request.POST:
        current_user = request.user
        rating = request.POST.get("rating")  
        review_text = request.POST.get("comment")  
        review = Reviews.objects.create(user=current_user,course=course,rating=rating,review_text=review_text)
        print("======================================")
        print(review)
       
    
    # for less in course.lessons_set.all():
    #     print(less.lesson_title)
    #     for video in less.video_set.all():
    #         print(video.video_title)
    return render(request, 'course-details.html', {'course': course})







# def coursedetails(request, slug):
#     course = get_object_or_404(courses, slug=slug)
#     for review in course.reviews_set.all():
#         print(review.course)  
#     for less in course.lessons_set.all():
#         print(less.lesson_title)
#         for video in less.video_set.all():
#             print(video.video_title)
#     return render(request, 'course-details.html', {'course': course})

# def coursedetails(request,slug):
#     course = get_object_or_404(courses, slug=slug)
#     return render(request, 'course-details.html', {'course': course}) 

def student_dashboard(request):
    return render(request, 'dashboard/student-dashboard.html')
def dashboard(request):
    return render(request,'dashboard/student-dashboard.html')
def student_profile(request):
    return render(request,'dashboard/student-profile.html')
def student_settings(request):
    return render(request,'dashboard/student-settings.html')

# def coursedet(request):
#     return render(request,"course-details.html")
def course(request):
    course = courses.objects.all()
    return render(request, 'course.html', {'courses': course})


def student_enrolled_courses(request):
    return render(request,'dashboard/student-enrolled-courses.html')


def loginUser(request):
    if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")           
            print(  username,  password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                login(request, user)
           
                return render(request,"index.html")   
            else:     
                messages.error(request, 'invalid user name or password')      
                return render(request,"login.html")  
       
    else:
        return render(request,"login.html")         

  


# views.py
from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.models import User

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

        ph_number = request.POST.get("ph_number")
        profile_picture = request.FILES.get("profile_picture")

        user_profile = UserProfile.objects.create(user=user, phone_number=ph_number, profile_picture=profile_picture)
        print(user_profile)

    return render(request, "login.html")


def lesson(request):
    lessons = Lessons.objects.all()
    context = {'lessons': lessons}
    return render(request, 'lesson.html', context)



    # videos = Video.objects.select_related('lesson').all()
    # for lesson in lessons:
    #     for video in lesson.video_set.all():
    #         print("Display other video details as needed:", video.video_upload_url)
    
    # return render(request, 'test.html', context)