# Generated by Django 4.1.2 on 2022-10-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_alter_author_options_alter_book_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='book'),
        ),
    ]
