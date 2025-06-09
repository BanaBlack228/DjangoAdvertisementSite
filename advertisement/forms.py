from django import forms
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if kwargs.get('initial'):
            author = kwargs['initial'].pop('author')
        else:
            author = kwargs.pop('author')
        super().__init__(*args, **kwargs)
        self.fields['author'].initial = author
        self.fields['author'].disabled = True
        self.fields['author'].widget = forms.HiddenInput()

    class Meta:
        model = Post
        fields = ('title', 'text','image', 'author')

        labels = {
            'title': 'Загаловок',
            'text': 'Текст поста',
            'image': 'Изображение'
        }