# Generated by Django 4.2.8 on 2024-03-19 13:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0011_blogcomment_content_object"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blogcomment",
            old_name="blogPage",
            new_name="post",
        ),
    ]