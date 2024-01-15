# From django 
from django.db import models
from django.core.exceptions import ValidationError
from modelcluster.models import ParentalKey
# from wagtail 
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail import blocks

# from project
from portfolio.models import PortfolioPage

# Create your models here

class HomePage(Page):

        hero_title = StreamField(
                [('title', blocks.CharBlock())],
                null = True, blank = True,
                use_json_field= True
        )

        slogan = models.CharField(blank= True, max_length=2000)

        call_to_action = StreamField(
                [('items', blocks.CharBlock())],
                null = True, blank = True,
                use_json_field= True
        )

        # portfolio below section 
        content_row = models.CharField(max_length=10000, blank=True, null=True,)
        def get_latest_portfolios(self):

                max_count = 4

                return PortfolioPage.objects.live().order_by('-date')[:max_count]  

        def get_context(self, request):

                context = super().get_context(request)

                context['latest_portfolios'] = self.get_latest_portfolios()

                return context

        content_panels = Page.content_panels + [
            FieldPanel('hero_title'),
            FieldPanel('slogan'),
            FieldPanel('content_row'),
            FieldPanel('call_to_action'),
            InlinePanel("business_statement", label= "Business Statement")
        ]

# Vision and Mission Part 
class BusinessStatement(models.Model):

    page = ParentalKey(HomePage, 
           null=True,
           blank=True,
           on_delete=models.SET_NULL,
           related_name='business_statement'
    )

    title = models.CharField( max_length= 50)

    body = RichTextField()

    panels = [
        FieldPanel('title'),
        FieldPanel('body'),
    ]