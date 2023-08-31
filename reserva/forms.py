from django import forms
from reserva.models import Reserva


class ReservaModelForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'stand': forms.Select(attrs={'class': 'form-control'}),
            'nome_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_empresa': forms.Select(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'quitado': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
