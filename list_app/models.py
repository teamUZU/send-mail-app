from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    tel_number = models.CharField(max_length=15, blank=True)
    mail = models.EmailField(max_length=5000, blank=True)
    regddate = models.DateField(blank=True)
    STATUSES = (
            ('アクティブ', 'アクティブ'),
            ('非アクティブ', '非アクティブ'),
            ('優良', '優良'),
            ('取引終了', '取引終了'),
            ('運営者', '運営者'),
        )
    status = models.CharField(
        max_length=10,
        choices=STATUSES,
        default='取引終了',
        )
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    tel_number = models.CharField(max_length=15, blank=True)
    mail = models.EmailField(max_length=50, blank=True)
    regddate = models.DateField(blank=True)
    STATUSES = (
            ('アクティブ', 'アクティブ'),
            ('非アクティブ', '非アクティブ'),
            ('優良', '優良'),
            ('利用終了', '利用終了'),
            ('運営者', '運営者'),
        )
    status = models.CharField(
        max_length=10,
        choices=STATUSES,
        default='利用終了',
        )
    
    def __str__(self):
        return self.name