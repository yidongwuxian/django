from django.db import models

# Create your models here.
class User(models.Model):
	username  = models.CharField(max_length = 30)
	uploadImg = models.FileField(upload_to = './upload/')

	def __unicode__(self):
		return self.username