from importlib.metadata import version

try:
    __version__ = version("earthaccess_keyring")
except Exception:
    __version__ = "9999"
