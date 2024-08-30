from tkinter import W
from django import forms
import re


class VisitForm(forms.Form):
    name = forms.CharField(label = 'Имя', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}))
    phone = forms.CharField(label = 'Телефон', max_length=20, widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Номер телефона', 'class': 'form-control'}))
    comment = forms.CharField(label = 'Комментарий', required=False, widget=forms.Textarea(attrs={'placeholder': 'Комментарий', 'class': 'form-control'}))

    def clean_phone(self):
        # self.cleaned_data - словарь с данными, полученными из формы
        phone = self.cleaned_data.get("phone", '').strip()
        
        # Проверяем формат номера +7, 8
        phone_pattern = r'^(\+7|8)\d{10}$'

        if not re.match(phone_pattern, phone):
            raise forms.ValidationError("Номер должен начинаться +7, 8 и далее 10 цифр")
        return phone
