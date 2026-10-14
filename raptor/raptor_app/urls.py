from django.contrib import admin
from django.urls import path
from raptor_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("about_us",aboutus),
    path("contact_us",contactus)
]
