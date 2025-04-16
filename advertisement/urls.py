from django.urls import path
from advertisement.views import main_page, about, settings,support,notification

app_name = 'advertisement'
urlpatterns = [
    path('about/', about, name='about'),
    path('settings/', settings, name='settings'),
    path('support/', support, name='support'),
    path('notification/', notification, name='notification'),
    path('', main_page, name='main_page')
]