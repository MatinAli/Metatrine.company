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
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path
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

        [('title', blocks.CharBlock())],
        null =True,
        blank =True,
        use_json_field=True,
    )

    hero_subtitle = models.CharField(

        max_length=125,
        blank=False,
        null=False,
        default="Featured Stories"
    ) 

    # return last posts published in the BlogIndexPage
    def get_recent_posts(self):

        max_count = 4

        return BlogPage.objects.all().order_by('-first_published_at')[:max_count]


    def get_context(self, request):

        context = super().get_context(request)

        posts = self.get_children().live().public().order_by("-last_published_at")

        context['posts'] = posts

        categories = BlogCategory.objects.all()

        context['categories'] = categories

        recent_posts = self.get_recent_posts()

        context['recent_posts'] = recent_posts

        return context

    content_panels = Page.content_panels + [

        FieldPanel('hero_title'),
        FieldPanel('hero_subtitle'),
    ]

class BlogTagIndexPage(Page):

    def get_context(self, request):
        
        # Filter by tag name
        tag = request.GET.get('tag')

        posts = BlogPage.objects.filter(tags__name=tag)

        categories = BlogCategory.objects.all()

        # update template context
        context = super().get_context(request)

        context = {
            
            "posts": posts,
            "categories": categories,
        }

        return context

class BlogTagPage(TaggedItemBase):

    content_object = ParentalKey(

        "BlogPage",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )

class BlogPage(RoutablePageMixin,Page):

    pub_date = models.DateTimeField(

        "Publish date",
        serialize=True,
        default=None,
    )
    
    main_image = models.ForeignKey(

        'wagtailimages.Image',
        on_delete=models.PROTECT,
        related_name='post_banner_image',
        default=None,
    )

    post_body = RichTextField(

        blank=True,
    )

    categories = ParentalManyToManyField(

        "blog.BlogCategory",
        blank=True,
    )

    tags = ClusterTaggableManager(

        through=BlogTagPage,
        blank=True,
    )

    class Meta: 

        ordering = ["pub_date","title"]

    # return last posts published in the BlogIndexPage
    def get_recent_posts(self):

        max_count = 4

        return BlogPage.objects.all().order_by('-first_published_at')[:max_count]


    def get_context(self, request):

        context = super(BlogPage, self).get_context(request)

        context["recent_posts"] = self.get_recent_posts()

        context["categories"]= BlogCategory.objects.all()

        context["tags"] = Tag.objects.all()


        return context

    content_panels = Page.content_panels + [
        
        MultiFieldPanel([
            FieldPanel("pub_date"),
            FieldPanel("tags"),
            FieldPanel("categories", widget=forms.CheckboxSelectMultiple()),
        ], heading="Post Meta Data"),

        MultiFieldPanel([
            FieldPanel("main_image"),
            FieldPanel("post_body"),
            InlinePanel("blog_page_gallery", label="Post Inline Images")
        ], heading="Post Contents"),

        InlinePanel("comments", label="Post Comments"),
    ]

class BlogPageGalleryImage(Orderable):

    content_object = ParentalKey(

        "BlogPage",
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

class Comment(models.Model):

    comment = models.TextField()
    email = models.EmailField()
    author = models.CharField(max_length=255)

    panels = [
        FieldPanel("comment"),
        FieldPanel("email"),
        FieldPanel("author"),
    ]
   
    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'
    
    class Meta:
        abstract = True

class BlogPageComments(Orderable, Comment):

    page = ParentalKey(
        "BlogPage",
        related_name="comments",
    )

