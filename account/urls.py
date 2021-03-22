from django.conf.urls import url
from django.contrib.auth import views as auth_views
from account.views import sign_in

urlpatterns=[
	url(r'^sign_up/$',sign_in,name='signin'),
	url(r'^login/$',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
	url(r'^logout/$',auth_views.LogoutView.as_view(next_page='home1'),name='logout'),
]