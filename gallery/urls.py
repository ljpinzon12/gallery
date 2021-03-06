from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^media/$', views.all_media, name="All media"),
    url(r'^users/$', views.all_users, name="All users"),
    url(r'^categories/$', views.all_categories, name="All categories"),
    url(r'^modify/$', views.modify, name="Modify"),
    url(r'^create/$', views.create, name="Create"),
    url(r'^create_clip/$', views.create_clip, name="Create Clip"),
    url(r'^clip/(?P<clip_id>\d+)/$', views.clip_by_id, name="Clip by id"),
    url(r'^media/(?P<media_id>\d+)/clips/$', views.all_clips_by_media, name="Clip by media"),
    url(r'^user/(?P<user_id>\w+)/$', views.user_by_id, name="User by id"),
    url(r'^media/(?P<categoria_id>\d+)/$', views.media_by_categoria, name="Media by categoria"),
    url(r'^uploads/user/(?P<id_user>\w+)/$', views.simple_upload, name='simple_upload'),
    url(r'^login/$', views.login, name='login'),

]