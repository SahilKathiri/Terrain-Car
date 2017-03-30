from django.db import models
from django.contrib.auth.models import User

def svg_upload_path_1(instance, filename):
	return 'svg_cars/{0}/1__{1}'.format(instance.user.username, filename)

def svg_upload_path_2(instance, filename):
	return 'svg_cars/{0}/2__{1}'.format(instance.user.username, filename)

def svg_upload_path_3(instance, filename):
	return 'svg_cars/{0}/3__{1}'.format(instance.user.username, filename)

def svg_upload_path_4(instance, filename):
	return 'svg_cars/{0}/4__{1}'.format(instance.user.username, filename)

def svg_upload_path_5(instance, filename):
	return 'svg_cars/{0}/5__{1}'.format(instance.user.username, filename)

class GameUser(models.Model):
	user = models.OneToOneField(User, null=True)

	# CARS
	car_1 = models.FileField(upload_to=svg_upload_path_1, blank=True)
	car_2 = models.FileField(upload_to=svg_upload_path_2, blank=True)
	car_3 = models.FileField(upload_to=svg_upload_path_3, blank=True)
	car_4 = models.FileField(upload_to=svg_upload_path_4, blank=True)
	car_5 = models.FileField(upload_to=svg_upload_path_5, blank=True)

	# High scores
	score_level_1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	score_level_2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	score_level_3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	score_level_4 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	score_level_5 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)


	class Meta:
		permissions = (
			('view_game', "Can view Game"),
		)