# Generated by Django 2.1.5 on 2019-02-23 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0020_profile_type_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type_user',
            field=models.CharField(default='student', max_length=20),
        ),
    ]
