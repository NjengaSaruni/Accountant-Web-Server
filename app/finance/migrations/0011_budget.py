# Generated by Django 2.1.7 on 2019-04-09 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0010_auto_20190323_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='The maximum amount allowed for the tag in this m', max_digits=100)),
                ('overflow', models.BooleanField(blank=True, default=False, help_text='Whether the budget remains will overflow into the next cycle.')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('tag', models.ForeignKey(help_text='The tag whose budget is being added', on_delete=django.db.models.deletion.PROTECT, related_name='budgets', to='finance.Tag')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]