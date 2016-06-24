from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_page.models import User

class RegistrationForm(UserCreationForm):
    nickname = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'nickname', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.nickname = self.cleaned_data['nickname']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
