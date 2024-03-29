# Generated by Django 4.2.8 on 2024-03-20 00:05

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):
    initial = True

    # dependencies = [
    #     # ("wagtailcore", "0092_query_searchpromotion_querydailyhits"),
    #     ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
    # ]

    operations = [
        migrations.CreateModel(
            name="AboutPage",
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
                ("services", wagtail.fields.RichTextField(max_length=600)),
                (
                    "services_item",
                    wagtail.fields.StreamField(
                        [("block", wagtail.blocks.CharBlock())], blank=True, null=True
                    ),
                ),
                (
                    "hero_title",
                    wagtail.fields.StreamField(
                        [("block", wagtail.blocks.CharBlock())], blank=True, null=True
                    ),
                ),
                (
                    "snap_shot",
                    wagtail.fields.StreamField(
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
                (
                    "big_title",
                    models.TextField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Title Moving Outer",
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
            name="OurTeam",
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
                ("name", models.CharField(max_length=120)),
                ("position", models.CharField(max_length=200)),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="ourteam",
                        to="about.aboutpage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customers",
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
                ("link", models.URLField()),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="customers",
                        to="about.aboutpage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BusinessInsight",
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
                ("body", wagtail.fields.RichTextField(max_length=1000)),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="business_insight",
                        to="about.aboutpage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AboutPageFAQ",
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
                ("overview_title", models.CharField(max_length=300)),
                ("overview_detail", models.CharField(max_length=1000)),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="faq",
                        to="about.aboutpage",
                    ),
                ),
            ],
        ),
    ]
