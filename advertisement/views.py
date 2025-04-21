from django.shortcuts import render


def main_page(request):
    context = {"title": "Главная страница"}
    return   render(request, template_name='advertisement/main_page.html', context=context)

def about(request):
    context = {"title": "Объявления"}
    return   render(request, template_name='advertisement/about.html', context=context)

def settings(request):
    context = {"title": "Настройки"}
    return   render(request, template_name='advertisement/settings.html', context=context)

def support(request):
    context = {"title": "Поддержка"}
    return   render(request, template_name='advertisement/support.html', context=context)

def notification(request):
    context = {"title": "Уведомления"}
    return   render(request, template_name='advertisement/notification.html', context=context)

def registration(request):
    context = {"title": "Регистрация"}
    return   render(request, template_name='advertisement/registration.html', context=context)