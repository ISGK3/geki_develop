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
        
    poseter_url = models.TextField(verbose_name='画像URL', blank=True, null=True)
    genre = models.CharField(verbose_name='ジャンル', max_length=128)
    title = models.CharField(verbose_name='タイトル', max_length=128)
    lv = models.CharField(verbose_name='レベル', max_length=128)
    notes = models.BigIntegerField(verbose_name='ノーツ', blank=True, null=True)
    bell = models.BigIntegerField(verbose_name='ベル', blank=True, null=True)
    const = models.FloatField(verbose_name='譜面定数', blank=True, null=True)
    bpm = models.IntegerField(verbose_name='BPM', blank=True, null=True)
    difficulty = models.CharField(verbose_name='難易度', max_length=128)
    
    