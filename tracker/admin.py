from django.contrib import admin
from .models import*

# Register your models here.

# designer and developer
#برنت تاميني


class Manage_WebSite_owner(admin.ModelAdmin):
     list_display=['pk','website_owner','logo_display','website_name','the_url','counting_number_of_visits']
  

     
class Manage_Tracking_statistic(admin.ModelAdmin):
     list_display=['last_track','writing_number_of_visits']
  
admin.site.register(WebSite_owner,Manage_WebSite_owner)
admin.site.register(Tracking_statistic,Manage_Tracking_statistic)