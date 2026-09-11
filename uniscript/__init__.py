"""
uniscript — Auto Unicode subscript/superscript conversion.

Public API
----------
sub(text, fallback=FallbackMode.PASSTHROUGH)     -> str
sup(text, fallback=FallbackMode.PASSTHROUGH)     -> str
render(text, fallback=FallbackMode.PASSTHROUGH)  -> str
coverage(chars, mode)                            -> CoverageReport | tuple
check(text)                                      -> dict
FallbackMode
CoverageReport
UniScriptError
GREEK_SHORTHANDS
resolve_shorthands
"""

from uniscript._core import sub, sup
from uniscript._parser import render
from uniscript._fallback import FallbackMode
from uniscript._errors import UniScriptError
from uniscript._coverage import coverage, check, CoverageReport
from uniscript._greek import GREEK_SHORTHANDS, resolve_shorthands

__version__ = "0.1.0"
__all__ = [
    "sub",
    "sup",
    "render",
    "coverage",
    "check",
    "FallbackMode",
    "CoverageReport",
    "UniScriptError",
    "GREEK_SHORTHANDS",
    "resolve_shorthands",
]

