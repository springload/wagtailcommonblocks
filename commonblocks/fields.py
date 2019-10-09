from wagtail.core.fields import RichTextField

SIMPLERICHTEXT_FEATURES = ["link", "bold", "italic", "ol", "ul", "document-link"]


class SimpleRichTextField(RichTextField):
    """
    RichTextField with a set, limited number of features
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, features=SIMPLERICHTEXT_FEATURES, **kwargs)
