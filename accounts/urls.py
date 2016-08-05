from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^cancel_subscription/$', views.cancel_subscription, name='cancel_subscription'),
    url(r'^subscriptions_webhook/$', views.subscriptions_webhook, name= "subscriptions_webhook")
]