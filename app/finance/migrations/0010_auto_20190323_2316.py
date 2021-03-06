# Generated by Django 2.1.7 on 2019-03-23 23:16

import app.finance.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_auto_20190323_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='limit',
            name='end_date',
            field=models.DateTimeField(blank=True, default=app.finance.models.get_end_of_month, help_text='The end date for this limit.'),
        ),
        migrations.AlterField(
            model_name='limit',
            name='start_date',
            field=models.DateTimeField(blank=True, default=app.finance.models.get_start_of_month, help_text='The day from which transactions under this tag will countin the limit.'),
        ),
    ]
