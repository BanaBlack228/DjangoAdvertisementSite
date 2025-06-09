from django.urls import path
from advertisement.views import (main_page, about,
                                 settings,support,
                                 about_a_site,add_post,
                                 read_post, update_post,
                                 delete_post, user_posts, user_info)

app_name = 'advertisement'
urlpatterns = [
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
    path('post/user/info/<int:user_id>/', user_info, name='user_info'),
    path('post/user/<int:user_id>/', user_posts, name='user_posts'),
    path('post/<int:pk>/edit/', update_post, name='update_post'),
    path('post/<slug:slug>/', read_post, name='read_post'),
    path('post', add_post, name='add_post'),
    path('about/', about, name='about'),
    path('settings/', settings, name='settings'),
    path('support/', support, name='support'),
    path('about_a_site/', about_a_site, name='about_a_site'),
    path('', main_page, name='main_page')
]