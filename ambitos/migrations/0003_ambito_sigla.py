# Generated by Django 2.1.3 on 2018-11-12 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambitos', '0002_auto_20181112_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambito',
            name='sigla',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='Sigla'),
        ),
    ]
