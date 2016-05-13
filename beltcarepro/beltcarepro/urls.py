"""beltcarepro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from base.views import Dashboard
from base.views import CustomerList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$','base.views.index'),
    url(r'^dashboard/', Dashboard.as_view()),
    url(r'^data_conveyor/','base.views.data_conveyor'),
    url(r'^view_customer/','base.views.view_customer'),
    url(r'^add_customer/','base.views.add_customer'),
    url(r'^data_site/','base.views.data_site'),
    url(r'^view_site/','base.views.view_site'),
    url(r'^add_customer_site/','base.views.add_customer_site'),
    url(r'^detail_conveyor_condition/','base.views.detail_conveyor_condition'),
    url(r'^login/','base.views.login_custom'),
    url(r'^customer/', CustomerList.as_view(), name='data-customer'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

