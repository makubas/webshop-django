# Generated by Django 3.2.3 on 2021-05-29 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210528_1254'),
        ('purchases', '0004_auto_20210529_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
