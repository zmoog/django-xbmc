# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#import xadmin
#xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
#from xadmin.plugins import xversion
#xversion.register_models()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xbmc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^xadmin/', include(xadmin.site.urls)),
    # url(r'^admin_tools/', include('admin_tools.urls')),
    # url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^showcase/', include('showcase.urls', namespace='showcase')),
    url(r'^api/', include('api.urls')),
)
