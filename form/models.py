from django.db import models
#from phone_field import PhoneField
# Create your models here.
class Form(models.Model):
	name = models.CharField(max_length=100)
	url = models.URLField()
	phone_number = models.IntegerField()

	class Meta:
		verbose_name_plural="Forms"
		unique_together = ('name', 'url', 'phone_number')

	def __str__(self):
		return self.name