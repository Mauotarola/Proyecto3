from django.conf.urls import include, url
from .import views 
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^desayuno', views.desayuno, name='desayuno'),
    url(r'^almuerzo', views.almuerzo, name='almuerzo'),
    url(r'^postre', views.postre, name='postre'),
    url(r'^cena', views.cena, name='cena'),
    url(r'^reposteria', views.reposteria, name='reposteria'),
    url(r'^banqueteria', views.banqueteria, name='banqueteria'),
    url(r'^registro/', views.registro, name="registro"),
    path('oauth/', include('social_django.urls', namespace='social'))
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)