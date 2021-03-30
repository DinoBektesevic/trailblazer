from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gallery import views


urlpatterns = [
    path('', views.render_gallery, name='gallery'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
