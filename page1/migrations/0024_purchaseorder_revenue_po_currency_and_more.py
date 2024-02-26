# Generated by Django 5.0.2 on 2024-02-26 02:24

import djmoney.models.fields
from decimal import Decimal
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0023_merge_20240223_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='revenue_PO_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('IDR', 'Indonesian Rupiah (Rp.)'), ('USD', 'US Dollar ($)')], default='IDR', editable=False, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='workorder',
            name='revenue_PO_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('IDR', 'Indonesian Rupiah (Rp.)'), ('USD', 'US Dollar ($)')], default='IDR', editable=False, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='revenue_PO',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0'), default_currency='IDR', max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='revenue_PO',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0'), default_currency='IDR', max_digits=15, null=True),
        ),
    ]
