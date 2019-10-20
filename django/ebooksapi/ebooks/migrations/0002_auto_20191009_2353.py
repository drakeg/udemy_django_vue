# Generated by Django 2.2.6 on 2019-10-10 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
