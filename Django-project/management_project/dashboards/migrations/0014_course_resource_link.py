# Generated by Django 5.1.4 on 2024-12-25 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0013_rename_resource_link_module_youtube_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='resource_link',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]