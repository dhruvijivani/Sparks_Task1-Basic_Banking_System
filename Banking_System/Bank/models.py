from django.db import models

# Create your models 

class user(models.Model):
    account_no = models.IntegerField(null=False)
    Name = models.CharField(null=False,max_length=100)
    Email=models.EmailField()
    Balance = models.PositiveIntegerField(null=False)
    def __str__(self):
        return self.Name

class transaction_details(models.Model):
    source_name = models.CharField(max_length=122)
    source_acc_no = models.CharField(max_length=122)
    Current_balance = models.PositiveIntegerField()
    money_deposit = models.PositiveIntegerField(null=False)
    destination_name = models.CharField(max_length=122)
    date = models.DateField()