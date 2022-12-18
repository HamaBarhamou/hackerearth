# Generated by Django 4.1.4 on 2022-12-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitorig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('mac_adresse', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField(default=None)),
                ('usage_time', models.TimeField(default=None)),
                ('upload', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('download', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
            ],
        ),
    ]
