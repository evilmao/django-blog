
'''为登录应用user 定义的URL'''

from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
import django.contrib.auth.views

urlpatterns=[
	#登录页面
	url(r'^login/$', login, {'template_name': 'user/index.html'}, name='login'),
	#定义一个用户注销的页面
	url(r'^logout/$', views.logout_view, name='logout'),
	#url(r'^login/', views.login_site, name='login'),
	#url(r'^login/$', django.contrib.auth.views.login, name='login'),
	url(r'^register/$', views.register, name='register'),
]
