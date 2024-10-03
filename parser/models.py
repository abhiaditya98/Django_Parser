
from django.db import models

class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/',max_length=256)  # Adjust the upload directory as needed
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Candidate(models.Model):
    Name = models.CharField(max_length=250,null=True)
    PhoneNumber = models.CharField(max_length=20,null=True)
    Email = models.EmailField(null=True)
    Experience = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.Name} - {self.Email}"
