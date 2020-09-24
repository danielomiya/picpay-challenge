"""
Utils functions

Author: Daniel Omiya
"""

def sanitize(value):
    """
    Sanitizes values to be serialized as CSV

    Args:
        value (any): any value to be treated

    Returns:
        str: stringify'ed value
    """
    if isinstance(value, str):
        return '"' + value.replace('"', '\\"') + '"'
    return str(value)
