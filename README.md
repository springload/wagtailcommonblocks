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

## Development

### Releases

- Make a new branch for the release of the new version.
- Update the [CHANGELOG](https://github.com/springload/wagtailcommonblocks/CHANGELOG.md).
- Update the version number in `setup.py`, following semver.
- Make a PR and squash merge it.
- Back on master with the PR merged, use `make publish` (confirm, and enter your password).
- Finally, go to GitHub and create a release and a tag for the new version.
- Done!
