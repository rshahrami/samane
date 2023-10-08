from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.validators import MinValueValidator, MaxValueValidator, validate_comma_separated_integer_list



MALI_TYPE_CHOICES = [
    ('bedehkar', 'بدهکار'),
    ('bestankar', 'بستانکار'),
]


def tomorrowDate():
    return timezone.now() + timedelta(days=1)


class Enteghad(models.Model):
    user = models.CharField(max_length=20, default='', verbose_name='کاربر')
    title = models.CharField(max_length=50, verbose_name='عنوان انتقاد')
    descriptions_user = models.TextField(
        default='', null=True, blank=True, verbose_name='توضیحات کاربر')
    descriptions_admin = models.TextField(
        default='', null=True, blank=True, verbose_name='نوضیحات مدیریت')
    
    class Meta:
        verbose_name =("انتقاد و پیشنهاد")
        verbose_name_plural =("انتقاد و پیشنهادها")
    
    def __str__(self) -> str:
        return self.title
    

class Morkhasi(models.Model):
    user = models.CharField(max_length=20, default='', verbose_name='کاربر')
    descriptions_user = models.CharField(
        max_length=500, default='', null=True, blank=True, verbose_name='توضیحات کاربر')
    descriptions_admin = models.CharField(
        max_length=500, default='', null=True, blank=True, verbose_name='نوضیحات مدیریت')
    start_date = models.DateField(default=tomorrowDate, verbose_name='تاریخ شروع مرخصی')
    end_date = models.DateField(default=tomorrowDate, verbose_name='تاریخ پایان مرخصی')
    active = models.BooleanField(default=False, verbose_name='تایید مرخصی')

    class Meta:
        verbose_name =("مرخصی")
        verbose_name_plural =("درخواست مرخصی")


class Mali(models.Model):
    user = models.CharField(max_length=20, default='', verbose_name='کاربر')
    descriptions_user = models.TextField(
        default='', null=True, blank=True, verbose_name='توضیحات کاربر')
    descriptions_admin = models.TextField(
        default='', null=True, blank=True, verbose_name='نوضیحات مدیریت')
    etebar = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100000000), 
        validate_comma_separated_integer_list], 
        verbose_name='میزان درخواست اعتبار (تومان)')
    type = models.CharField(
        max_length=200, choices=MALI_TYPE_CHOICES, verbose_name='نوع درخواست')
    taeed_activity = models.BooleanField(default=False, verbose_name='وضعیت تایید')
    tasvie_activity = models.BooleanField(default=False, verbose_name='وضعیت تسویه')

    class Meta:
        verbose_name =("اعتبار")
        verbose_name_plural =("اعتبار")