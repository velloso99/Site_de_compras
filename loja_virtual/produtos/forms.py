from django import forms 
from .models import produtos

class produtosform(forms.ModelForm):
    class Meta:
        model= produtos
        fields = '__all__'