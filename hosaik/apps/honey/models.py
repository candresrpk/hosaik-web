from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
    
    options = (
        ('expense', 'expense'),
        ('earn', 'earn'),
    )
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    ammount = models.IntegerField()
    type_of = models.CharField(max_length=7, choices=options)
    
    
    def __str__(self) -> str:
        return f'{self.title} - {self.ammount} as an {self.type_of}'
    