from django.contrib import admin
from django.urls import path
from produtos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('produtos/', views.produtos_view, name='produtos'),
    path('contato/', views.contato, name='contato'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
