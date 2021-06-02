# Generated by Django 3.2.3 on 2021-05-29 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0003_auto_20210529_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='payment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchases.payment'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='shipping',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchases.shipping'),
        ),
    ]