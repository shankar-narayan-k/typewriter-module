"""
typewriter
"""

from email.utils import parseaddr
from importlib.metadata import (
    PackageNotFoundError,
    metadata,
    version,
)

# Convert import package name (acme_sdk) to distribution name (acme-sdk)
DIST_NAME = __name__.replace("_", "-")

try:
    __version__ = version(DIST_NAME)

    _meta = metadata(DIST_NAME)

    __package_name__ = _meta.get("Name", DIST_NAME)

    # PEP 621 stores authors in Author-email
    __author__, __author_email__ = parseaddr(_meta.get("Author-email", ""))

except PackageNotFoundError:
    # Package has not been installed yet
    __version__ = "0.0.0"
    __package_name__ = DIST_NAME
    __author__ = ""
    __author_email__ = ""

from .main import main, typewriter_decorator as typewriter

__all__ = [
    "__package_name__",
    "__version__",
    "__author__",
    "__author_email__",
    "main",
    "typewriter",
]
