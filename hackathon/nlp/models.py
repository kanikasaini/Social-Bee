from django.db import models
from django import forms

class Profile(models.Model):
	name = models.CharField(max_length = 50)
	picture = models.ImageField(upload_to = 'pictures')

	class Meta:
		db_table = "profile"