from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Oferta(models.Model):
    CATEGORIA_CHOICES = [
        ('alimentacao', 'Alimentação'),
        ('bebidas', 'Bebidas'),
        ('servicos', 'Serviços'),
        ('produtos', 'Produtos'),
        ('outros', 'Outros'),
    ]
    
    STATUS_CHOICES = [
        ('ativa', 'Ativa'),
        ('inativa', 'Inativa'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name="Título da Oferta")
    descricao = models.TextField(verbose_name="Descrição")
    preco_original = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
        validators=[MinValueValidator(0.01)],
        verbose_name="Preço Original"
    )
    preco_oferta = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Preço com Desconto"
    )
    validade = models.DateField(verbose_name="Validade")
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativa')
    imagem = models.URLField(max_length=500, blank=True, verbose_name="URL da Imagem")
    estabelecimento = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE,
        related_name='ofertas'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-data_criacao']
    
    def __str__(self):
        return self.titulo
    
    @property
    def desconto_percentual(self):
        if self.preco_original:
            return round(((self.preco_original - self.preco_oferta) / self.preco_original) * 100)
        return 0
    
    def esta_valida(self):
        return self.validade >= timezone.now().date() and self.status == 'ativa'

# Create your models here.
