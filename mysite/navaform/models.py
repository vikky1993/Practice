from django.db import models

# Create your models here.

class Nava(models.Model):
	name	  = models.CharField(max_length=30)
	email	  = models.EmailField()
	subject   = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email
