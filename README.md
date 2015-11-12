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

* SpecificPageChooserBlock
* SimpleRichTextBlock
* FullImageBlock
* QuoteBlock
* HeadingBlock
* VideoBlock
* InternalLink
* ExternalLink
* InternalButtonLink
* ExternalButtonLink
* LinksBlock

You can override the headings of the `HeadingBlock` block:

```
...
COMMONBLOCKS_HEADING = (
    ('h1', 'h1'),
    ('h2', 'h2'),
)
```
