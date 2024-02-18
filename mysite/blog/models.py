from django.db import models

# Add these:
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

class BlogIndexPage(Page):

    headline = models.CharField(max_length=255, blank=False, null=True)
    intro = models.CharField(max_length=255, blank=False, null=True)
    main_image = models.ImageField(upload_to='images/', blank=False, null=True)
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('headline'),
        FieldPanel('main_image'),
    ]

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    main_image = models.ImageField(upload_to='images/', blank=False, null=True)
    tag_line = models.CharField(max_length=255, blank=False, null=True)
    blog_title = models.CharField(max_length=255, blank=False, null=True)
    author = models.CharField(max_length=255, blank=False, null=True)
    author_image = models.ImageField(upload_to='images/', blank=False, null=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('tag_line'),
        index.SearchField('blog_title'),
        index.SearchField('author'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('blog_title'),
        FieldPanel('tag_line'),
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('main_image'),
        FieldPanel('author'),
        FieldPanel('author_image'),
    ]
