import os

from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin, auth
from django.shortcuts import redirect

from basic_pay.views import shop


admin.autodiscover()


urlpatterns = patterns('',
    url(r'', include(shop.urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'basic_pay.views.home'),
    url(r'^products/$', 'basic_pay.views.product_list',
        name='plata_product_list'),
    url(r'^products/(?P<object_id>\d+)/$', 'basic_pay.views.product_detail',
        name='plata_product_detail'),

    url(r'^receipt/(?P<order_id>\d+)/$', 'basic_pay.views.receipt_pdf', name='receipt_pdf'),
    url(r'^reporting/', include('plata.reporting.urls')),

    url(r"^account/", include("account.urls")),
    url(r"^my_orders/$", 'basic_pay.views.my_orders', name='my_orders'),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), 'media/')}),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
