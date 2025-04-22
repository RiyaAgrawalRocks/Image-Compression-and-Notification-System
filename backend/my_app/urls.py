from .views import *
from django.urls import path, include

urlpatterns = [
path('upload', upload),
path('compressed_img', show_compressed),
]