# Generated by Django 4.2.3 on 2023-08-11 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0004_alter_advertisement_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
