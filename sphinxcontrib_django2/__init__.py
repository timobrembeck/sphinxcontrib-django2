"""
This is a sphinx extension which improves the documentation of Django apps.
"""
__version__ = "1.6"


def setup(app):
    """
    Allow this module to be used as sphinx extension.

    Setup the upstream extension sphinxcontrib-django.

    :param app: The Sphinx application object
    :type app: ~sphinx.application.Sphinx
    """

    # Load upstream extension
    app.setup_extension("sphinxcontrib_django")

    return {
        "version:": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
