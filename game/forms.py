from django import forms

from s3direct.widgets import S3DirectWidget

from .models import GameUser

class LoginForm(forms.Form):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': 'Password'}))


class UploadCarsForm(forms.ModelForm):
	car_1 = forms.URLField(required=False, widget=S3DirectWidget(dest='svg_cars'))
	car_2 = forms.URLField(required=False, widget=S3DirectWidget(dest='svg_cars'))
	car_3 = forms.URLField(required=False, widget=S3DirectWidget(dest='svg_cars'))
	car_4 = forms.URLField(required=False, widget=S3DirectWidget(dest='svg_cars'))
	car_5 = forms.URLField(required=False, widget=S3DirectWidget(dest='svg_cars'))
	class Meta:
		model = GameUser
		fields = ['car_1', 'car_2', 'car_3', 'car_4', 'car_5',]


class ScoreForm(forms.Form):
	score = forms.DecimalField()