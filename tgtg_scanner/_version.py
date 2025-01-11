import importlib.metadata

PACKAGE_NAME = "tgtg_scanner"

metadata = importlib.metadata.metadata(PACKAGE_NAME)

__title__ = metadata["Name"]
__description__ = metadata["Summary"]
__version__ = importlib.metadata.version(PACKAGE_NAME)
__author__ = metadata["Author"]
__author_email__ = metadata["Author-email"]
__license__ = metadata["License"]
__url__ = metadata["Project-URL"].split(", ")[1]
