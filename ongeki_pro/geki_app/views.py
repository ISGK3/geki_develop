from re import template
from django.http import Http404
from django.shortcuts import render
from django.views import View
from . import models, library

# Create your views here.

def top(request):
    template_name = 'top/top.html'
    # yahoo天気
    url = 'https://weather.yahoo.co.jp/weather/jp/13/'
    area_code = '4410'
    endpoint = '.html'
    weather_info = library.get_weather(URL=url + area_code + endpoint)
    return render(request, template_name, context=weather_info)


class musicListView(View):
    """
    楽曲一覧取得
    """
    def __init__(self, **kwargs):
        self.template_name = 'music/music_list.html'
        
        # 画面毎に設定する想定
        self.head_meta = {
            'title': 'オンゲキ楽曲一覧',
            'card': 'summary_large_image',
            'image': '',
            'mode': 'image',
            'movie_url': '',
        }
    
    def get(self, request):      
        
        music_list = models.MusicInfo.objects.all()
        context = {'music_list': music_list,
                   'head_meta': self.head_meta,
                   }
        
        return render(request, template_name=self.template_name, context=context)

class musicDetail(View):
    """
    楽曲詳細
    """
    def __init__(self, **kwargs):
        self.template_name = 'music/music_detail.html'
        # 画面毎に設定する想定
        # TODO 後で修正
        self.head_meta = {
            'title': 'オンゲキ楽曲詳細',
            'card': 'summary_large_image',
            'image': '',
            'mode': 'movie',
            'movie_url': '',
        }
        
    def get(self, request,title):
        
        # 楽曲情報取得
        musics =  models.MusicInfo.objects.filter(
            title=title,
            )
        
        # ポスター画像設定
        img = ''
        if musics.count() != 0:
            music = musics.first()
            img = music.poster.url
            self.head_meta['image'] = img
            self.head_meta['movie_url'] = music.movie_url
        
        # 楽曲詳細取得
        musicDetail = models.MusicDetail.objects.filter(
            title=title,
            ).first()
        
        context = {'musics': musics,
                   'head_meta': self.head_meta,
                   'img': img,
                   'music_detail': musicDetail,
                   }
        return render(request, template_name=self.template_name, context=context)