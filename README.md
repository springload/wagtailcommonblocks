Wagtail Commonblocks
====================

# Quickstart

Assuming you have a [Wagtail](https://wagtail.io/) project up and running:

``` $ pip install commonblocks```

Add commonblocks to your `settings.py` in the INSTALLED_APPS section:

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
