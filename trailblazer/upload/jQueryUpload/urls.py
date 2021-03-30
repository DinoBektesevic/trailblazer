from django.urls import path

from . import views

urlpatterns = [
    path('', views.BasicUploadView.as_view(), name='upload'),
]
