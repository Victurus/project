# Generated by Django 2.0.3 on 2018-03-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20180313_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(blank=True, to='book.Genre'),
        ),
    ]
