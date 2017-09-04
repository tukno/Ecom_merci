# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 00:25
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(help_text='Preencha como está no Cartão de Crédito', max_length=256, verbose_name='Nome do Titular do Cartão de Crédito')),
                ('card_number', models.CharField(max_length=16, verbose_name='Número do Cartão de Crédito')),
                ('security_code', models.CharField(max_length=3, verbose_name='Código de Segurança do Cartão de Crédito')),
                ('expire_date', models.DateField(verbose_name='Validade do Cartão de Crédito')),
                ('provider', models.CharField(max_length=20, verbose_name='Bandeira do Cartão de Crédito')),
            ],
            options={
                'verbose_name': 'Cartão de Crédito',
                'verbose_name_plural': 'Cartões de Crédito',
            },
        ),
        migrations.CreateModel(
            name='CustomerUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(help_text='Número de telefone. Preencha apenas com númreos.', max_length=15, verbose_name='Número de Telefone')),
            ],
            options={
                'verbose_name': 'Número de Telefone',
                'verbose_name_plural': 'Números de Telefone',
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(help_text='Preencha com o nome completo do país onde esse endereço se encontra.', max_length=50, verbose_name='País')),
                ('state', models.CharField(help_text='Estado ou província onde esse estado se encontra.', max_length=50, verbose_name='Estado')),
                ('city', models.CharField(help_text='Cidade onde esse endereço se encontra.', max_length=50, verbose_name='Cidade')),
                ('zip_code', models.CharField(blank=True, help_text='Código de Endereço Postal', max_length=10, null=True, verbose_name='CEP')),
                ('address', models.CharField(help_text='Endereço Postal', max_length=256, verbose_name='Endereço')),
                ('reference', models.CharField(blank=True, help_text="Ponto de Referência nas redondezas. Ex: 'Ao lado da Farmécia'", max_length=256, null=True, verbose_name='Ponto de Referência.')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.PhoneNumber')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.CustomerUser')),
            ],
            options={
                'verbose_name': 'Endereço para Envio',
                'verbose_name_plural': 'Endereços para Envio',
                'ordering': ('country', 'state', 'city', 'zip_code'),
            },
        ),
        migrations.AddField(
            model_name='customeruser',
            name='phone_numbers',
            field=models.ManyToManyField(to='usuario.PhoneNumber'),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.CustomerUser'),
        ),
    ]
