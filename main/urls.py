from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^register$', views.register, name='register'),
    url(r'^add', views.add),
    url(r'^checkUsr', views.check_usr, name='check'),
    url(r'^checkMail', views.check_mail, name='e_check'),
    url(r'^logOut', views.log_out, name='logOut'),
]
