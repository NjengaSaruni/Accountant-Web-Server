# Generated by Django 2.1.7 on 2019-03-22 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0006_tag_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Limit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='The maximum amount allowed for this tag', max_digits=100)),
                ('start_date', models.DateTimeField(auto_now_add=True, help_text='The day from which transactions under this tag will countin the limit.')),
                ('end_date', models.DateTimeField(auto_now_add=True, help_text='The end date for this limit.')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('tag', models.ForeignKey(help_text='The tag whose limit is being added', on_delete=django.db.models.deletion.PROTECT, related_name='limits', to='finance.Tag')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
