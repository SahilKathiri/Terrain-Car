from hashlib import sha1
import base64
import hashlib
import hmac
import logging
import os
import time
import urllib
import urllib.parse

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .forms import LoginForm, UploadCarsForm, ScoreForm

from .models import GameUser


@login_required()
@permission_required('game.view_game')
def index(request):
	context_dict = {}
	instance = GameUser.objects.get(user__username=request.user.username)
	if request.method == 'POST':
		form = UploadCarsForm(request.POST, request.FILES, instance=instance)

		if form.is_valid():
			instance.car_1 = form.cleaned_data['car_1']
			instance.car_2 = form.cleaned_data['car_2']
			instance.car_3 = form.cleaned_data['car_3']
			instance.car_4 = form.cleaned_data['car_4']
			instance.car_5 = form.cleaned_data['car_5']
			instance.save()
			return redirect('game:index')
	else:
		form = UploadCarsForm(initial=model_to_dict(instance))

	context_dict['form'] = form
	context_dict['game_user'] = instance
	return render(request, 'game/index.html', context_dict)


@login_required()
@permission_required('game.view_game')
def level_1(request):
	context_dict = {}
	game_user = GameUser.objects.get(user=request.user)
	context_dict['game_user'] = game_user


	if game_user.car_1:
		context_dict['svg_car'] = game_user.car_1.url
	else:
		context_dict['svg_car'] = ''

	if request.method == 'POST':
		form = ScoreForm(request.POST)

		if form.is_valid():
			game_user.score_level_1 = form.cleaned_data['score']
			game_user.save()
			return redirect('game:index')
	else:
		form = ScoreForm()
	
	context_dict['send_score_form'] = form

	context_dict['level'] = 'svg/terrain2.svg'
	return render(request, 'game/race.html', context_dict)


@login_required()
@permission_required('game.view_game')
def level_2(request):
	context_dict = {}
	game_user = GameUser.objects.get(user=request.user)
	context_dict['game_user'] = game_user
	
	if game_user.car_2:
		context_dict['svg_car'] = game_user.car_2.url
	else:
		context_dict['svg_car'] = ''

	if request.method == 'POST':
		form = ScoreForm(request.POST)

		if form.is_valid():
			game_user.score_level_2 = form.cleaned_data['score']
			game_user.save()
			return redirect('game:index')
	else:
		form = ScoreForm()
	
	context_dict['send_score_form'] = form
	
	context_dict['level'] = 'svg/terrain2.svg'
	return render(request, 'game/race.html', context_dict)


@login_required()
@permission_required('game.view_game')
def level_3(request):
	context_dict = {}
	game_user = GameUser.objects.get(user=request.user)
	context_dict['game_user'] = game_user

	if game_user.car_3:
		context_dict['svg_car'] = game_user.car_3.url
	else:
		context_dict['svg_car'] = ''

	if request.method == 'POST':
		form = ScoreForm(request.POST)

		if form.is_valid():
			game_user.score_level_3 = form.cleaned_data['score']
			game_user.save()
			return redirect('game:index')
	else:
		form = ScoreForm()
	
	context_dict['send_score_form'] = form

	context_dict['level'] = 'svg/terrain2.svg'
	return render(request, 'game/race.html', context_dict)


@login_required()
@permission_required('game.view_game')
def level_4(request):
	context_dict = {}
	game_user = GameUser.objects.get(user=request.user)
	context_dict['game_user'] = game_user
	
	if game_user.car_4:
		context_dict['svg_car'] = game_user.car_4.url
	else:
		context_dict['svg_car'] = ''

	if request.method == 'POST':
		form = ScoreForm(request.POST)

		if form.is_valid():
			game_user.score_level_4 = form.cleaned_data['score']
			game_user.save()
			return redirect('game:index')
	else:
		form = ScoreForm()
	
	context_dict['send_score_form'] = form

	context_dict['level'] = 'svg/terrain2.svg'
	return render(request, 'game/race.html', context_dict)


@login_required()
@permission_required('game.view_game')
def level_5(request):
	context_dict = {}
	game_user = GameUser.objects.get(user=request.user)
	context_dict['game_user'] = game_user

	if game_user.car_2:
		context_dict['svg_car'] = game_user.car_5.url
	else:
		context_dict['svg_car'] = ''

	if request.method == 'POST':
		form = ScoreForm(request.POST)

		if form.is_valid():
			game_user.score_level_5 = form.cleaned_data['score']
			game_user.save()
			return redirect('game:index')
	else:
		form = ScoreForm()
	
	context_dict['send_score_form'] = form

	context_dict['level'] = 'svg/terrain2.svg'
	return render(request, 'game/race.html', context_dict)


def game_auth(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect('game:index')
			else:
				return HttpResponse('Your account is disabled')
		else:
			print("Invalid login details: {0}, {1}.".format(username, password))
			return HttpResponse("Invalid login details supplied")

	else:
		return render(request, 'game/login.html', {})


@csrf_protect
def game_login(request):
	form = LoginForm()
	context_dict = {'form': form}
	return render(request, 'game/login.html', context_dict)


@login_required()
def game_logout(request):
	logout(request)
	return redirect('game:login')


@login_required()
@permission_required('game.view_game')
def sign_s3(request):
	"""
	https://devcenter.heroku.com/articles/s3-upload-python
	"""
	AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
	AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
	S3_BUCKET = os.environ.get('S3_BUCKET_NAME')

	object_name = urllib.parse.quote_plus(request.GET['file-name'])
	mime_type = request.GET['file-type']

	secondsPerDay = 24*60*60
	expires = int(time.time()+secondsPerDay)
	amz_headers = "x-amz-acl:public-read"

	string_to_sign = "PUT\n\n%s\n%d\n%s\n/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, object_name)

	encodedSecretKey = AWS_SECRET_KEY.encode()
	encodedString = string_to_sign.encode()
	h = hmac.new(encodedSecretKey, encodedString, sha1)
	hDigest = h.digest()
	signature = base64.encodebytes(hDigest).strip()
	signature = urllib.parse.quote_plus(signature)
	url = 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, object_name)

	return JsonResponse({
		'signed_request': '%s?AWSAccessKeyId=%s&Expires=%s&Signature=%s' % (url, AWS_ACCESS_KEY, expires, signature),
		'url': url,
	})