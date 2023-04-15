# Generated by Django 3.1.3 on 2023-03-25 08:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0009_auto_20230325_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='viewer',
            field=models.ManyToManyField(related_name='viewer_question', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='View',
        ),
    ]
