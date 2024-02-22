# Generated by Django 5.0.2 on 2024-02-22 04:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0017_itemsumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemsumber',
            old_name='sku',
            new_name='item',
        ),
        migrations.AlterField(
            model_name='itemsumber',
            name='jenis_sumber',
            field=models.CharField(choices=[('online', 'Online Store'), ('pabrik', 'Pabrik')], max_length=30),
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revenue_PO', models.IntegerField()),
                ('nomor_PO', models.IntegerField()),
                ('tanggal_PO', models.DateField()),
                ('tanggal_process', models.DateField()),
                ('tanggal_input_accurate', models.DateField()),
                ('tanggal_pengiriman_barang', models.DateField()),
                ('tanggal_pengiriman_invoice', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], max_length=30)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page1.items')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page1.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revenue_PO', models.IntegerField()),
                ('nomor_PO', models.IntegerField()),
                ('tanggal_PO', models.DateField()),
                ('tanggal_process', models.DateField()),
                ('tanggal_input_accurate', models.DateField()),
                ('tanggal_pengiriman_barang', models.DateField()),
                ('tanggal_pengiriman_invoice', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], max_length=30)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page1.customer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page1.items')),
            ],
        ),
    ]
