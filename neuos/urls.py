"""neuos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main.views import *
from main.api import *
from main.oauth import *
import django_cas_ng

apipatterns = [
    # student api
    url(r'^updatename', update_name),
    url(r'^updaterepo', update_repo),
    url(r'getenv', get_environment),
    url(r'^check_one', check_request),
    # teacher api
    url(r'^addissue', add_issue),
    url(r'^(switchissued)', switch),
    url(r'^(switchallowsubmit)', switch),
    url(r'^uploadfile', upload_file),
    url(r'^delstudents', del_students),
    url(r'^addstudent', add_student),
    url(r'^updatedeadline', update_deadline),
    url(r'^check_all', check_request_all),
    # check api
    url(r'^getcheck', get_check),
    url(r'^checkback', check_back)
]

urlpatterns = [
    url(r'^$', index),
    url(r'^home/$', home),
    url(r'^home/mywork/(\d+)?', mywork),
    url(r'^home/myinfo', myinfo),
    url(r'^teacher/$', teacher),
    url(r'^teacher/students', students),
    url(r'^teacher/issues/(\d+)?', issues),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(apipatterns)),

    url(r'^accounts/login$', django_cas_ng.views.login, name='cas_ng_login'),
    url(r'^accounts/logout$', logout, name='cas_ng_logout'),

    url(r'^oauth/login/?$', github_login),
    url(r'^oauth/callback/?$', github_callback),
]
