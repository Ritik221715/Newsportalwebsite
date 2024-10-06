


from django.contrib import admin
from .models import *
# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Mobile','Message')
admin.site.register(contactus,contactusAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','category_picture')

admin.site.register(category,categoryAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('slider_picture','slider_title','slider_description')

admin.site.register(slider,sliderAdmin)

class tbl_jobsAdmin(admin.ModelAdmin):
    list_display = ('title','title_link','posted_date')

admin.site.register(tbl_jobs,tbl_jobsAdmin)

class tbl_cityAdmin(admin.ModelAdmin):
    list_display = ('id','city_name','city_picture')

admin.site.register(tbl_city,tbl_cityAdmin)

class tbl_newsAdmin(admin.ModelAdmin):
    list_display = ('id','headline','news_category','news_city','news_description','posted_date','news_picture')

admin.site.register(tbl_news,tbl_newsAdmin)

class video_newsAdmin(admin.ModelAdmin):
    list_display = ('id','news_headline','news_description','video_link','posted_date')
admin.site.register(video_news,video_newsAdmin)
