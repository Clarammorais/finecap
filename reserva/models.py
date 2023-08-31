from django.db import models


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome_categoria


class Stand(models.Model):
    localizacao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.localizacao} - R${self.valor}'


class Reserva(models.Model):
    stand = models.OneToOneField(
        Stand, on_delete=models.SET_NULL, null=True
    )
    nome_empresa = models.CharField(max_length=100)
    categoria_empresa = models.ForeignKey(
        Categoria, on_delete=models.CASCADE
    )
    cnpj = models.CharField(max_length=18)
    quitado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nome_empresa