from django.db import models 
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail.admin.panels import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel)
from wagtail.fields import RichTextField, StreamField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField,)
from wagtail import blocks
# Create your models here.

class FormField(AbstractFormField):

    page = ParentalKey(
        'ContactPage',
        on_delete= models.CASCADE,
        related_name="form_fields"
    )
    
class ContactPage(AbstractEmailForm):

    template = 'contact/contact_page.html'

    landing_page_template = 'contact/contact_page_landing.html'

    hero_title = StreamField(
        [('block', blocks.CharBlock())],
        null = True,
        blank = True,
        use_json_field= True,
    )

    thank_you_text = RichTextField(
        blank= True,
    )

    information = StreamField([
        ('office', blocks.StructBlock([
            ('city_country', blocks.CharBlock()),
            ('address', blocks.CharBlock()),
            ('email', blocks.EmailBlock()),
            ('telephone_number', blocks.CharBlock()),
        ])),
    ], use_json_field= True, default = None)


    def get_context(self, request):
        return super().get_context(request)

    content_panels = AbstractEmailForm.content_panels +[

        FieldPanel('hero_title'),
        FieldPanel('information'),
        InlinePanel('form_fields',label = 'Form Field'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname = "col6"),
                FieldPanel('to_address', classname = "col6"),
            ]),
            FieldPanel('subject'),
        ],"Email"),
    ]



