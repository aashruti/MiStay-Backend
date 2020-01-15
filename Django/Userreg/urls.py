from django.conf.urls import url
from Userreg import views
# SET THE NAMESPACE!
app_name = 'Userreg'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^Cevent/$',views.Cevent,name='Cevent'),
    url('',views.EventList.as_view(),name='Eevent'),
    url('', views.EventDelete.as_view(), name='Devent'),
    url('', views.EventDetail.as_view(), name='event-detail'),
    url('', views.attend_event, name='attend_event'),
    url('', views.not_attend_event, name='not_attend_event'),
]