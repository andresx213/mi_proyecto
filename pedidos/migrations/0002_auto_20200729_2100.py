# Generated by Django 3.0.8 on 2020-07-29 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameModel(
            old_name='Articulos',
            new_name='Articulo',
        ),
        migrations.RenameModel(
            old_name='pedidos',
            new_name='pedido',
        ),
        migrations.DeleteModel(
            name='Cientes',
        ),
    ]
