from django import template
from django.utils.safestring import mark_safe

from commonblocks.simple_rich_text import SimpleRichText

try:
    from wagtail.core.rich_text import expand_db_html
except ImportError:
    from wagtail.wagtailcore.rich_text import expand_db_html


register = template.Library()


@register.filter
def simplerichtext(value):
    """
    Simple richtext filter to avoid the wrapping <div class='richtext'></div> markup
    """
    if isinstance(value, SimpleRichText):
        html = value
    elif value is None:
        html = ''
    else:
        html = expand_db_html(value)

    return mark_safe(html)
