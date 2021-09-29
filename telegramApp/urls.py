
from django.urls import path
from . import views


urlpatterns = [
  
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_user,name='logout'),
    path('home/',views.home,name='home'),
    path('post_message/<str:msg>/',views.post_event_on_telegram,name='post_message'),
    path('checkusername/',views.check_username,name='check_username'),

]
