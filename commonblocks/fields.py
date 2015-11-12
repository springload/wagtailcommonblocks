import json

from django.db import models

from wagtail.wagtailcore.whitelist import attribute_rule, check_url
from wagtail.wagtailcore.rich_text import DbWhitelister
from wagtail.wagtailcore.fields import RichTextArea

allow_without_attributes = attribute_rule({})


class SimpleDbWhitelister(DbWhitelister):
    """
    DbWhitelister to allow/disallow stuff on the text editor
    """
    element_rules = {
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


class SimpleRichTextArea(RichTextArea):
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
        return "makeRichTextEditable({0}, {1});".format(
            json.dumps(id_),
            json.dumps(self.hallo_plugins)
        )

    def value_from_datadict(self, data, files, name):
        original_value = super(SimpleRichTextArea, self).value_from_datadict(data, files, name)
        if original_value is None:
            return None
        return SimpleDbWhitelister.clean(original_value)


class SimpleRichTextField(models.TextField):
    """
    Textfield using .SimpleRichTextArea as widget
    """
    def formfield(self, **kwargs):
        defaults = {'widget': SimpleRichTextArea}
        defaults.update(kwargs)
        return super(SimpleRichTextField, self).formfield(**defaults)
