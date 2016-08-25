import json

from wagtail.wagtailadmin.rich_text import HalloRichTextArea

from .fields import SimpleDbWhitelister


class HalloWidget(HalloRichTextArea):
    config = {
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
            json.dumps(self.config)
        )

    def value_from_datadict(self, data, files, name):
        original_value = super(HalloWidget, self).value_from_datadict(data, files, name)
        if original_value is None:
            return None
        return SimpleDbWhitelister.clean(original_value)
