from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Topics,Rooms,Message
from .forms import RoomForm, RegisterForm,MessageForm,EditUserForm
from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request,topic_room='All'):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topics.objects.all()
    rooms_count = Rooms.objects.all().count()
    messages = Message.objects.all()[0:4]

    if topic_room == "All":
        rooms = Rooms.objects.filter(name__icontains=q)
    else:
        rooms = Rooms.objects.filter(topic__name=topic_room)

    context = {'topics':topics,
               'rooms':rooms,
               'rooms_count':rooms_count,
               'messages':messages
               }



    return render(request,'main_content.html',context)



def room(request,pk):
    form = MessageForm()
    room = Rooms.objects.get(id=pk)
    messages = Message.objects.filter(Room__id=pk).order_by('-created')
    participances = room.participants.all()

    if request.method == 'GET' and request.GET.get('body') != None:
        Message.objects.create(body=request.GET.get('body'),User=request.user,Room=room)
        room.participants.add(request.user)

    context = {'room': room,
               'messages': messages,
               'form': form,
               'participances':participances
               }


    return render (request, 'room.html',context)


@login_required(login_url="/login/")
def create_room(request):
    topics = Topics.objects.all()
    form = RoomForm()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topics.objects.get_or_create(name=topic_name)

        Rooms.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request,'create_room.html',context)


def logout_page(request):
    logout(request)
    return redirect('home')

def login_page(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request,'login.html')

def signup_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    context = {'form': form}
    return render(request,'signup.html',context)


def edit_userPage(request):
    form = EditUserForm(instance=request.user)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = EditUserForm(instance=request.user)

    context = {'form':form}
    return render(request,'edit_user.html',context)


def profile_page(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topics.objects.all()
    rooms_count = Rooms.objects.all().count()
    messages = Message.objects.filter(User=request.user)[0:4]
    rooms = Rooms.objects.filter(host=request.user)

    context = {'topics': topics,
               'rooms_count': rooms_count,
               'messages': messages,
               'rooms': rooms,
               }
    return render(request,'profile.html',context)