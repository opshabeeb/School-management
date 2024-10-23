# Generated by Django 5.1.2 on 2024-10-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(max_length=10)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('student_class', models.CharField(choices=[('1', 'Class 1'), ('2', 'Class 2'), ('3', 'Class 3'), ('4', 'Class 4'), ('5', 'Class 5'), ('6', 'Class 6'), ('7', 'Class 7'), ('8', 'Class 8'), ('9', 'Class 9'), ('10', 'Class 10'), ('11', 'Class 11'), ('12', 'Class 12')], max_length=25)),
                ('division', models.CharField(choices=[('A', 'Division A'), ('B', 'Division B'), ('C', 'Division C'), ('D', 'Division D'), ('E', 'Division E')], max_length=25)),
            ],
        ),
    ]
