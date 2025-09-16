from django import forms
from .models import Oferta
from django.core.exceptions import ValidationError
from django.utils import timezone

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = [
            'titulo', 'descricao', 'preco_original', 'preco_oferta',
            'validade', 'categoria', 'status', 'imagem'
        ]
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }
    
    def clean_validade(self):
        validade = self.cleaned_data.get('validade')
        if validade and validade < timezone.now().date():
            raise ValidationError("A validade não pode ser anterior à data atual.")
        return validade
    
    def clean(self):
        cleaned_data = super().clean()
        preco_original = cleaned_data.get('preco_original')
        preco_oferta = cleaned_data.get('preco_oferta')
        
        if preco_original and preco_oferta and preco_original <= preco_oferta:
            raise ValidationError("O preço original deve ser maior que o preço com desconto.")
        
        return cleaned_data