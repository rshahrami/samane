from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from jalali_date import datetime2jalali
from django.core.validators import MinValueValidator, MaxValueValidator, validate_comma_separated_integer_list


MALI_TYPE_CHOICES = [
    ('bedehkar', 'بدهکار'),
    ('bestankar', 'بستانکار'),
]


class Topic(models.Model):
    topic = models.CharField(max_length=30, verbose_name="عنوان رشته")
    descriptions = models.CharField(max_length=100, blank=True, null=True, verbose_name="توضیحات رشته")
    class Meta:
        verbose_name =("دسته بندی")
        verbose_name_plural =("دسته بندی")

    def __str__(self) -> str:
        return self.topic
    

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/topic/<filename>
    return "{0}/{1}".format(instance.topic, filename)



class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان') # name of article
    topic = models.ForeignKey(Topic, on_delete=models.RESTRICT, default='', null=True, 
                              blank=True, verbose_name='موضوع') # topic of article
    # topic = models.ManyToManyField(Topic, verbose_name='موضوع')
    descriptions = models.CharField(
        max_length=300, blank=True, null=True, default='', verbose_name='نوضیحات')
    date_report = models.DateTimeField(default=timezone.now, verbose_name='زمان ایجاد گزارش')
    date_upload = models.DateTimeField(auto_now_add=True, editable=True, verbose_name='زمان بارگذاری')
    documents = models.FileField(
        upload_to=user_directory_path, default='', null=True, verbose_name='بارگزاری سند')
    author = models.ForeignKey(User, on_delete= models.RESTRICT, default='', null=True, 
                               blank=True, verbose_name='نویسنده گزارش') # author name of article    
    user = models.CharField(max_length=20, blank=True, null=True, default='', verbose_name='کاربر ')
    slug = models.SlugField(verbose_name='آدرس مقاله')

    class Meta:
        verbose_name =("گزارش")
        verbose_name_plural =("گزارشات")

    def __str__(self) -> str:
        return self.title

    def jalaliDateReport(self):
        return datetime2jalali(self.date_report).strftime('%H:%M ساعت %d-%m-%Y')
    jalaliDateReport.short_description = 'زمان تهیه گزارش'
    jalaliDateReport.admin_order_field = "date_report"

    def jalaliDateUpload(self):
        return datetime2jalali(self.date_upload).strftime('%H:%M ساعت %d-%m-%Y')
    jalaliDateUpload.short_description = 'زمان بارگذاری گزارش'


