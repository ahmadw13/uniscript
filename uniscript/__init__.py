"""
uniscript — Auto Unicode subscript/superscript conversion.

Public API
----------
sub(text, fallback=FallbackMode.PASSTHROUGH)  -> str
sup(text, fallback=FallbackMode.PASSTHROUGH)  -> str
render(text, fallback=FallbackMode.PASSTHROUGH) -> str
FallbackMode
UniScriptError
"""

from uniscript._core import sub, sup
from uniscript._parser import render
from uniscript._fallback import FallbackMode
from uniscript._errors import UniScriptError

__version__ = "0.1.0"
__all__ = ["sub", "sup", "render", "FallbackMode", "UniScriptError"]
