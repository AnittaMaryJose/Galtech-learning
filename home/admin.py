from django.contrib import admin
from . models import UserProfile
from . models import courses
from . models import Lessons
from . models import Video
from . models import Reviews
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(courses)
admin.site.register(Lessons)
admin.site.register(Video)
admin.site.register(Reviews)