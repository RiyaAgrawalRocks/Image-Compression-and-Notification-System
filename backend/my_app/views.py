from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from backend import settings
from .tasks import *
from .models import *
from .serializers import *

@api_view(['POST'])
@permission_classes([AllowAny]) 
@parser_classes([MultiPartParser, FormParser])
def upload(request):
    serializer=JobSerializer(data=request.data)
    if serializer.is_valid():
        job=serializer.save()
        compress.delay(str(job.id))
        return Response({"job id":{job.id}, "status":{job.status}}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def status_check(request, job_id):
    try:
        job=Job.objects.get(id=job_id)
        return Response({"job id": str(job_id), "status": job.status})
    except Job.DoesNotExist:
        return Response({"error":"Job Not Found"}, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])  
def job_complete_hook(request):
    data = request.data
    job_id = data.get('job_id')
    status = data.get('status')
    compressed_url = data.get('compressed_url')
    if not job_id or not status:
        return Response({"error": "Missing job_id or status"}, status=400)
    try:
        job = Job.objects.get(job_id=job_id)
    except Job.DoesNotExist:
        return Response({"error": "Job not found"}, status=404)
    
    job.status = status
    if compressed_url:
        job.compressed_url = compressed_url
    job.save()

    send_email.delay(
        subject='Your image has been compressed!',
        message=f'Hi, your image is ready at: {compressed_url}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[job.email],
        fail_silently=True
    )

    return Response({"message": "Job status updated successfully"}, status=200)