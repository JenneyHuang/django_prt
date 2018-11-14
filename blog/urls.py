from django.conf.urls import url,include
import blog.views

urlpatterns = [
    url(r'^$',blog.views.archive),
    url(r'^create/', blog.views.create_blogpost),
    url(r'^table/',blog.views.table),
]