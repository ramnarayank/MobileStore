from django.conf.urls import url

from . import views

app_name='mobiles'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<device_id>[0-9]+)/$',views.detail,name='details'),


    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'^login_user/$',views.login_user,name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^deviceadd/$',views.DeviceCreate.as_view(),name='deviceadd'),
    url(r'(?P<pk>[0-9]+)/deviceupdate/$',views.DeviceUpdate.as_view(),name='deviceupdate'),
    url(r'(?P<pk>[0-9]+)/devicedelete/$',views.DeviceDelete.as_view(),name='devicedelete'),

]

