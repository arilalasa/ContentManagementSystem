from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home$','articles.views.auth_login'),
    url(r'^home/$','articles.views.auth_login'),
    url(r'^auth_logout$','articles.views.auth_logout'),
    url(r'^register/$','articles.views.register'),
    url(r'^$','articles.views.home_page'),
    url(r'^CustomForms/$','articles.views.home'),
    url(r'^CustomForms/(?P<article_id>\d+)/$','articles.views.home'),
    url(r'^CustomForms/delete/(?P<article_id>\d+)/$','articles.views.delete'),
    # url(r'^$', 'CustomForms.views.home', name='home'),
    # url(r'^CustomForms/', include('CustomForms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
