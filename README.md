Wagtail Commonblocks
====================

# Quickstart

Assuming you have a [Wagtail](https://wagtail.io/) project up and running:

``` $ pip install wagtailcommonblocks```

Add commonblocks to your `settings.py` in the INSTALLED_APPS section, before the core wagtail packages:

```
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

```
...
COMMONBLOCKS_HEADING = (
    ('h1', 'h1'),
    ('h2', 'h2'),
)
```

# Version history

* [0.0.2](releases/tag/0.0.2) compatible with [Wagtail 1.2](https://github.com/torchbox/wagtail/tree/v1.2)
* [0.0.1](releases/tag/0.0.1) compatible with [Wagtail 1.1](https://github.com/torchbox/wagtail/tree/v1.1)

