from django.urls import path,include
from blog import views
from django.contrib import admin

app_name = '<blog>'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('about/',views.about,name="about"),
    path('users/',views.users,name="users"),
    path('macro/',views.macro,name="macro"),
    path('earth/',views.earth,name="earth"),
    path('archi/',views.archi,name="archi"),
    path('animals/',views.animals,name="animals"),
    path('travel/',views.travel,name="travel"),
    path('long/',views.long,name="long"),
    path('roads/',views.roads,name="roads"),
    path('experiment/',views.experiment,name="experiment"),





]
