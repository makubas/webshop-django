# Generated by Django 3.2.3 on 2021-05-31 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('products', '0003_auto_20210528_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='comments.Comment'),
        ),
    ]
