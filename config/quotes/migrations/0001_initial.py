# Generated by Django 3.2.10 on 2022-05-10 06:28

import config.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('book_author', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(limit_value=2, message=None), config.validators.CharValidator], verbose_name='Author')),
                ('book_title', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(limit_value=2, message=None), config.validators.CharValidator], verbose_name='Title')),
                ('book_category', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(limit_value=2, message=None), config.validators.CharValidator], verbose_name='Category')),
                ('height', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('quote_file', models.ImageField(height_field='height', upload_to='upload', validators=[django.core.validators.validate_image_file_extension, django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])], verbose_name='Quote', width_field='width')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='quote_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quotes.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='quotes.quote')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
