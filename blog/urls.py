from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.post_list, name='home'),
    url(r'^blog/top$', views.post_list_top,name='top'),
    url(r'^blog/shortest', views.post_list_shortest, name='shortest'),
    url(r'^blog/newest', views.post_list_newest, name='newest'),
    url(r'^blog/oldest', views.post_list_oldest, name='oldest'),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail, name='view_post'),
    url(r'^blog/result', views.search, name='search'),
    url(r'^blog/tag/(\w+)/$', views.gettags, name='gettags'),
    url(r'^blog/post/new/$', views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', views.edit_post,name='edit_post'),
]