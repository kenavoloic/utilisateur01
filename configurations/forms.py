# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field

class CustomLoginForm(forms.Form):
    username = forms.CharField(
        label="👤 Identifiant",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password = forms.CharField(
        label="🔒 Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'custom-form'
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            HTML('<h2 class="login-title">🔐 Connexion</h2>'),
            Field('username', css_class='form-group'),
            Field('password', css_class='form-group'),
            Submit('submit', '🚀 Se connecter 🚪✨✨', css_class='btn btn-primary')
        )
