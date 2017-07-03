from django.utils.html import format_html, format_html_join
from django.conf import settings

from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_js')
def editor_js():
    js_files = [
        'commonblocks/js/hallo-bootstrap.js',
    ]

    return format_html_join(
        '\n',
        '<script src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )
