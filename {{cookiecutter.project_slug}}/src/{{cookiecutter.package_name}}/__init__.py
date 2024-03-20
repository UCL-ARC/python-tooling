"""{{cookiecutter.package_name}} package."""
from ._version import __version__  # noqa: F401


def example_function(argument: str, keyword_argument: str = "default") -> str:
    """
    Concatenate string arguments - an example function docstring.

    :param argument: An argument.
    :param keyword_argument: A keyword argument with a default value.
    :returns: The concatenation of `argument` and `keyword_argument`.
    """
    return argument + keyword_argument
