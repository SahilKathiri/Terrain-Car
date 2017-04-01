from django.db import models
from django.contrib.auth.models import User
from s3direct.fields import S3DirectField

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
	car_1 = S3DirectField(dest='svg_cars', blank=True)
	car_2 = S3DirectField(dest='svg_cars', blank=True)
	car_3 = S3DirectField(dest='svg_cars', blank=True)
	car_4 = S3DirectField(dest='svg_cars', blank=True)
	car_5 = S3DirectField(dest='svg_cars', blank=True)

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