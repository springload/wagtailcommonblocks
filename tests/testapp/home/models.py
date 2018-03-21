from __future__ import absolute_import, unicode_literals

from commonblocks import blocks, fields

try:
    from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
    from wagtail.core.models import Page
    from wagtail.core.fields import StreamField
except ImportError:
    from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
    from wagtail.wagtailcore.models import Page
    from wagtail.wagtailcore.fields import StreamField


class TestPage(Page):
    text_field = fields.SimpleRichTextField()
    body_blocks = StreamField([
        ('text', blocks.SimpleRichTextBlock()),
        ('quote', blocks.CommonQuoteBlock()),
        ('image', blocks.CommonImageBlock()),
        ('heading', blocks.CommonHeadingBlock()),
        ('video', blocks.CommonVideoBlock()),
        ('internal', blocks.CommonInternalLink()),
        ('external', blocks.CommonExternalLink()),
        ('links', blocks.CommonLinksBlock()),
        ('page', blocks.CommonPageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('text_field'),
        StreamFieldPanel('body_blocks'),
    ]
