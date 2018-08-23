# Generated by Django 2.1 on 2018-08-07 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('criado_em', models.DateField(auto_now_add=True, verbose_name='data')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Quantidade de Cópias')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor Total')),
            ],
        ),
        migrations.CreateModel(
            name='Preco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('data', models.DateField(auto_now_add=True, verbose_name='data')),
                ('editao_em', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
                ('titulo', models.CharField(max_length=100, verbose_name='Descrição')),
                ('colorido', models.BooleanField(default=False, verbose_name='Colorido')),
                ('papel', models.CharField(choices=[('A4', 'A4'), ('A3', 'A3')], default='A4', max_length=10, verbose_name='Papel')),
                ('valor_copia', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor por cópia')),
            ],
        ),
        migrations.AddField(
            model_name='caixa',
            name='preco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Preco'),
        ),
    ]