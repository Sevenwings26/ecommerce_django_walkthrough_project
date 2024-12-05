from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'block py-3 w-2/3', 'placeholder':'Unique email address'}))
    username = forms.CharField(label='', max_length=150, widget=forms.TextInput(attrs={'class':'block py-3', 'placeholder':'Username'}))
        
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'block py-3 w-2/3'
        self.fields['username'].widget.attrs['placeholder'] ='Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_only </small></span>'
        
        self.fields['password1'].widget.attrs['class'] = 'block py-3 w-2/3'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text=' <ul class="form-text text-muted" > <li>Your password can\'t be too similar to your personal information.</li> <li> Your password must contain 8 characters. </li><li>Your password can\'t be too commonly used password</li> <li> Your password can\'t be entirely numeric. </ul>'
        # self.fields['password1'].help_text=''
        
        self.fields['password2'].widget.attrs['class'] = 'block w-2/3 py-3'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'mb-2', 'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': '', 'placeholder': 'Password'}))



