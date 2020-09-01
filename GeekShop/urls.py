from django.conf.urls.static import static
from django.urls import path, include

from GeekShop import settings
from mainapp import views

urlpatterns = [
    path('', views.main, name='main'),
    path('catalog/', include('mainapp.urls', namespace='catalog')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('', include('social_django.urls', namespace='social')),
    path('contacts/', views.contacts, name='contacts'),
    path('games/', views.games, name='games'),
    path('catalog/product_1', views.product_1, name='product_1'),
    path('catalog/product_2', views.product_2, name='product_2'),
    path('catalog/product_3', views.product_3, name='product_3'),
    path('admin/', include('adminapp.urls', namespace='admin')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
