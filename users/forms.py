from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class CustomLoginForm(forms.ModelForm):
    username_or_email = forms.CharField(label='Username or Email', max_length=254)

    class Meta:
        model = User
        fields = ['username_or_email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get('username_or_email')
        password = cleaned_data.get('password')

        if username_or_email and password:
            # check if the user entered an email address
            if '@' in username_or_email:
                try:
                    # try to get the user by email
                    user = User.objects.get(email=username_or_email)
                    cleaned_data['username'] = user.username
                except User.DoesNotExist:
                    raise ValidationError('Invalid email or password')
            else:
                cleaned_data['username'] = username_or_email

        return cleaned_data
