# Generated by Django 4.2.7 on 2024-01-03 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense_entry',
            name='expense_user',
            field=models.CharField(max_length=250),
        ),
    ]