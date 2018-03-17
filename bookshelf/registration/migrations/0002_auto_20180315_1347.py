# Generated by Django 2.0.3 on 2018-03-15 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20180313_1100'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('bookid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book.Book')),
            ],
        ),
        migrations.RenameField(
            model_name='myuser',
            old_name='already_read',
            new_name='to_read',
        ),
        migrations.AddField(
            model_name='myuser',
            name='rated_books',
            field=models.ManyToManyField(blank=True, to='registration.BookRating'),
        ),
    ]
