# Generated by Django 5.0.1 on 2024-01-24 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0005_ariza_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubPort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcriseportfolio', models.CharField(max_length=50)),
            ],
        ),
    ]