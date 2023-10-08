from django.contrib import admin
from samane.models import Article, Topic
from jalali_date.admin import ModelAdminJalaliMixin
from rangefilter.filters import DateRangeFilterBuilder


admin.site.site_header = "پنل مدیریت"
admin.site.site_title = "پنل"
admin.site.index_title = "پنل"



class ArticleAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'topic', 'user', 'author', 'jalaliDateReport', 'jalaliDateUpload']
    list_per_page = 20
    exclude = ['user']
    ordering = ['date_report']
    search_fields = ['title']
    date_hierarchy = 'date_report'
    prepopulated_fields = {
        "slug": ["title"]
        }
    list_filter = [
        ("date_report", DateRangeFilterBuilder()), 'date_report','title', 'topic', 
        'user', 'author'
        ]
    fieldsets = [
        (
            None, 
            {
                'fields': 
                [
                    'title', ('topic', 'author'), 'slug'
                    ]
                }
            ),
        (
            'زمان', 
            {
                'fields':[
                    'date_report'
                    ]
                }
            ),
    ]

    def save_model(self, request, obj, form, change):
        if not change:    
            obj.user = request.user
        super().save_model(request, obj, form, change)
        


admin.site.register(Topic)
admin.site.register(Article, ArticleAdmin)
