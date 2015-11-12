from django import template
from django.utils.safestring import mark_safe

from wagtail.wagtailcore.rich_text import expand_db_html
from commonblocks.simple_rich_text import SimpleRichText

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
