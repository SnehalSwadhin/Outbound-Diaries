from django.shortcuts import render
from .models import Diary

# Create your views here.


def index(request):
    diaries = Diary.objects.all()
    context ={'diaries': diaries}
    return render(request, 'index.html', context)


def discuss(request, id=None):
    if id:
        item = Diary.objects.get(id=id)
        context = {'diary': item}
        return render(request, 'discussion.html', context)
    else:
        index(request)
