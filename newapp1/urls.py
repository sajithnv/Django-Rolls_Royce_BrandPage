from django.conf.urls import url
from newapp1.views import todoadd,view,help1,contact1
urlpatterns=[
        url(r'^todoadd/$',todoadd,name='todoadd'),
        url(r'^view/$',view,name='view'),
        url(r'^help1/$',help1,name='help2'),
        url(r'^$',contact1,name='contact2'),
    ]
