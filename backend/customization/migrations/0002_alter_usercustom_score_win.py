# Generated by Django 5.1 on 2024-09-04 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustom',
            name='score_win',
            field=models.IntegerField(default=5),
        ),
    ]
