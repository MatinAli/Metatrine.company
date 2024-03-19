from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0092_query_searchpromotion_querydailyhits"),
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
    ]

    operations = [
        migrations.CreateModel(
            name="PortfolioCategory",
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
                ("name", models.CharField(max_length=255)),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        default="corporate",
                        help_text="You can define a slug to identify projects by this category",
                        max_length=255,
                        verbose_name="slug",
                    ),
                ),
            ],
            options={
                "verbose_name": "Portfolio Category",
                "verbose_name_plural": "Portfolio Categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="PortfolioIndexPage",
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
                ("intro", wagtail.fields.RichTextField(blank=True)),
                (
                    "hero_title",
                    wagtail.fields.StreamField(

                        [("title", wagtail.blocks.CharBlock())],
                        blank=True,
                        null=True,
                        use_json_field=True,

                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="PortfolioIndustryCategory",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "portfolio industry",
            },
        ),
        migrations.CreateModel(
            name="PortfolioTechnologyCategory",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "portfolio technology",
            },
        ),
        migrations.CreateModel(
            name="PortfolioPage",
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
                ("date", models.DateField(verbose_name="Post Date")),
                ("introduction", models.CharField(blank=True, max_length=10000)),
                ("body", wagtail.fields.RichTextField(blank=True, max_length=10000)),
                ("project_link", models.URLField()),
                (
                    "banner_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "categories",
                    modelcluster.fields.ParentalManyToManyField(
                        blank=True, to="portfolio.portfoliocategory"
                    ),
                ),
                (
                    "industries",
                    modelcluster.fields.ParentalManyToManyField(
                        blank=True, to="portfolio.portfolioindustrycategory"
                    ),
                ),
                (
                    "technologies",
                    modelcluster.fields.ParentalManyToManyField(
                        blank=True, to="portfolio.portfoliotechnologycategory"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="Gallery",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("caption", models.CharField(blank=True, max_length=250)),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="portfolio_gallery",
                        to="portfolio.portfoliopage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
