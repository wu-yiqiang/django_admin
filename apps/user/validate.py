from django import forms
from django.http import JsonResponse

from service_error.user import USER_RERROR
from .models import User


class LoginRegistrationFormValidate(forms.ModelForm):
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username is None:
            # return JsonResponse(USER_RERROR.USERNAME_IS_EMPTY)
            raise forms.ValidationError('用户名已存在')
        return username

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     if password is None:
    #         return JsonResponse(USER_RERROR.PASSWORD_IS_EMPTY)
    #     return password

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
