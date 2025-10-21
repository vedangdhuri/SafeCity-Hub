"""crime_analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from crime_analysis import settings
from user import views as userviews
from police import views as policeviews
from higher_officer import views as higher_officerviews
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',userviews.user_index, name="user_index"),
    url(r'^user_login/$',userviews.user_login, name="user_login"),
    url(r'^user_register/$',userviews.user_register, name="user_register"),
    url(r'^email_verification/$',userviews.email_verification, name="email_verification"),
    url(r'^upload_complaints/$',userviews.upload_complaints, name="upload_complaints"),
    url(r'^change_details/$',userviews.change_details, name="change_details"),
    url(r'^change_details1/$',userviews.change_details1, name="change_details1"),


    url(r'^police_login/$',policeviews.police_login, name="police_login"),
    url(r'^police_home/$',policeviews.police_home, name="police_home"),
    url(r'^update_details/$',policeviews.update_details, name="update_details"),
    url(r'^view_complaints/$',policeviews.view_complaints, name="view_complaints"),
    url(r'^update_casestatus/(?P<pk>\d+)/$',policeviews.update_casestatus,name="update_casestatus"),
    url(r'^arrest_criminal/(?P<pk>\d+)/$',policeviews.arrest_criminal,name="arrest_criminal"),
    url(r'^upload_criminals/$',policeviews.upload_criminals,name="upload_criminals"),
    url(r'^crime_analysis/$',policeviews.crime_analysis,name="crime_analysis"),
    url(r'^crime_chart/$',policeviews.crime_chart,name="crime_chart"),


    url(r'^admin_login/$',higher_officerviews.admin_login, name="admin_login"),
    url(r'^admin_home/$',higher_officerviews.admin_home, name="admin_home"),
    url(r'^police_emailverify/$',higher_officerviews.police_emailverify, name="police_emailverify"),
    url(r'^adminview_crime/$',higher_officerviews.adminview_crime, name="adminview_crime"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
