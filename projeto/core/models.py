from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'Criado em',
        auto_now_add=True,  # Define a data de criação automaticamente
        null=False,         # Garante que o campo não seja nulo
        blank=False         # Garante que o campo não seja deixado em branco no admin
    )
    modified = models.DateTimeField(
        'Modificado em',
        auto_now=True,      # Atualiza automaticamente a data de modificação
        null=False,         # Garante que o campo não seja nulo
        blank=False         # Garante que o campo não seja deixado em branco no admin
    )

    class Meta:
        abstract = True  # Garante que este modelo seja abstrato e não crie uma tabela no banco

