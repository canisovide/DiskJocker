# Generated by Django 4.1.3 on 2023-01-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0008_disque_region'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disque',
            old_name='region',
            new_name='continent',
        ),
        migrations.AddField(
            model_name='disque',
            name='pays',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
