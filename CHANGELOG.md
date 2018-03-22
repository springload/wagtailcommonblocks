# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

...

## [0.1] - 2018-03-22

### Fixed

- Compatibility with Wagtail 2.0

### Removed

- Compatibility with Wagtail prior 1.8

### Deprecated

- Use Wagtail's builtin `PageChooserBlock` instead of `CommonPageChooserBlock`
```diff
- CommonPageChooserBlock(app='my_app', page_class='MyModel')
+ PageChooserBlock(target_model='my_app.MyModel')
```

### Upgrade consideration

- Hold off if you're using `SimpleRichTextBlock` or `SimpleRichTextField`, see #8 for more information

## [0.0.3] - 2017-07-04

### Fixed

- Compatibility with Wagtail 1.5

## [0.0.2] - 2016-01-27

### Fixed

- Compatibility with Wagtail 1.2

## [0.0.1] - 2015-11-25

Initial Release

[Unreleased]: https://github.com/springload/wagtailcommonblocks/compare/0.1...HEAD
[0.1]: https://github.com/springload/wagtailcommonblocks/compare/0.0.3...0.1
[0.0.3]: https://github.com/springload/wagtailcommonblocks/compare/0.0.2...0.0.3
[0.0.2]: https://github.com/springload/wagtailcommonblocks/compare/0.0.1...0.0.2
[0.0.1]: https://github.com/springload/wagtailcommonblocks/compare/a9159c46ab8b6cf31213b9c97730fc5fd40c309c...0.0.1
