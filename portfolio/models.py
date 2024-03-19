# From django 
from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from django import forms
from django.apps import apps
from django.db.models import Count
# From wagtail
from wagtail.models import Page, Orderable, Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, MultipleChooserPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.snippets.models import register_snippet
from wagtail import blocks
# Create your models here.

@register_snippet
class PortfolioCategory(models.Model):

    name = models.CharField(

        max_length=255,
    )

    slug = models.SlugField(

        max_length=255,
        verbose_name="slug",
        allow_unicode=True,
        help_text="You can define a slug to identify projects by this category",
        default="corporate"

    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    class Meta:

        verbose_name = "Portfolio Category"
        verbose_name_plural = 'Portfolio Categories' 
        ordering = ["name"]

def __str__(self):

    return self.name   

@register_snippet       
class PortfolioIndustryCategory(models.Model):

    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
    ]
    def __str__(self):

        return self.name

    class Meta:

        verbose_name_plural = 'portfolio industry'

@register_snippet       
class PortfolioTechnologyCategory(models.Model):

    name = models.CharField(max_length=255)

    panels = [

        FieldPanel('name'),
    ]
    def __str__(self):

        return self.name

    class Meta:

        verbose_name_plural = 'portfolio technology'

class PortfolioIndexPage(Page):

    template = 'portfolio/portfolio_index_page.html'

    intro = RichTextField(blank=True)

    hero_title = StreamField(

        [('title', blocks.CharBlock())],
        null = True, 
        blank = True,
        use_json_field= True,
    )

    def get_context(self, request):

        context = super().get_context(request)

        posts = self.get_children().live().public().order_by('-first_published_at')

        categories = PortfolioCategory.objects.all()

        context['categories'] = categories

        context['posts'] = posts

        return context

    # get slogan from homepage 
    def get_homepage_slogan(self):

        HomePage = apps.get_model('home','HomePage')

        homepage= HomePage.objects.first()

        return homepage.slogan if homepage else None

    content_panels = Page.content_panels + [

        FieldPanel('intro'),
        FieldPanel('hero_title'),
    ]
          
class PortfolioPage(Page):

    template = 'portfolio/portfolio_page.html'

    date = models.DateField("Post Date")

    introduction = models.CharField(
        blank= True,
        max_length=10000
    )

    body = RichTextField(

        blank= True,
        max_length=10000,
    )

    project_link = models.URLField(

        max_length=200,
    )

    # Projects Category
    categories = ParentalManyToManyField(

        'portfolio.PortfolioCategory',
         blank=True,
    )

    # Industries Category
    industries = ParentalManyToManyField(

        'portfolio.PortfolioIndustryCategory',
         blank = True,
    )

    # Technology Category
    technologies = ParentalManyToManyField(

        'portfolio.PortfolioTechnologyCategory',
         blank = True,
    )

    banner_image = models.ForeignKey(

        'wagtailimages.Image',
        null= True,
        blank= True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_recent_projects(self):

        max_count = 1

        return PortfolioPage.objects.all().order_by('-title')[:max_count]

    def get_context(self, request):

        context = super(PortfolioPage,self).get_context(request)

        context['recents'] = self.get_recent_projects()

        return context 

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            FieldPanel('industries', widget=forms.CheckboxSelectMultiple),
            FieldPanel('technologies', widget=forms.CheckboxSelectMultiple),
        ],heading = 'Portfolio Information'),

        FieldPanel('banner_image'),
        FieldPanel('introduction'),
        FieldPanel('body'),
        FieldPanel('project_link'),
        MultipleChooserPanel(
            'portfolio_gallery',
            label = 'portfolio gallery',
            chooser_field_name= 'image'
            ),
    ] 

 # Portfolio Projects Gallery  
class Gallery(Orderable):

    page = ParentalKey(

        PortfolioPage,
        on_delete=models.CASCADE,
        related_name='portfolio_gallery',
    )

    image = models.ForeignKey(

        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+',
    )
    caption = models.CharField(

        blank=True,
        max_length=250,
    )

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]