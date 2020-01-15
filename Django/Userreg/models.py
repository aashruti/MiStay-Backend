from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User
'''from tinymce.models import HTMLField'''
# Create your models here.
class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	def __str__(self):
	  return self.user.username
class Event(models.Model):
    name = models.CharField(max_length=50)
    venue = models.CharField(max_length=200)
    date = models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')
    time = models.TimeField(help_text='Please use the following format: <em>HH:MM:SS<em>')
    category = models.CharField(max_length=50)
    num_of_attendees = models.PositiveIntegerField(default=0, blank=True)
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attending', blank=True)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'
        ordering = ['date', 'time']

    def get_absolute_url(self):
        return reverse('Userreg:event-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def get_number_of_attendeess(self):
        return self.attendees.all().count()

    def get_number_of_attendees(self):
        return self.num_of_attendees