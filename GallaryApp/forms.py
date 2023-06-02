from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from django.contrib.auth.models import User
from.models import ImageModel


class UserAuthentication(AuthenticationForm):

    username=forms.CharField(label='enter username',widget=forms.TextInput(attrs={'class':'form-control'}))
    
    password=forms.CharField(label='enter password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User

class RegisterForm(UserCreationForm):

    password1=forms.CharField(label='enter password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User 
        fields=['username','first_name','last_name','email','password1','password2']   

        labels={
            'username':'Enter Username',
            'first_name':'Enter FirstName',
            'last_name':'Enter Last Name',
            'email':'Enter Email-Id',
        } 

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            
        } 

class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageModel
        fields=['title','cat','image','desc']   

        labels={
            'title':'Enter Title',
            'cat':'Enter cat',
            'image':'select image to upload',
            'desc':'Enter desc',

        }

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
            'cat':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }       