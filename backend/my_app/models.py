from django.db import models
import uuid

choices=[('P', 'Pending'), ('D', 'Done')]
class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="originals/")
    compressed_url = models.URLField(blank=True, null=True)
    email = models.EmailField(null=False, blank=False, editable=True)
    status = models.CharField(max_length=20, choices=choices, default='P')
    created_at = models.DateTimeField(auto_now_add=True)

