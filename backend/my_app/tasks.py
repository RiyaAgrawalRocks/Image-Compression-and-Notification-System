from .models import *
from celery import shared_task
import os
from django.conf import settings
from PIL import Image

@shared_task
def compress(job_id):
    try:
        job=Job.objects.get(id=job_id)
        input_path=job.image.path

        compressed_dir=os.path.join(settings.MEDIA_ROOT, 'compressed')
        os.makedirs(compressed_dir, exist_ok=True)

        filename=os.path.basename(input_path)
        output_path=os.path.join(compressed_dir, filename)

        with Image.open(input_path) as img:
            img.save(output_path, optimize=True, quality=50)

        job.compressed_image=f'compressed/{filename}'
        job.status='D'
        job.save()
    except Exception as e:
        print(f"Compression failed for job {job_id}: {e}")

@shared_task
def store(compressed_img):
    return

@shared_task
def post_request(job):
    return

