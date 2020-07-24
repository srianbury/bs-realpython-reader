import importlib_resources as _resources
try:
    from configparser import ConfigParser as _ConfigParser
except ImportError:  # Python 2
    from ConfigParser import ConfigParser as _ConfigParser

# Version of realpython-reader package
__version__ = "1.0.1"

# Read URL of feed from config file
_cfg = _ConfigParser()
with _resources.path("reader", "config.cfg") as _path:
    _cfg.read(str(_path))
URL = _cfg.get("feed", "url")
