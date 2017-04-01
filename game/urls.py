from django.conf.urls import url


from . import views

app_name = 'game'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.game_login, name='login'),
    url(r'^logout/$', views.game_logout, name='logout'),
	url(r'^auth/$', views.game_auth, name='login_auth'),

	# # S3 Signing
	# url(r'^sign-s3/$', views.sign_s3, name='sign_s3'),

	# Levels
	url(r'^level/1$', views.level_1, name='level_1'),
	url(r'^level/2$', views.level_2, name='level_2'),
	url(r'^level/3$', views.level_3, name='level_3'),
	url(r'^level/4$', views.level_4, name='level_4'),
	url(r'^level/5$', views.level_5, name='level_5'),
	
]