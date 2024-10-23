# Generated by Django 5.1.2 on 2024-10-21 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_feehistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feehistory',
            name='transaction_id',
        ),
        migrations.AlterField(
            model_name='feehistory',
            name='payment_status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]