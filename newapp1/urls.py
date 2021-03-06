from django.conf.urls import url
from newapp1.views import todoadd,view,help1,contact1,todoedit,newedit,tododelete,delete
urlpatterns=[
        url(r'^todoadd/$',todoadd,name='todoadd'),
        url(r'^view/$',view,name='view'),
        url(r'^help1/$',help1,name='help2'),
        url(r'^contact/$',contact1,name='contact2'),
        url(r'^edit_titles/$',newedit,name='Edit1'),
        url(r'^edit/(?P<pk>\d+)$',todoedit,name='todoedit1'),
        url(r'^delete_titles/$',delete,name='delete1'),
        url(r'^delete/(?P<pk>\d+)$',tododelete,name='tododelete1'),
        
    ]
