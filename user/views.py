from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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


# def register_view(request):
#     if request.method == 'POST':       
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             return redirect('main')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})


# Функция регистрации описанная в ручном режиме
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                # create_vser (служебный метод) - в этом месте происходит хеширование пароля
                user = User.objects.create_user(username=username, password=password)
                # Логиним и редиректим 
                login(request, user)
                return redirect('main')
            else:
                error = 'Пользователь с таким именем уже существует'
        else:
            error = 'Пароли не совпадают'
        
        # Негативный случай. Мы показываем ошибку пользователю
        return render(request, 'register.html', {'error': error})
    
    # Метод GET
    return render(request, 'register.html')
