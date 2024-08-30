from django.shortcuts import render, redirect
from .forms import VisitForm
from .models import Visit, Master


def main(request):
    # Мастера для карусели фоточек (в форму данные берутся и по мастерам и по услугам автоматически)
    masters = Master.objects.all()
    if request.method == 'POST':
        form = VisitForm(request.POST)
        # метод is_valid - проверяет все ли поля заполнены корректно,
        # он сам проверяет валидацию из файла формс, нами написанных методов
        if form.is_valid():
            # Создание и сохранение записи в модели Visit
            Visit.objects.create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                comment=form.cleaned_data['comment'],
            )
            # Перенаправляем клиента на страницу благодарности если всё норм
            return redirect('thanks')
    else:
        form = VisitForm()

    return render(request, 'main.html', {'form': form, 'masters': masters})


def thanks(request):
    return render(request, 'thanks.html')

