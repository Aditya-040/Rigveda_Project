# Generated by Django 4.1.1 on 2022-11-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0005_alter_yoga_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yoga',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='yoga',
            name='problem',
            field=models.CharField(max_length=500),
        ),
    ]