# Generated by Django 3.2.4 on 2023-01-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20230103_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='projects',
            field=models.ManyToManyField(blank=True, to='projects.Project'),
        ),
    ]
