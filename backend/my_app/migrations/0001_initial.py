# Generated by Django 5.1.2 on 2025-04-22 12:08

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='originals/')),
                ('compressed_url', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('D', 'Done')], default='P', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
