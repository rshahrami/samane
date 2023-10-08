from django.contrib import admin
from personal.models import Enteghad, Morkhasi, Mali
from jalali_date.admin import ModelAdminJalaliMixin


admin.site.site_header = "پنل مدیریت"
admin.site.site_title = "پنل"
admin.site.index_title = "پنل"


class MorkhasiAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('user',)
    exclude = ('user',)
    ordering = ['user', 'active']

    def save_model(self, request, obj, form, change):
        if not change:    
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user) 
  
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ["user", "descriptions_user"]
        return ["active","descriptions_admin"]
    


class EnteghadAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title',)
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not change:    
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user) 

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ["title", "descriptions_user"]
        return ["descriptions_admin"]


class MaliAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('user', 'etebar', 'type', 'taeed_activity', 'tasvie_activity')
    exclude = ['user']

    def save_model(self, request, obj, form, change):
        if not change:    
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user) 
  
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ["descriptions_user"]
        return ["descriptions_admin", "taeed_activity", "tasvie_activity"]


admin.site.register(Morkhasi, MorkhasiAdmin)
admin.site.register(Enteghad, EnteghadAdmin)
admin.site.register(Mali, MaliAdmin)

