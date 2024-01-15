# From django
from django.db import models
from modelcluster.fields import ParentalKey

# From wagtail 
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
# from wagtail.fields import RichTextField
from wagtail.images.models import Image
from wagtail import blocks

# Create your models here.
class AboutPage(Page):
    # template = 'about/about_page.html'

    services = RichTextField(max_length=600)

    services_item = StreamField([('block', blocks.CharBlock())],
                    null = True, blank = True, use_json_field= True)

    hero_title  = StreamField([('block', blocks.CharBlock())],
                  null = True, blank = True, use_json_field= True)

    # about-page title-moving-outer
    big_title = models.TextField( blank= True, null = True,
                max_length=250,
                verbose_name="Title Moving Outer" )

    content_row = models.CharField(max_length=10000, blank=True, null=True,)

    
    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('services'),
        FieldPanel('services_item'),
        FieldPanel('big_title'),
        InlinePanel('faq', label="Frequently Asked Questions"),
        InlinePanel('ourteam', label="Our Team"),
        InlinePanel('customers', label="Our Customers"),
        FieldPanel('content_row'),
        InlinePanel('business_insight', label="Business Insights"),
        InlinePanel('snap_shot', label="Snap Shots"),
    ]

class AboutPageFAQ(models.Model):

    page = ParentalKey(AboutPage, related_name='faq')

    overview_title = models.CharField(max_length=300)

    overview_detail = models.CharField(max_length=1000)

    panels = [
        FieldPanel('overview_title'),
        FieldPanel('overview_detail'),
    ]

class OurTeam(models.Model):

    page = ParentalKey(AboutPage, 
           null=True,
           blank=True,
           on_delete=models.SET_NULL,
           related_name='ourteam'
    )

    name = models.CharField(max_length=120)
    
    position = models.CharField(max_length= 200)

    image = models.ForeignKey(
            Image,
            on_delete=models.CASCADE,
            related_name='+',
            null=True,
            blank=True
    )

    panels =[
        FieldPanel('name'),
        FieldPanel('position'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return self.name

class Customers(models.Model):

    page = ParentalKey(AboutPage, 
           null=True,
           blank=True,
           on_delete=models.SET_NULL,
           related_name='customers')

    link = models.URLField(max_length=200)

    image = models.ForeignKey(
            Image,
            on_delete=models.CASCADE,
            related_name='+',
            null=True,
            blank=True
    )

    panels =[
        FieldPanel('link'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return self.link 

# About-Page Agency snapshot section
class SnapShot(models.Model):

    page = ParentalKey(AboutPage, 
           null=True,
           blank=True,
           on_delete=models.SET_NULL,
           related_name='snap_shot')


    title = models.CharField(max_length= 100, blank=True, null=True)

    count_field = models.IntegerField(null=True, blank=True, )

    panels = [
        FieldPanel('title'),
        FieldPanel('count_field')
    ]

# The Challenge and The Approch part
class BusinessInsight(models.Model):

    page = ParentalKey(AboutPage, 
           null=True,
           blank=True,
           on_delete=models.SET_NULL,
           related_name='business_insight'
    )

    title = models.CharField( max_length= 50)

    body = RichTextField( max_length= 1000)

    panels = [
        FieldPanel('title'),
        FieldPanel('body'),
    ]


