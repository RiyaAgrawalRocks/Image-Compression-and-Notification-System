from .views import *
from django.urls import path

urlpatterns = [
path('upload', upload),
path('status/<job_id>', status_check),
path('internal/hooks/job-complete', job_complete_hook)
]