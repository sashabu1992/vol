from django import forms
from .models import Profile

class UserProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(label='Фотография')
    bio = forms.CharField(label='Краткое описание', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}))
    city = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Город'}))
    user_phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}))
    vk = forms.CharField(label='Вконтакте', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Вконтакте'}))
    instagram = forms.CharField(label='Instagram', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Instagram'}))
    telegram = forms.CharField(label='Telegram', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telegram'}))

    class Meta:
        # Название модели на основе
        # которой создается форма
        model = Profile
        # Включаем все поля с модели в форму
        fields = ('profile_pic','bio','city','user_phone','vk','instagram','telegram')

    