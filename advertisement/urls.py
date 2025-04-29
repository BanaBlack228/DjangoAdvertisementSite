from django.urls import path
from advertisement.views import (main_page, about,
                                 settings,support,
                                 notification,registration,
                                 add_post,read_post,
                                 update_post, delete_post)

app_name = 'advertisement'
urlpatterns = [
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
    path('post/<int:pk>/edit/', update_post, name='update_post'),
    path('post/<int:pk>/', read_post, name='read_post'),
    path('post', add_post, name='add_post'),
    path('about/', about, name='about'),
    path('settings/', settings, name='settings'),
    path('support/', support, name='support'),
    path('registration/', registration, name='registration'),
    path('notification/', notification, name='notification'),
    path('', main_page, name='main_page')
]