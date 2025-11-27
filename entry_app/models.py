from django.db import models
from acco.models import AccountsUser

# Create your models here.

class ModelApp(models.Model):
    t_title = models.CharField(max_length=10)
    t_text = models.CharField(max_length=100)
    user = models.ForeignKey(AccountsUser, on_delete=models.CASCADE)