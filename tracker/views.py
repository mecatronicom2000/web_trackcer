from django.shortcuts import render ,redirect
from .adjusted_forms import *
from django.contrib.auth.models import User
import requests as url_tracker
from bs4 import BeautifulSoup as Clean_html
import datetime as Dt_item
from django.utils import timezone
from django.contrib.auth import login as record_command
from django.contrib.auth.decorators import login_required
import random
from django.core.paginator import *
from hitcount.views import HitCountDetailView




id_count=0
# Create your views here.
def register(links):
    model_f=User_Form()
    if links.method=='POST':
        print("anlizing form validation")
        model_f=User_Form(links.POST)
        if model_f.is_valid():
            print("yes it is....data diliverd to the database")
            
            f_user=model_f.save()
            record_command(links,f_user)
            print("user saved to the database")
            return redirect('home')
        else:
            print("No post action happend")
            model_f=User_Form()
    
    return render(links,'register.html',{'form':model_f})




def the_home(links):
    '''
    get the IPaddress to get increased by one track
    call seation storage in js and get views in web scrabing 
      dddddddddddd
    '''
    print("developers.similarweb CONTENT PAGE:")
    ip = Url_tracker.get('https://api.ipify.org').text
    print("\nZZZZZZZZZZZZZZZZZZZZZ6"*5)
    #webitem=WebSite_owner.objects.get(pk=web_x)
    web_array=WebSite_owner.objects.all()
    date_model=Dt_item.datetime.now()
    tz_model=timezone.now()
    print("Welcom to your HOME")
    return render(links,'menu.html',{'all_websites':web_array,'tz':tz_model,'dm':date_model,'g_ip':ip})
    


@login_required
def add_a_website_to_track(links,un):
    super_user=User.objects.get(pk=un)
    print("post operation applied")
    print("proceeding....")
    #model_f=Web_form(links.POST)
    
    if links.method=='POST':
        logo_=links.POST['logox']
        website_name_=links.POST['name']
        the_url_=links.POST['x_url']
        print("all client's data OBTAIEND...new object created")
        client_obj=WebSite_owner(logo=logo_,website_owner=super_user,website_name=website_name_,the_url=the_url_)
        client_obj.save()
        return redirect("track_code")
    return render(links,"add_a_website.html")


def help(links):
    return render(links,"how_to_use.html")


def track_code_generation(links):
    
    num = random.randint(1,5000000)
    css_in_html='''<style>#counter_area'''+str(num)+'''{'''+'''position: relative;top: 150px;text-align: center;background-color: #005bc4;color: #fff;align-items: center;border-radius: 20px;padding: 30px;font-size: 10px;}</style>'''
    the_js_code=''' <script>
     var model_color=document.getElementById("model_color'''+str(num)+'''");
      document.getElementById('counter_area'''+str(num)+'''').style.backgroundColor=sessionStorage.getItem('bkg_model');
      document.getElementById('count_x'''+str(num)+'''').style.fontSize=sessionStorage.getItem('key_font');
      var vistors=document.getElementById('v_result'''+str(num)+'''');
 
     vistors.style.fontSize=sessionStorage.getItem('key_font');
     console.log("localhost featch results");





      let c_visits;
      if (!sessionStorage.getItem('c_visits')) {
        console.log("c_visits not found....creating a one");
        console.log(sessionStorage.setItem('c_visits',1));
      } else {
        console.log("Permission Disabled");
      }
      c_visits=+sessionStorage.getItem('c_visits');
      const const_c_visits=c_visits+1;
      sessionStorage.setItem('c_visits',const_c_visits);
      console.log("current count item :"+const_c_visits);
      vistors.innerHTML=const_c_visits;
      

      function change_the_bk() {
     document.getElementById('counter_area'''+str(num)+'''').style.backgroundColor=sessionStorage.setItem('bkg_model',model_color.value);
     document.getElementById("count_x'''+str(num)+'''").style.background=sessionStorage.setItem('key_font',model_text.value+"px");
      document.getElementById("v_result'''+str(num)+'''").style.fontSize=sessionStorage.setItem('key_font',model_text.value+"px")
      }
       const get_tz=document.getElementById("get_tz'''+str(num)+'''");
       const date_model=new Date();
       const offset=date_model.getTimezoneOffset();
      const str_date=Intl.DateTimeFormat().resolvedOptions().timeZone;
       get_tz.innerHTML=str_date;

       let router_ip=fetch('https://api.ipify.org?format=json').then(del=>del.json().then(ip_x=>ip_x.ip))
window.sessionStorage.setItem('client_sessionhost',router_ip);


var count=0;
fetch('https://api.ipify.org?format=json').then(del=>del.json()).then(evol=>{

if (router_ip===window.sessionStorage.getItem('client_sessionhost')) {
    count_x.innerHTML=count;
} else {
    count_x.innerHTML=count+1;
}
  console.log(evol.ip);
//count_x.innerHTML=evol.ip;
});






      </script>


      




      '''
    the_js_code2='''<script>
    var model_color=document.getElementById("model_color'''+str(num)+'''");
let count_x=document.getElementById("count_x'''+str(num)+'''");
window.sessionStorage.setItem('client_localhost',fetch('https://api.ipify.org?format=json').then(del=>del.json().then(ip_x=>ip_x.ip)))



  function change_the_bk(color_x) {
    window.sessionStorage.setItem('counter_bkg',color_x)

    counter_area.style.backgroundColor=window.sessionStorage.setItem("bkg_model",document.getElementById("model_color").value);
   document.getElementById("contacts").style.background=model_color.value;
    
  }



var count=0;
fetch('https://api.ipify.org?format=json').then(del=>del.json()).then(evol=>{
    
if (evol.ip) {
    count=count+1;
    count_x.innerHTML=count;
} else if(evol.ip===window.sessionStorage.getItem('client_localhost')) {
    count=count;
}else{console.log("vistors none");}


count_x.innerHTML=count;
});

 </script>'''
    
    h1_style='''font-family: 'Cairo';font-size: 20px;color: #fff;'''
    display_action="""{% with firstname=1  firstname=firstname+1%}
<h1 class='title' style='color:white;'>Hello {{ firstname }}, how are you?</h1>
{% endwith %}"""
    print(num)
    code_into_fotter=mark_safe(f"<div  onchange='change_the_bk();' class='counter_now' id='counter_area{num}' ><lable class='lable' for='model_color{num}'>adjust color:<input type='color' name='model_color{num}' id='model_color{num}' /></lable><lable class='lable' for='model_text'>adjust text:<input type='number' name='model_text' id='model_text' /></lable><h1 style='{h1_style}' id='count_x{num}'>now vistors of my site are <span id='v_result{num}' class='view_1'>0</span> vistor</h1><small style='color: white;font-size: 15px;' id='get_tz{num}' class='view_2' ></small></div>")
    print("the tracker value is ",str(num))
    return render(links,"track_code.html",{'code':css_in_html+"<br>\n<br>\n<br>\n<br>\n<br>"+code_into_fotter+"<br>\n<br>\n<br>\n<br>\n<br>"+the_js_code,},)




def output_page(links):
    page_domain=links.GET.get('pg',1)
    web_array=WebSite_owner.objects.all()
    web_site_pages=Paginator(web_array,10)
    try:
        pg1=web_site_pages.page(page_domain)
    except PageNotAnInteger:
        pg1=web_site_pages.page(1)
    except EmptyPage:
        pg1=web_site_pages.page(web_site_pages.num_pages)


    return render(links,"output_page.html",{'all_websites':pg1})

def web_report(links,web_x):
    webitem=WebSite_owner.objects.get(pk=web_x)
    return render(links,"report.html",{'the_item':webitem})


def staff_report(links,web_x):
    user_own_websites=WebSite_owner.objects.filter(website_owner=web_x)
    return render(links,"owner_of_websites.html",{'owner_w':user_own_websites})




def statistic_generation(links,web_x):
    max=0
    target_webitem=WebSite_owner.objects.get(pk=web_x)
    requsted_page=links.GET.get('page',1)
    
    #statistic_report=Tracking_statistic.objects.create(the_tracked=target_webitem)
    full_statistic_report=Tracking_statistic.objects.filter(the_tracked=web_x)
    pages_per_page=Paginator(full_statistic_report,40)
    try:
     all_pages=pages_per_page.page(requsted_page)
    except PageNotAnInteger :
        all_pages=pages_per_page.page(1)
    except EmptyPage:
        all_pages=pages_per_page.page(pages_per_page.num_pages)
    print("statistic_generation object created for id_"+str(all_pages))
    return render(links,"statistics.html",{'target':target_webitem,'target_res':full_statistic_report,'pages':all_pages})


def E404(links,exception):
    return render(links,'E404.html',{'e':exception})
def E500(links):
    return render(links,'E500.html')