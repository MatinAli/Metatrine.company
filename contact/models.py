from django.db import models 
from django.core.validators import RegexValidator
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField,)
from wagtail.contrib.forms.forms import FormBuilder
from wagtail import blocks
# Create your models here.


class ContactPage(Page):
    template = 'contact/contact_page.html'

    hero_title = StreamField([('block', blocks.CharBlock())],
    null = True,
    blank = True,
    use_json_field= True,
    )
    # email = models.CharField(max_length=250, default='info@metatrin.com')
    # location = models.CharField(max_length=100, default='Istanbul')
    # address_details = models.CharField(blank=True, default=None, max_length=500)
    # telephone_number = models.CharField(max_length=17, blank=True)
    # Contact Information Fields 
    information = StreamField(
        [
            ('city_country', blocks.CharBlock()),
            ('address', blocks.RichTextBlock()),
            ('email', blocks.EmailBlock()),
            ('telephone_number', blocks.CharBlock()),
        ], use_json_field= True, default = None,
    )

    def get_context(self, request):
        return super().get_context(request)

    content_panels = Page.content_panels +[
        FieldPanel('hero_title'),
        FieldPanel('information'),
    ]




