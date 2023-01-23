# Generated by Django 3.2 on 2023-01-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('amount', models.FloatField()),
                ('type', models.CharField(choices=[('percent', 'percent'), ('fix', 'fix')], default='percent', max_length=10)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('expire', models.DateTimeField(blank=True, null=True)),
                ('number', models.IntegerField(default=0)),
                ('remaining', models.IntegerField(default=0)),
                ('is_unexpired', models.BooleanField(default=False)),
                ('is_unlimited', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]