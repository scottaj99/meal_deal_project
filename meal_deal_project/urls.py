"""meal_deal_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from meal_deal import views
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^meal_deal/', include('meal_deal.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',
        include('registration.backends.simple.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')
