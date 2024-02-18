from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('home_title'),
        FieldPanel('home_subtitle'),
        FieldPanel('home_main_image'),
    ]
    # field for page title
    home_title = models.CharField(max_length=255, blank=False, null=True)
    # field for page subtitle
    home_subtitle = models.CharField(max_length=255, blank=False, null=True)
    # field for page image
    home_main_image = models.ImageField(upload_to='images/', blank=False, null=True)
