"""Basic utils for work with LaTeX documents."""


from datetime import date as datum
from typing import Any, Optional
import sys
from os import path


def get_dir() -> str:
    """Returns directory where main file has been executed.

    Returns:
        str: Directory name where is main file
    """
    return str(path.dirname(str(sys.modules['__main__'].__file__)))


def get_path() -> str:
    """Returns path to main file.

    Returns:
        str: Path to main file
    """
    return str(path.abspath(str(sys.modules['__main__'].__file__)))


def command(comm: str, main: Optional[str] = None, *params) -> str:
    """Template for creating commands.

    If main is None, than return '\\command'.
    If main is not none, but any optional parameter given, than return '\\command{main}'
    If main and optional parameters given, than return '\\command[param1, param2, ...]{main}'

    Args:
        comm (str): Name of command
        main (str): Main parameter of command, defaults None
        *params (str): Optional parameters of command

    Returns:
        str: string of given command by given parameters.
    """
    if main is None:
        return f"\\{comm}"
    elif params:
        return f"\\{comm}[{', '.join(params)}]{{{main}}}"
    else:
        return f"\\{comm}{{{main}}}"


def doublecommand(comm: str, main: str, second: str) -> str:
    """Template for creating doublecommands.

    Commands lokks like this \\comm{main} {second}

    Args:
        comm (str): Name of command
        main (str): First parameter
        second (str): Second parameter

    Returns:
        str: string of given command by given parameters.
    """
    return f"\\{comm}{{{main}}} {{{second}}}"


class PreambleProperty:
    """Template for preamble attribute properties."""

    def __init__(self, name: str) -> None:
        """Initialize given attribute by name.

        Args:
            name (str): Name of attribute.
        """
        self.name = f'_{name}'

    def __get__(self, obj) -> Optional[str]:
        """Getter template.

        Args:
            obj: Object that use this template for given property.

        Returns:
            str: String in form of TeX command for this attribute.
        """
        value = getattr(obj, self.name)
        return command(self.name[1:], str(value)) if value is not None else None

    def __set__(self, obj, value) -> None:
        """Setter template.

        Args:
            obj: Object that use this template for given property.
            value: New value of attribute.
        """
        setattr(obj, self.name, value)
