from django import forms


class ModelForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField()
    publication_date = forms.DateField(auto_now_add=True)
    category = forms.CharField()
    author = forms.CharField()