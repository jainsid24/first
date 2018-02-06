from django.contrib import admin
from .models import Post
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()
# Register your models here.
admin.site.register(Post)