from django.db import models

class categoria(models.Model):
    nome= models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class produtos(models.Model):
    nome= models.CharField(max_length=200)
    descrição = models.TextField()
    preco= models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    link_externo = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
