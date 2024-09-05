from django.shortcuts import render, redirect
from .forms import VisitModelForm
from .models import Visit, Master, Service
from django.http import JsonResponse
# Импорт базового View класса
from django.views.generic import View


MENU = [
        {'title': 'Главная', 'url': '/', 'active': True},
        {'title': 'Мастера', 'url': '#masters', 'active': True},
        {'title': 'Услуги', 'url': '#services', 'active': True},
        {'title': 'Отзывы', 'url': '#reviews', 'active': True},
        {'title': 'Запись на стрижку', 'url': '#orderForm', 'active': True},
    ]

def get_menu_context(menu: list[dict] = MENU):
    return {"menu": menu}


def main(request):
    # Мастера для карусели фоточек (в форму данные берутся и по мастерам и по услугам автоматически)
    masters = Master.objects.all()
    menu = get_menu_context()

    if request.method == 'POST':
        form = VisitModelForm(request.POST)
        # метод is_valid - проверяет все ли поля заполнены корректно,
        # он сам проверяет валидацию из файла формс, нами написанных методов
        if form.is_valid():
            # Сохранение будет быстрее
            form.save()
            # Перенаправляем на страницу благодарности
            return redirect('thanks')
        
        # Отдаем заполненную форму с ошибку
        if form.errors:
            return render(request, "main.html", {"form": form, 'masters': masters})
        
        
    else:
        form = VisitModelForm()

    return render(request, 'main.html', {'form': form, 'masters': masters, **menu})


class ThanksView(View):
    ''' 
    Функция get будет обрабатывать запрос методом get
    Еще есть post, put (обновить), delete
    View - базовый класс для создания представлений
    '''
    def get(self, request):
        return render(request, 'thanks.html', get_menu_context())


def get_services_by_master(request, master_id):
    services = Master.objects.get(id=master_id).services.all()
    services_data = [{'id': service.id, 'name': service.name} for service in services]
    return JsonResponse({'services': services_data})

