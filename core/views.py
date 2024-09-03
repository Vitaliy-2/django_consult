from django.shortcuts import render, redirect
from .forms import VisitModelForm
from .models import Visit, Master, Service
from django.http import JsonResponse


def main(request):
    # Мастера для карусели фоточек (в форму данные берутся и по мастерам и по услугам автоматически)
    masters = Master.objects.all()
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

    return render(request, 'main.html', {'form': form, 'masters': masters})


def thanks(request):
    return render(request, 'thanks.html')


def get_services_by_master(request, master_id):
    services = Master.objects.get(id=master_id).services.all()
    services_data = [{'id': service.id, 'name': service.name} for service in services]
    return JsonResponse({'services': services_data})

