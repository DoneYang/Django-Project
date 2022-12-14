# Generated by Django 4.1.2 on 2022-10-25 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_bookcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'Author'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='bookcomment',
            options={'ordering': ['id'], 'verbose_name_plural': ['Book Comment']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AddField(
            model_name='book',
            name='level',
            field=models.CharField(blank=True, choices=[('B', 'Basic'), ('M', 'Menium'), ('A', 'Advance')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bookcomment',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
