# Generated by Django 4.2.8 on 2024-03-07 22:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_blogpage_post_body"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blogindexpage",
            old_name="hero_subtilte",
            new_name="hero_subtitle",
        ),
    ]
