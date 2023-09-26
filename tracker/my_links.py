from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [


path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'),name="login"),
path('accounts/logout/', auth_views.LogoutView.as_view(),name="logout"),
path('accounts/register/', views.register,name="register"),
path('',views.the_home,name='home'),
path('about_the_site', views.help,name="about"),
path('add_webproject_by_username_<int:un>/', views.add_a_website_to_track,name="input_item"),
path('add_webproject_by_username_/track_code', views.track_code_generation,name="track_code"),
path('output_page/', views.output_page,name="output_page"),
path('add_webproject/details_of_org_<int:web_x>', views.web_report,name="details"),
path('websites_of_user_<int:web_x>', views.staff_report,name="s_report"),
path('websites_of_user_<int:web_x>/all_statis',views.statistic_generation,name="statis")

]