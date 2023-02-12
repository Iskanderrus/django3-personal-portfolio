from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)  # string field with max length of 100
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')  # creates directory to store images of the portfolio
    url = models.URLField(blank=True)  # blank=True for opening the page in the new browser tab

    def __str__(self):
        return self.title

