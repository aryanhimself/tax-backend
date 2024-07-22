from django.db import models

from users.models import User

# Create your models here.
class FiscalYear(models.Model):
    initiate_date = models.DateField(max_length=5)
    meta = models.JSONField(null=True, blank=True)
    label = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)

# insert into dbo.fiscal_year(initiate_date, meta, label, description) values ('2023-04-01', {}, "2079-80", "Fiscal Year 2079-80");
    def __str__(self):
        return self.initiate_date.__str__()

    class Meta:
        verbose_name = 'Fiscal Year'
        verbose_name_plural = 'Fiscal Years'


class IncomeTaxPolicy(models.Model):
    fiscal_year = models.ForeignKey(FiscalYear, null=False, on_delete=models.DO_NOTHING)
    meta = models.JSONField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'Income Tax Policy - {self.fiscal_year.initiate_date.year}'

    class Meta:
        verbose_name = 'Income Tax Policy'
        verbose_name_plural =  'Income Tax Policies'


class IncomeTaxRecord(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('dispute', 'In dispute')
    )
    user = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    meta = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.status}'

    class Meta:
        verbose_name = 'Income Tax Record'
        verbose_name_plural =  'Income Tax Records'


class CorporateTaxPolicy(models.Model):
    fiscal_year = models.ForeignKey(FiscalYear, null=False, on_delete=models.DO_NOTHING)
    meta = models.JSONField()

    def __str__(self):
        return f'Corporate Tax Policy - {self.fiscal_year.initiate_date.year}'

    class Meta:
        verbose_name = 'Income Tax Policy'
        verbose_name_plural =  'Income Tax Policies'


class CorporateTaxRecord(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('dispute', 'In dispute')
    )
    user = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    meta = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.status}'

    class Meta:
        verbose_name = 'Corporate Tax Record'
        verbose_name_plural =  'Corporate Tax Records'

class VehicleTaxPolicy(models.Model):
    fiscal_year = models.ForeignKey(FiscalYear, null=False, on_delete=models.DO_NOTHING)
    meta = models.JSONField()

    def __str__(self):
        return f'Vehicle Tax Policy - {self.fiscal_year.initiate_date.year}'

    class Meta:
        verbose_name = 'Vehicle Tax Policy'
        verbose_name_plural =  'Vehicle Tax Policies'

class VehicleTaxRecord(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('dispute', 'In dispute')
    )
    user = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    meta = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.status}'

    class Meta:
        verbose_name = 'Vehicle Tax Record'
        verbose_name_plural =  'Vehicle Tax Records'

