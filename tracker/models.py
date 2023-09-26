from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.html import mark_safe
import requests as Url_tracker
from bs4 import BeautifulSoup as Clean_html
import random
from datetime import datetime
from pytz import timezone
import socket

# Create your models here.
class WebSite_owner(models.Model):
    logo=models.ImageField(upload_to='web_companyX',verbose_name="upload_logo",null=True,blank=True)
    website_owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="display_url_of")
    website_name=models.CharField(verbose_name='your website/project name:',max_length=45)
    the_url=models.CharField(verbose_name="add web site domain",name="the_url",max_length=200)
    posted_in=models.DateTimeField(auto_now_add=True)
    my_views=models.PositiveBigIntegerField(default=0)
    
    def counting_number_of_visits(self):
        '''
        التعويض العام لابد ان يكون بهذه الصيغه 
        <div class='e_counter' id='web_{num}'><p class='subtitle is-3'>number of site_visitors are<span id='{num}'></span> visitor</p></div><scripts>const vistors=document.getElementById('{num}');{the_js_code}</scripts>
        مع الاخذ في الاعتبار ان  متغير the_js_code 
        يوضع محتواه في ملف خارجي
        '''

        '''
        اختبار أدخال بيانات الموقع بمعلومية السيرفر الداخلي
        مع الاخذ في الاعتبار ان السيرفير الداخلي  له مفتاح واحد فقط
        .
        .
        .
        .
        النتيجة:ناجح
h1->id:count_x
span->id:v_result




'class':'view_1'
'class':'view_2'
        '''



#http://makkahegypt.com/
        count_backend=0
        track_a_website=Url_tracker.get("http://makkahegypt.com/")
        randome_src=track_a_website.content
        clean_code=Clean_html(randome_src,"lxml")
        display=clean_code.find_all("div",{'class':'counter_now'})
        display_=clean_code.find_all("small",{'class':'view_2'})
        #count_backend=display
        #view_data=display.contents[0].find_all_next('label')
        if display and display_ :
           self.my_views+=1
           return mark_safe(f"<li style='background-color:#fa0;'>{display }</li>")
        else:
            return mark_safe(f"<li style='background-color:#fa0;'>None---None</li>")



        
    def __str__(self):
        return str(self.the_url)
    def posted_date(self):
        return str(self.posted_in.strftime("%Y-%A-%B"))
    def auto_counter(self):
        '''track_a_website=Url_tracker.get("http://"+self.the_url+"/")
        responce_code=track_a_website.status_code
        print("the responce code\n",responce_code)'''
        host_name=socket.gethostbyname(socket.gethostname())
        public_host_name=Url_tracker.get("https://api.ipify.org").text
        print("your host name is ",public_host_name)
        return mark_safe(f"{public_host_name}-{host_name}")
    def logo_display(self):
        return mark_safe(f"<img src='"+str(self.logo)+"' width='128px' height='128px' />")
    def print_website_owner(self):
        return mark_safe(f"<tr style='padding:0px 30px 0px 30px;'><td>{self.pk}</td><td>{self.website_name}</td><td>{self.posted_date()}</td><td>{self.the_url}</td><td>{self.counting_number_of_visits()}</td>")
    
class Tracking_statistic(models.Model):
    '''
    تتم عملية متابعة الزيارات أوتومتيكيا بمجرد دخول الزائر
    الي الموقع من الصفحة الرئيسية لذا لابد من الدخول  منها
    او من
    '''
    last_track=models.DateTimeField(auto_now_add=True)
    the_tracked=models.ForeignKey(WebSite_owner,on_delete=models.CASCADE,related_name='statistics')
    def get_timeZone_model(self):
            
            return mark_safe(f"<script> var k_{self.pk}= new Date();document.getElementById('time_{self.pk}').innerText=k_{self.pk};</script><p class='subtitle' id='time_{self.pk}'></p>")
    def writing_number_of_visits(self):
        '''
        التعويض العام لابد ان يكون بهذه الصيغه 
        <div class='e_counter' id='web_{num}'><p class='subtitle is-3'>number of site_visitors are<span id='{num}'></span> visitor</p></div><scripts>const vistors=document.getElementById('{num}');{the_js_code}</scripts>
        مع الاخذ في الاعتبار ان  متغير the_js_code 
        يوضع محتواه في ملف خارجي
        '''





        track_a_website=Url_tracker.get("http://127.0.0.1:8000/")
        randome_src=track_a_website.content
        clean_code=Clean_html(randome_src,"lxml")
        display=clean_code.find("div",{'id':'v_result'})
        return mark_safe(f"<p>{display}</p>")
    def __str__(self):
        return str(self.last_track)
    def print_tracking(self):
        return mark_safe(f"<tr><td>{self.pk}</td><td id='date_{self.pk}'></td><td>{self.the_tracked}</td><td>{self.writing_number_of_visits()}</td></tr>")
    


    