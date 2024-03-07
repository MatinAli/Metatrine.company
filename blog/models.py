# From Django
from django.db import models
from django import forms

# From Wagtail 
from wagtail.models import Page, Orderable
from wagtail.fields import (
    RichTextField,
    StreamField,
)
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail import blocks
from wagtail.snippets.models import register_snippet
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField,
)
# From other packages
from taggit.models import TaggedItemBase, Tag 
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey, ParentalManyToManyField
# Create your models here.

class BlogCategory(models.Model):

    name = models.CharField(max_length=125)

    slug = models.SlugField(

        max_length=255,
        verbose_name ="Slug",
        allow_unicode=True,
        help_text="You can define a slug to identify posts by this category",
    )
    
    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    # a meta class of a class that defines how a class behaves.
    class Meta:
        verbose_name = "‌Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__(self):

        return self.name

@register_snippet(BlogCategory)

class BlogIndexPage(Page):
    
    hero_title  = StreamField(

        [('block', blocks.CharBlock())],
        null =True,
        blank =True,
        use_json_field=True,
    )

    hero_subtilte = models.CharField(

        max_length=125,
        blank=False,
        null=False,
        default="Featured Stories"
    ) 

    def get_context(self, request):

        context = super().get_context(request)

        posts = self.get_children().live().public().order_by("-last_published")

        context['posts'] = posts

        return context

    content_panels = Page.content_panels + [

        FieldPanel('hero_title'),
        FieldPanel('hero_subtilte'),
    ]

class BlogTagIndexPage(Page):

    def get_context(self, request):
        
        # Filter by tag name
        tag = request.GET.get('tag')

        posts = BlogPage.object.filter(tags__name=tag)

        # update template context
        context = super().get_context(request)

        context['context'] = context

        return context

class BlogTagPage(TaggedItemBase):

    content_object = ParentalKey(

        "BlogPage",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )

class BlogPage(Page):

    pub_date = models.DateTimeField(

        "Publish date",
        serialize=True,
        default=None,
    )
    
    post_title = models.CharField(

        max_length=250,
        help_text="Post Title",
        default=None,
    ) 

    main_image = models.ForeignKey(

        'wagtailimages.Image',
        on_delete=models.PROTECT,
        related_name='post_banner_image',
        default=None,
    )

    main_header =models.CharField(

        max_length=250,
        help_text="Post Main Heading",
        default="Image Above Heading"
    )

    categories = ParentalManyToManyField("blog.BlogCategory", blank=True)

    tags = ClusterTaggableManager(

        through=BlogTagPage,
        blank=True,
    )

    class Meta: 

        ordering = ["pub_date","post_title"]

    # Post Navigation Function for getting next or previous post
    def next_post(self):
        if self.get_next_siblings():
            return self.get_next_sibling().url()
        else: 
            return self.get_siblings().first().url

    def prev_post(self):
        if get_prev_siblings():
            return self.get_prev_sibling().url
        else: 
            return self.get_siblings().last().url

    def get_recent_comments(self):

        max_count = 4

        return BlogComment.objects.all().order_by('-date')[:max_count]

    def get_recent_posts(self):

        max_count = 4
        return BlogPage.objects.all().order_by('-date')[:max_count]

    def get_context(self, request):

        context = supuer(BlogPage, self).get_context(request)

        context["categories"]= BlogCategory.objects.all()

        context["tags"] = Tag.objects.all()

        context['recent_posts'] = self.get_recent_posts()

        context['recent_comments'] = self.get_recent_comments()

        return context

    content_panels = Page.content_panels + [
        
        MultiFieldPanel([
            FieldPanel("pub_date"),
            FieldPanel("tags"),
            FieldPanel("categories", widget=forms.CheckboxSelectMultiple()),
        ], heading="Post Meta Data"),

        MultiFieldPanel([
            FieldPanel("post_title"),
            FieldPanel("main_image"),
            FieldPanel("main_header"),
            InlinePanel("blog_page_gallery", label="Post Inline Images")
        ], heading="Post Contents"),
    ]

class BlogPageGalleryImage(Orderable):
    content_object = ParentalKey(

        "BLogPage",
        related_name="blog_page_gallery",
        on_delete=models.CASCADE,
    )

    inline_image = models.ForeignKey(

        "wagtailimages.Image",
        on_delete= models.CASCADE,
        help_text="Posts Inline Images",
    )

    image_caption = models.CharField(

        max_length= 125,
        verbose_name="Caption",
        blank=True,
    )

    panel = [

        FieldPanel("inline_image"),
        FieldPanel("image_caption"),
    ]