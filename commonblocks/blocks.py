from django import forms
from django.apps import apps
from django.utils.functional import cached_property
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import RichTextBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock

from commonblocks.fields import SimpleRichTextArea
from commonblocks.simple_rich_text import SimpleRichText


DEFAULT_COMMONBLOCKS_HEADING = (
    ('h2', 'h2'),
    ('h3', 'h3'),
    ('h4', 'h4'),
    ('h5', 'h5'),
)

TARGETS = (
    ('', 'Open link in'),
    ('_self', 'Same window'),
    ('_blank', 'New window'),
)

HEADINGS = (('', _('Choose your heading')), ) + getattr(settings, 'COMMONBLOCKS_HEADINGS', DEFAULT_COMMONBLOCKS_HEADING)


class CommonPageChooserBlock(blocks.PageChooserBlock):
    """
    Custom PageChooser that allows filter by models classname
    """
    def __init__(self, can_choose_root=False, page_class='Page', app='wagtail.wagtailcore.models', **kwargs):
        self.page_class = page_class
        self.app = app
        super(SpecificPageChooserBlock, self).__init__(can_choose_root, **kwargs)

    @cached_property
    def target_model(self):
        page_class = apps.get_model(self.app, self.page_class)
        return page_class


class SimpleRichTextBlock(RichTextBlock):
    """
    Custom block inheriting from Wagtail's original one but replacing the RichText by a SimpleRichText
    """
    def get_default(self):
        if isinstance(self.meta.default, SimpleRichText):
            return self.meta.default
        else:
            return SimpleRichText(self.meta.default)

    def to_python(self, value):
        # convert a source-HTML string from the JSONish representation
        # to a SimpleRichText object
        return SimpleRichText(value)

    def value_from_form(self, value):
        # RichTextArea returns a source-HTML string; concert to a SimpleRichText object
        return SimpleRichText(value)

    @cached_property
    def field(self):
        return forms.CharField(widget=SimpleRichTextArea, **self.field_options)

    class Meta:
        icon = 'bold'


class CommonImageBlock(blocks.StructBlock):
    """
    Block for single images with all necessary attributes such as alternative title, caption and so on.
    """
    image = ImageChooserBlock(required=True)
    alternative_title = blocks.CharBlock(required=False)
    caption = SimpleRichTextBlock(required=False)
    attribution = blocks.CharBlock(required=False)
    license_url = blocks.URLBlock(required=False)
    license_name = blocks.CharBlock(required=False)

    @property
    def get_title(self):
        if self.alternative_title:
            return self.alternative_title
        else:
            self.image.title

    class Meta:
        icon = 'image'
        template = 'commonblocks/image.html'


class CommonQuoteBlock(blocks.StructBlock):
    """
    Block for rich text quotes
    """
    quote = SimpleRichTextBlock(required=True)
    author = blocks.CharBlock(required=False)
    author_title = blocks.CharBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = 'openquote'
        template = 'commonblocks/quote.html'


class CommonHeadingBlock(blocks.StructBlock):
    """
    Heading Block
    """
    size = blocks.ChoiceBlock(required=True, choices=HEADINGS, help_text=_('Heading Size'))
    title = blocks.CharBlock(required=True)
    subtitle = blocks.CharBlock(required=False)

    class Meta:
        icon = 'title'
        template = 'commonblocks/heading.html'


class CommonVideoBlock(blocks.StructBlock):
    """
    Video block
    """
    video = EmbedBlock(
        required=True,
        help_text=_('Paste your video URL ie: https://www.youtube.com/watch?v=05GKqTZGRXU')
    )
    caption = SimpleRichTextBlock(required=False)

    class Meta:
        icon = 'media'
        template = 'commonblocks/video.html'


class CommonInternalLink(blocks.StructBlock):
    """
    Single Internal link block
    """
    link = blocks.PageChooserBlock(required=True)
    title = blocks.CharBlock(required=False)

    @property
    def get_title(self):
        if self.title:
            return self.title
        else:
            self.link.title

    class Meta:
        template = 'commonblocks/internal_link.html'
        icon = 'link'


class CommonExternalLink(blocks.StructBlock):
    """
    Single External Tile Block
    """
    link = blocks.URLBlock(required=True)
    title = blocks.CharBlock(required=True)
    target = blocks.ChoiceBlock(
        required=True,
        choices=TARGETS,
        default='_self',
        help_text=_('Open link in')
    )

    class Meta:
        template = 'commonblocks/external_link.html'
        icon = 'site'


class CommonLinksBlock(blocks.StreamBlock):
    """
    A collection of Link Blocks, Orderable
    """
    internal_link = CommonInternalLink(label=_('Internal page'))
    external_link = CommonExternalLink(label=_('External Page'))

    class Meta:
        template = 'commonblocks/links.html'
        icon = 'link'
