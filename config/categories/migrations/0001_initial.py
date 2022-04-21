# Generated by Django 4.0.4 on 2022-04-21 20:58

import config.validators
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(limit_value=2, message=None), config.validators.CharValidator], verbose_name='category')),
            ],
        ),
    ]
