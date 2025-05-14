from django.db import models

class Submission(models.Model):
    data = models.JSONField()             
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission #{self.pk}"
