# Generated by Django 4.2.8 on 2024-03-19 23:34

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.blocks
import wagtail.contrib.routable_page.models
import wagtail.fields


class Migration(migrations.Migration):
    initial = True

    # dependencies = [
    #     ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
    #     # (
    #     #     "taggit",
    #     #     "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",),
    #     ("wagtailcore", "0092_query_searchpromotion_querydailyhits"),
    # ]

    operations = [
        migrations.CreateModel(
            name="BlogCategory",
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
                ("name", models.CharField(max_length=125)),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="You can define a slug to identify posts by this category",
                        max_length=255,
                        verbose_name="Slug",
                    ),
                ),
            ],
            options={
                "verbose_name": "\u200cBlog Category",
                "verbose_name_plural": "Blog Categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="BlogIndexPage",
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
                (
                    "hero_subtitle",
                    models.CharField(default="Featured Stories", max_length=125),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="BlogPage",
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
                    "pub_date",
                    models.DateTimeField(default=None, verbose_name="Publish date"),
                ),
                ("post_body", wagtail.fields.RichTextField(blank=True)),
                (
                    "categories",
                    modelcluster.fields.ParentalManyToManyField(
                        blank=True, to="blog.blogcategory"
                    ),
                ),
                (
                    "main_image",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="post_banner_image",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "ordering": ["pub_date", "title"],
            },
            bases=(
                wagtail.contrib.routable_page.models.RoutablePageMixin,
                "wagtailcore.page",
            ),
        ),
        migrations.CreateModel(
            name="BlogTagIndexPage",
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
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="BlogTagPage",
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
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="blog.blogpage",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_items",
                        to="taggit.tag",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BlogPageGalleryImage",
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
                (
                    "image_caption",
                    models.CharField(
                        blank=True, max_length=125, verbose_name="Caption"
                    ),
                ),
                (
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_page_gallery",
                        to="blog.blogpage",
                    ),
                ),
                (
                    "inline_image",
                    models.ForeignKey(
                        help_text="Posts Inline Images",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BlogPageComments",
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
                ("comment", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("author", models.CharField(max_length=255)),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.blogpage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="blogpage",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="blog.BlogTagPage",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
