from django.db import models
from accounts.models import MedicalWorker

# Create your models here.


class Notice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        MedicalWorker, on_delete=models.SET_NULL, null=True, blank=True
    )
    read_by = models.ManyToManyField(MedicalWorker, related_name="read_by", blank=True)

    def __str__(self):
        return self.title
