from django.shortcuts import render
from .models import Music

def music_list(request):
    musics = Music.objects.all()
    return render(request, 'music_list.html', {'musics': musics})
