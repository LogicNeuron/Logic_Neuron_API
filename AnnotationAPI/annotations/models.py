from django.db import models

class Annotation(models.Model):
    annotator_name = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    text = models.TextField()
    annotation_text = models.CharField(max_length=100)
    annotation_type = models.CharField(max_length=100)
    start_offset = models.IntegerField()
    end_offset = models.IntegerField()

    def __str__(self):
        return f"{self.annotator_name} - {self.file_name}"
