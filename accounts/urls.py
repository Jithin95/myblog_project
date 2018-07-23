from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.home, name = "home"),
    url(r'login/', views.login, name = "login"),
    url(r'logindata/', views.logindata, name = "logindata"),
    url(r'register/', views.login, name = "register"),
]
