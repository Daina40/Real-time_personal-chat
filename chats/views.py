from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from chats.models import ChatModel
# Create your views here.

def index(request):
    users = User.objects.exclude(username=request.user.username)

    context = {
        'users' : users
    }

    return render(request, 'index.html', context)

def chatpage(request, username):
    try:
        user_obj = User.objects.get(username=username)
        users = User.objects.exclude(username=request.user.username)
    except User.DoesNotExist:
        return HttpResponse("User does not exist")

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    message_obj = ChatModel.objects.filter(thread_name=thread_name)

    context = {
        'users' : users,
        'user' : user_obj,
        'messages':message_obj
    }

    return render(request, 'main_chat.html', context)