# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sorl.thumbnail import ImageField
from django.db import models
import uuid
import os

# Create your models here.
def story_upload(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("website", filename)



class Railway(models.Model):
    title			= models.CharField(default="", max_length=255)
    description     = models.CharField(default="", max_length=255)
    category        = models.CharField(max_length=100, blank=True, choices=(('garden','Garden Layouts'),('public','Public Displays'),('archive','Archive')))

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Railways"
        verbose_name = "Railway"

    def __unicode__(self):
        return self.title

class RailwayImage(models.Model):
    railway     	= models.ForeignKey(Railway, blank=True, null=True)
    description     = models.CharField(default="", max_length=255)
    image           = ImageField(upload_to=story_upload, blank=True,null=True)
    position		= models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ## ordering = ['title']
        verbose_name_plural = "RailwayImages"
        verbose_name = "RailwayImage"

    def __unicode__(self):
        return self.railway.title


