from django.urls import path, include
from django.conf.urls import url

from .views import register_view, login_view,UserDetail,postman



urlpatterns = [
    path('register/',register_view),
    path('login/', login_view),
    path('post/',postman),


    # path('home/', home_view),
    url(r'^userget/(?P<id>\d+)/$', UserDetail.as_view()),
    url(r'^userdelite/(?P<id>\d+)/$', UserDetail.as_view()),
    url(r'^userupdate/(?P<id>\d+)/$', UserDetail.as_view()),
    url(r'^auth/', include('social_django.urls')),

    # url(r'^auth/', include('rest_framework_social_oauth2.urls'))
]