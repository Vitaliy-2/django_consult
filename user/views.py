from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # request - нужен бля выдачи кукисов пользователю (доступ к маршрутам)
        # Тут же в password=password происходит хэширование
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Неверные учетные данные')
    
    # Метод GET
    return render(request, 'login.html')


def logout_view(request):
    # logout - выйти из системы
    logout(request)
    return redirect('main')
