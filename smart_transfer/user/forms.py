from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'user_type',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''  
            field.widget.attrs.update({'class': 'form-control'})  


class CustomUserLogin(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(
        label="Password",
        max_length=100,
        required=True,
        widget=forms.PasswordInput()
    )

