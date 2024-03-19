# Generated by Django 4.2.8 on 2024-03-18 01:15

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("about", "0019_delete_snapshot"),
    ]

    operations = [
        migrations.AddField(
            model_name="aboutpage",
            name="snap_shot",
            field=wagtail.fields.StreamField(
                [
                    (
                        "snap_shot",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("amount", wagtail.blocks.IntegerBlock()),
                            ]
                        ),
                    )
                ],
                default=None,
            ),
        ),
    ]
