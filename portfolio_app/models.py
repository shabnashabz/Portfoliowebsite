from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    technologies = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)  # Demo or GitHub link
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    



