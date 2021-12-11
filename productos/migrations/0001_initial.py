# Generated by Django 3.2.9 on 2021-11-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('codigo_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=255, null=True)),
                ('nitproveedor', models.IntegerField()),
                ('precio_compra', models.FloatField()),
                ('ivacompra', models.FloatField()),
                ('precio_venta', models.FloatField()),
            ],
        ),
    ]