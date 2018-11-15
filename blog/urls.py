from django.conf.urls import url,include
import blog.views

urlpatterns = [
    url(r'^$',blog.views.archive,name='blogpost'),
    url(r'^post/(?P<pk>[0-9]+)/$', blog.views.post_detail, name='post_detail'),
    url(r'^post/new/$', blog.views.post_new, name='post_new'),

    url(r'^post/(?P<pk>[0-9]+)/edit/$', blog.views.post_edit, name='post_edit'),
    url(r'^create/', blog.views.create_blogpost),
    #url(r'^table/',blog.views.table),
]