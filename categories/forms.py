from django.forms import ModelForm
from django.forms.widgets import TextInput

from .models import Footware, Clothing, Automobile, Electronic, Furniture, Sport, Book


class FootwareForm(ModelForm):
    class Meta:
        model = Footware
        fields = '__all__'


class ClothingForm(ModelForm):
    class Meta:
        model = Clothing
        fields = '__all__'
        

class AutomobileForm(ModelForm):
    class Meta:
        model = Automobile
        fields = '__all__'


class ElectronicForm(ModelForm):
    class Meta:
        model = Electronic
        fields = '__all__'


class FurnitureForm(ModelForm):
    class Meta:
        model = Furniture
        fields = '__all__'


class SportForm(ModelForm):
    class Meta:
        model = Sport
        fields = '__all__'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

