from django.db import models

class Usuario(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20)

    def str(self):
        return self.nome
    
# A forma da leitura do banco