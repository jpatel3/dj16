from django.conf.urls import patterns, url

from post import views

'''
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<post_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<post_id>\d+)/comment/$', views.comment, name='comment'),
'''
urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<post_id>\d+)/comment/$', views.comment, name='comment'),
)