# Generated by Django 5.0.1 on 2024-01-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0003_rename_qoshish_ariza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcrise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcrise', models.CharField(max_length=50)),
            ],
        ),
    ]
