# Generated by Django 2.1.2 on 2018-10-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_liftit', '0002_auto_20181024_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='id_number',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
    ]
