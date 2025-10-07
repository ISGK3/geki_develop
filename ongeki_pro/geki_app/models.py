from django.db import models

# Create your models here.
class sysModelBase(models.Model):
    """
    modelテンプレート
    """
    class Meta:
        abstract = True
    
    id = models.BigAutoField(primary_key=True)
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='作成日時'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        db_index=True,
        verbose_name='更新日時'
    )



class MusicInfo(sysModelBase):
    """
    楽曲情報
    """
    class Meta:
        verbose_name = "楽曲情報"
        verbose_name_plural = verbose_name
        
    poster = models.ImageField(verbose_name='画像URL', upload_to='img', blank=True, null=True)
    genre = models.CharField(verbose_name='ジャンル', max_length=128)
    title = models.CharField(verbose_name='タイトル', max_length=128)
    lv = models.CharField(verbose_name='レベル', max_length=128)
    notes = models.BigIntegerField(verbose_name='ノーツ', blank=True, null=True)
    bell = models.BigIntegerField(verbose_name='ベル', blank=True, null=True)
    const = models.FloatField(verbose_name='譜面定数', blank=True, null=True)
    bpm = models.IntegerField(verbose_name='BPM', blank=True, null=True)
    difficulty = models.CharField(verbose_name='難易度', max_length=128)
    movie_url = models.CharField(verbose_name='動画URL', max_length=128, blank=True,  null=True)

class MusicDetail(sysModelBase):
    """
    楽曲詳細情報
    """
    class Meta:
        verbose_name = "楽曲詳細情報"
        verbose_name_plural = verbose_name
        
    poster = models.ImageField(verbose_name='画像URL', upload_to='img', blank=True, null=True)
    genre = models.CharField(verbose_name='ジャンル', max_length=128)
    title = models.CharField(verbose_name='タイトル', max_length=128)
    artist = models.CharField(verbose_name='アーティスト', max_length=128, blank=True, null=True)
    opponent = models.CharField(verbose_name='対戦相手', max_length=128, blank=True, null=True)
    unlocked = models.CharField(verbose_name='解禁方法', max_length=128, blank=True, null=True)
