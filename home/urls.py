from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('cart',views.cart,name='cart'),
    path('course-details/<slug:slug>/',views.coursedetails,name="course-details"),
    path('student_dashboard',views.student_dashboard,name='student_dashboard'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('student_profile',views.student_profile,name='student_profile'),
    path('course',views.course,name='course'),
    path('student_enrolled_courses',views.student_enrolled_courses,name='student_enrolled_courses'),
    path('login',views.loginUser,name="login"),
    path('signup',views.signup ,name="signup"),   
    path('lesson',views.lesson,name="lesson"),
    path('student_settings',views.student_settings,name='student_settings'),
]
