from django.db import models

# Create your models here.
class Accounts(models.Model):
    AccountType = {
        ('debit', 'Debit'),
        ('credit', 'Credit')

    }
    purpose     = models.CharField(max_length=100)
    acc_type    = models.CharField(max_length=10, choices=AccountType, blank=False)
    amount      = models.DecimalField(max_digits=11, decimal_places= 2)
    created     = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.purpose
