from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import telegram
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login, logout
from django.contrib import messages
from .models import MsgCount
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    if request.method == 'POST':
        data=request.POST
        username=data['username']
        password=data['password']
        cpassword=data['cpassword']
        if password!=cpassword:
            messages.error(request,"Password Not Matched") 
            return redirect('signup')
        user=User.objects.create_user(username=username,password=password)
        user.save()
        messages.success(request,"Registration Success") 
        return redirect('login')
        print(username,password)
    return render(request,'signup.html')    

def login(request):
    if request.method=='POST':
        data=request.POST
        username=data['username']
        password=data['password']
       
        print(password)
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Authentication Failed") 
            return redirect('login')    
    return render(request,'login.html')

@login_required(login_url='/')
def home(request):
    msg_count=MsgCount.objects.all()
    print(msg_count)
    context={
        'user_count':msg_count
    }
    return render(request,'home.html',context)


def post_event_on_telegram(request,msg):
    telegram_settings = settings.TELEGRAM
    bot = telegram.Bot(token=telegram_settings['bot_token'])
    bot.send_message(chat_id="-1001452900898",
        text=msg, parse_mode=telegram.ParseMode.HTML)
    if MsgCount.objects.filter(user=request.user).exists():
        msgcount=MsgCount.objects.get(user=request.user)
        if msg=='stupid':
            msgcount.stupid+=1
        elif msg=='fat':
            msgcount.fat+=1    
        else:
            msgcount.dump+=1   
        msgcount.save()    
    else:
        if msg=='stupid':
            msgcount=MsgCount(user=request.user,stupid=1)
        elif msg=='fat':
            msgcount=MsgCount(user=request.user,stupid=1)  
        else:
            msgcount=MsgCount(user=request.user,stupid=1) 
        msgcount.save()    

    messages.success(request,msg+" Send Successfully...")       
    return redirect('home') 







def check_username(request):
    if request.method == "GET":
        username=request.GET['username']
        
        if User.objects.filter(username=username).exists():
            return HttpResponse(" not available")
        else:
            return HttpResponse("available")  



def logout_user(request):
    logout(request)
    return redirect('/')

