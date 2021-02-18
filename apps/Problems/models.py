from django.db import models
from django.urls import reverse
from django.conf import settings

from datetime import datetime

from taggit.managers import TaggableManager



class Problem(models.Model):
    title = models.CharField(max_length=100, blank=False)

    statement = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('problems:problemDetail',args=[self.id])

    def get_latex(self):
        return "\subsection{" + self.title+ "} \n" + self.statement