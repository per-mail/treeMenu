# Generated by Django 3.0.4 on 2023-02-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rubric',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]