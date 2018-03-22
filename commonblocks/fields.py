import json

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models
from django.forms import Media

import wagtail

try:
    from wagtail.admin.rich_text import HalloRichTextArea
    from wagtail.admin.rich_text.converters.editor_html import DbWhitelister
    from wagtail.core.whitelist import attribute_rule, check_url
except ImportError:
    from wagtail.wagtailadmin.rich_text import HalloRichTextArea
    from wagtail.wagtailcore.rich_text import DbWhitelister
    from wagtail.wagtailcore.whitelist import attribute_rule, check_url


allow_without_attributes = attribute_rule({})
ELEMENT_RULES = {
    '[document]': allow_without_attributes,
    'a': attribute_rule({'href': check_url, 'id': True, 'linktype': True}),
    'p': allow_without_attributes,
    'b': allow_without_attributes,
    'i': allow_without_attributes,
    'u': allow_without_attributes,
    'ul': allow_without_attributes,
    'ol': allow_without_attributes,
    'li': allow_without_attributes,
}


if wagtail.VERSION >= (2,):
    class SimpleDbWhitelister(DbWhitelister):
        """
        DbWhitelister to allow/disallow stuff on the text editor
        """

        def __init__(self, converter_rules=None):
            super(SimpleDbWhitelister, self).__init__(converter_rules or [])
            self.element_rules = ELEMENT_RULES

else:
    class SimpleDbWhitelister(DbWhitelister):
        """
        DbWhitelister to allow/disallow stuff on the text editor
        """
        element_rules = ELEMENT_RULES


class SimpleRichTextArea(HalloRichTextArea):
    """
    Customised RichTextArea
    """
    hallo_plugins = {
        'halloheadings': {
            'formatBlocks': ['p']
        },
        'halloformat': {
            'formattings': {
                "bold": True,
                "italic": True,
            },
        },
        'hallowagtaildoclink': {},
        'hallolists': {
            "lists": {
                "ordered": True,
                "unordered": True
            }
        },
        'hallowagtaillink': {},
        'hallorequireparagraphs': {},
        'hallocleanhtml': {
            'format': False,
            'removeTags': ['span', 'div', 'table', 'strong'],
            'allowedTags': ['a', 'p', 'i', 'b'],
            'removeAttrs': ['class', 'style'],
            'allowedAttributes': [
                ['a', ['href', 'target', 'id', 'linktype']]
            ]
        }
    }

    def render_js_init(self, id_, name, value):
        return "makeHalloSimpleRichTextEditable({0}, {1});".format(
            json.dumps(id_),
            json.dumps(self.hallo_plugins)
        )

    def value_from_datadict(self, data, files, name):
        original_value = super(SimpleRichTextArea, self).value_from_datadict(data, files, name)
        if original_value is None:
            return None

        if wagtail.VERSION >= (2,):
            return SimpleDbWhitelister().clean(original_value)
        else:
            return SimpleDbWhitelister.clean(original_value)

    @property
    def media(self):
        base_media = super(SimpleRichTextArea, self).media
        custom_media = Media(js=[
            static('commonblocks/js/vendor/jquery.htmlClean.min.js'),
            static('commonblocks/js/vendor/rangy-selectionsaverestore.js'),
            static('commonblocks/js/hallo-bootstrap.js'),
        ])
        return base_media + custom_media


class SimpleRichTextField(models.TextField):
    """
    Textfield using .SimpleRichTextArea as widget
    """
    def formfield(self, **kwargs):
        defaults = {'widget': SimpleRichTextArea}
        defaults.update(kwargs)
        return super(SimpleRichTextField, self).formfield(**defaults)
