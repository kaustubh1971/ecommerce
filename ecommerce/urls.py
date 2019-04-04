from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

# from products.views import (ProductListView,
#                             product_list_view ,
#                             ProductDetailView ,
#                             product_detail_view,
#                             ProductFeaturedListView,
#                             ProductFeaturedDetailView,
#                             ProductDetailSlugView)
from . import views
from carts.views import cart_home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home_page, name='home'),
    url(r'^about/$',views.about_page,name='about'),
    url(r'^contact/$',views.contact_page, name='contact'),
    url(r'^login/$',views.login_page, name='login'),
    url(r'^register/$',views.register_page, name='register'),
    url(r'^bootstrap/$',TemplateView.as_view(template_name='bootstrap/example.html')),
    url(r'^products/',include('products.urls',namespace='products')),
    url(r'^search/',include('search.urls',namespace='search')),
    url(r'^cart/$',cart_home, name='cart'),
    # url(r'^featured/$',ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$',ProductFeaturedDetailView.as_view()),
    # url(r'^products/$',ProductListView.as_view()),
    # url(r'^products-fbv/$',product_list_view),
    # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    # url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    # url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
]

if settings.DEBUG:
    urlpatterns= urlpatterns+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)