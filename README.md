# wagtailcommonblocks [![PyPI](https://img.shields.io/pypi/v/wagtailcommonblocks.svg)](https://pypi.python.org/pypi/wagtailcommonblocks)

> Common StreamField blocks for Wagtail.

*Check out [Awesome Wagtail](https://github.com/springload/awesome-wagtail) for more awesome packages and resources from the Wagtail community.*

## Quickstart

Assuming you have a [Wagtail](https://wagtail.io/) project up and running:

```sh
pip install wagtailcommonblocks
```

Add commonblocks to your `settings.py` in the INSTALLED_APPS section, before the core wagtail packages:

```python
...
    'commonblocks',
    'wagtail.contrib.wagtailsitemaps',
...
```
# Available blocks

* CommonPageChooserBlock
* SimpleRichTextBlock
* CommonImageBlock
* CommonQuoteBlock
* CommonHeadingBlock
* CommonVideoBlock
* CommonInternalLink
* CommonExternalLink
* CommonLinksBlock

You can override the headings of the `CommonHeadingBlock` block:

```python
...
COMMONBLOCKS_HEADING = (
    ('h1', 'h1'),
    ('h2', 'h2'),
)
```

# Version history

* [0.0.3](https://github.com/springload/wagtailblocks/tree/0.0.2) compatible with [Wagtail 1.5](https://github.com/torchbox/wagtail/tree/v1.5)
* [0.0.2](https://github.com/springload/wagtailblocks/tree/0.0.2) compatible with [Wagtail 1.2](https://github.com/torchbox/wagtail/tree/v1.2)
* [0.0.1](https://github.com/springload/wagtailblocks/tree/0.0.1) compatible with [Wagtail 1.1](https://github.com/torchbox/wagtail/tree/v1.1)

