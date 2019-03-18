from django.conf.urls import url
from meal_deal import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_deal/$',
    views.add_deal,
    name='add_deal'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
    url(r'^deals/(?P<meal_deal_slug>[\w\-]+)/$',
        views.show_meal_deal, name='show_meal_deal'),



] 

