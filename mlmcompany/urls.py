
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from useraccounts.views import loginview
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')),
    path('user/',include('useraccounts.urls')),

    path('login/',loginview,name='login'),
    path('',TemplateView.as_view(template_name='home.html'),name='home'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
