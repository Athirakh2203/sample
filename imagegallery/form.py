from django import forms
from .models import imagegallery
class imageForm(forms.ModelForm):
    class Meta:
        model=imagegallery
        fields=('caption','image')