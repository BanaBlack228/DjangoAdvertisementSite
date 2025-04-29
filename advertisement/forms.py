from django import forms
from django.contrib.auth.models import User
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=200, label="Загаловок")
    text = forms.CharField(widget=forms.Textarea, label="Текст объявления")
    author = forms.ModelChoiceField(queryset=User.objects.all(), label="Автор")
    image = forms.ImageField(required=False, label="Изображение")

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

        # fields = '__all__'
        #exclude = ('author','created_at')

        labels = {
            'title':'Загаловок',
            'text': 'Текст поста'
        }