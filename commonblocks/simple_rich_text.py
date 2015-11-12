from django.utils.safestring import mark_safe
from django.utils.encoding import python_2_unicode_compatible

from wagtail.wagtailcore.rich_text import RichText, expand_db_html


@python_2_unicode_compatible
class SimpleRichText(RichText):
    """
    A custom simple RichText to avoid the <div class='richtext'></div>
    """

    def __str__(self):
        return mark_safe(expand_db_html(self.source))
