from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'post.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^new-users/select-role/$', 'post.views.select_role', name='select_role'),
    url(r'^social/logged-in/$', 'post.views.already_registered', name='already_registered'),
    url(r'^posts/', include('post.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^community/$', include('forums.urls')),
    url(r'^articles/comments/', include('django.contrib.comments.urls')),
    url(r'^accounts/', include(
        'registration.backends.simple.urls')),
    url('', include('social.apps.django_app.urls', namespace='social'))
)
