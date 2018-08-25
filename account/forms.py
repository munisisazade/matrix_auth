from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

from account.models import Article, Picture

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=58, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == 'email':
                self.fields[name].widget = forms.EmailInput(attrs={
                    'class': 'form-control'
                })
            elif name == 'password':
                self.fields[name].widget = forms.PasswordInput(attrs={
                    'class': 'form-control'
                })
            elif name == 'first_name' or name == 'last_name' or name == 'username':
                self.fields[name].widget = forms.TextInput(attrs={
                    'class': 'form-control'
                })


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['image',]


Pictureformset = forms.formset_factory(PictureForm)
