from django.urls import path, re_path
from .views import index,search,docs,intro,get_pending,get_done,get_all,load_more
from .utils import service_worker,manifest,offline,RobotsTxtView




urlpatterns=[
    path('',index,name='home'),
    path('search/',search,name='search'),
    path('docs/',docs,name='docs'),
    path('get_pending/',get_pending,name='pending'),
    path('done_get/',get_done,name='get_done'),
    path('get_all',get_all,name='get_all'),
    path('more/',load_more,name='more')

]














urlpatterns+=[
    re_path(r'^serviceworker\.js$', service_worker, name='sw'),
    re_path(r'^manifest\.json$', manifest, name='manifest'),
    path('offline/',offline,name='offline'),
    re_path(r'^robots\.txt$', RobotsTxtView.as_view()),
]