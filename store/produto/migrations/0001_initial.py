# Generated by Django 3.0.6 on 2020-06-03 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('categoria',),
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importado', models.BooleanField(default=False)),
                ('ncm', models.CharField(max_length=13, verbose_name='NCM')),
                ('produto', models.CharField(max_length=100, unique=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='preço')),
                ('estoque', models.IntegerField(verbose_name='estoque atual')),
                ('estoque_minimo', models.PositiveIntegerField(default=0, verbose_name='estoque mínimo')),
                ('data', models.DateField(blank=True, null=True)),
                ('categoria', models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='produto.Categoria')),
            ],
            options={
                'ordering': ('produto',),
            },
        ),
    ]
