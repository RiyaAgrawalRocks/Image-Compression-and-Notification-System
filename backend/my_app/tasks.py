from .models import *
from celery import shared_task
import os, requests
from django.conf import settings
from PIL import Image

@shared_task
def compress(job_id):
    print(f"Compress task started for job_id: {job_id}")
    try:
        job=Job.objects.get(id=job_id)
        input_path=job.image.path

        compressed_dir=os.path.join(settings.MEDIA_ROOT, 'compressed')
        print(f"Trying to create: {compressed_dir}")
        os.makedirs(compressed_dir, exist_ok=True)
        print("Directory created.")

        filename=os.path.basename(input_path)
        output_path=os.path.join(compressed_dir, filename)

        with Image.open(input_path) as img:
            img.save(output_path, optimize=True, quality=50)
        print(f"Compressed url is here: {job.compressed_url}")
        requests.post('http://127.0.0.1:8000/internal/hooks/job-complete', json={'job_id': job_id, 'compressed_url':f'compressed/{filename}'})
        return job.id
    except Exception as e:
        print(f"Compression failed for job {job_id}: {e}")
        return f"Error: {e}"



@shared_task
def store(compressed_img):
    return

@shared_task
def post_request(job):
    return

@shared_task
def send_email(job):
    return


