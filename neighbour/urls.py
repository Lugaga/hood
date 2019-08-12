from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search, name='search'),
    url(r'^business$', views.business, name='business'),
    url(r'^profile/(?P<username>\w{0,50})$', views.profile, name='profile'),
    url(r'^edit_profile/(?P<username>\w{0,50})$', views.edit_profile, name='edit_profile'),
    url(r'^post/(\d+)$', views.post, name='post'),
    url(r'^new_post$', views.new_post, name='new_post'),
    url(r'^new_business$', views.new_business, name='new_business')
]