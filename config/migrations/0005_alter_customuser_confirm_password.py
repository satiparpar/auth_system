# Generated by Django 5.0 on 2023-12-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_alter_customuser_confirm_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='confirm_password',
            field=models.CharField(max_length=128),
        ),
    ]
