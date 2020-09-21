from django.db import models


# Create your models here.
class Tasks(models.Model):
    task_id = models.CharField(max_length=200)
    job_name = models.CharField(max_length=200)
    dna_string = models.TextField(max_length=1000)
    dna_result = models.TextField(max_length=2000)

    def __str__(self):
        return f"{self.task_id} {self.job_name}"
