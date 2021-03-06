from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User

from products.models import Product


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = 'email'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login'))


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price',
                  'amount', 'manufacturer', 'product_model', 'category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create product'))
