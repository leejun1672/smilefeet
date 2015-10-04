from django.db import models

class ImageModel(models.Model):
    imgfile = models.FileField(upload_to='upload')
    def __str__(self):
        return self.imgfile.name
