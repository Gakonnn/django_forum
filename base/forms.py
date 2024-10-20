from .models import Rooms,Message,Topics
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ('name','topic','description')


class RegisterForm(UserCreationForm):
    class  Meta:
        model = User
        fields = ['username','password1','password2']



class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']