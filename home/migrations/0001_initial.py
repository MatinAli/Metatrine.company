# Generated by Django 4.2.8 on 2024-03-19 23:53

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):
    initial = True

    # dependencies = [
    #     ("wagtailcore", "0092_query_searchpromotion_querydailyhits"),
    # ]

    operations = [
        migrations.CreateModel(
            name="HomePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "hero_title",
                    wagtail.fields.StreamField(
                        [("title", wagtail.blocks.CharBlock())], blank=True, null=True
                    ),
                ),
                ("slogan", models.CharField(blank=True, max_length=2000)),
                (
                    "call_to_action",
                    wagtail.fields.StreamField(
                        [("items", wagtail.blocks.CharBlock())], blank=True, null=True
                    ),
                ),
                (
                    "content_row",
                    models.CharField(blank=True, max_length=10000, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="BusinessStatement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("body", wagtail.fields.RichTextField()),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="business_statement",
                        to="home.homepage",
                    ),
                ),
            ],
        ),
    ]
