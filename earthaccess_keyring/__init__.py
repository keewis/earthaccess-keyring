from importlib.metadata import version

from earthaccess_keyring import patch  # noqa: F401

try:
    __version__ = version("earthaccess_keyring")
except Exception:
    __version__ = "9999"
