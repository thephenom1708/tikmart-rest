from django.forms import ModelForm
from django.forms.widgets import TextInput

from .models import Color

class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
        widgets = {
            'hexcode': TextInput(attrs={'type': 'color'}),
        }
