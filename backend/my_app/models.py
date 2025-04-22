from django.db import models
import uuid

choices=[('P', 'Pending'), ('D', 'Done')]
class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="originals/")
    email = models.EmailField(null=False, blank=False, editable=True)
    status = models.CharField(max_length=20, choices=choices, default='P', editable=False)
    compressed_url=models.EmailField(editable=True, null=False, default='Email@email.com')
