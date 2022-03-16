from re import template
from django.shortcuts import render
from django.views import View
from . import models

# Create your views here.

def top(request):
    template_name = 'top/top.html'
    return render(request, template_name)


class musicListView(View):
    """
    楽曲一覧取得
    """
    def get(self, request):
        template_name = 'music/music_list.html'
        
        music_list = models.MusicInfo.objects.all()
        context = {'music_list': music_list}
        
        return render(request, template_name=template_name, context=context)