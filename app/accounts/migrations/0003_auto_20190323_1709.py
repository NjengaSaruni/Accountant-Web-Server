# Generated by Django 2.1.7 on 2019-03-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190113_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='The time the transaction was done.'),
        ),
    ]