from django import forms


from .models import GameUser

class LoginForm(forms.Form):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': 'Password'}))


class UploadCarsForm(forms.ModelForm):
	car_1 = forms.FileField(required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
	car_2 = forms.FileField(required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
	car_3 = forms.FileField(required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
	car_4 = forms.FileField(required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
	car_5 = forms.FileField(required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
	class Meta:
		model = GameUser
		fields = ['car_1', 'car_2', 'car_3', 'car_4', 'car_5',]


class ScoreForm(forms.Form):
	score = forms.DecimalField()