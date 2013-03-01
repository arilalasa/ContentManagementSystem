from django import forms
from django.contrib.auth.models import User

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100,label='Article Header')
    content = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    userid=forms.CharField()
    password=forms.CharField()

class RegisterForm(forms.Form):
    username=forms.CharField(label = "Username",max_length = 30)
    first_name=forms.CharField(label = "Firstname", max_length = 50)
    last_name=forms.CharField(label = 'Lastname', max_length =50)
    email=forms.EmailField(label = 'Email', max_length = 75)
    password=forms.CharField(label = 'Password', widget = forms.PasswordInput)
    confirm_password=forms.CharField(label = 'Password confirmation',widget = forms.PasswordInput, help_text = 'enter the same Password as above')
    def clean_username(self):
        try:
             User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("this user exists already")

    def clean(self):
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise forms.ValidationError("passwords dont match each other")
        
        return self.cleaned_data

    def save1(self):
        new_user=User.objects.create_user(
                 username = self.cleaned_data['username'],
                 email =  self.cleaned_data['email'],
                 password = self.cleaned_data['password'])
        new_user.first_name=self.cleaned_data['first_name']
        new_user.last_name=self.cleaned_data['last_name']
        new_user.save()
        return new_user
        



    
