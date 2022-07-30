"""Tables and lists utilities and support for pandas dataframe."""

from typing import Any, Optional, Union
from collections.abc import Container, Sequence
from typing_extensions import Self
from mff_pytex.utils import command, doublecommand
from mff_pytex.structure import Environment, Writing
from mff_pytex.exeptions import WrongTypeListError
from pandas import DataFrame


class Style:
    """Style class takes table style settings and create TeX description of style.

    Attributes:
        columns (int): Count of columns of table.
        styles (dict): dictionary containing all style settings.
        centering (str): Centering of table.
    """

    def __init__(self, columns: int, **styles: Any) -> None:
        """Initialize Style class.

        Args:
            columns (int): Count of columns of table.
            **styles (Any): All settings of style.
        """
        self.columns = columns
        self.styles = styles
        self.centering = self.contains('centering')

    def contains(self, attr: str) -> Any:
        """Check if given attribute is in user-defined styles.

        Args:
            attr (str): Name of attribute.

        Returns:
            Any: attribute value setted by user. If not, than None.
        """
        if attr in self.styles.keys():
            return self.styles[attr]
        else:
            return None

    def __str__(self) -> str:
        """Returns Style object as TeX string.

        Returns:
            str: TeX description of style.
        """
        if self.centering is None:
            self.centering = 'c'
        settings = 'c' * self.columns
        return settings


class Table(Writing):
    """Table structure. Converts pandas' dataframe to TeX table.

    Attributes:
        dataframe (DataFrame): Dataframe containing table.
    """

    def __init__(self, dataframe: DataFrame, **styles: Any) -> None:
        """Initialize Table.

        Args:
            dataframe (DataFrame): Dataframe containing table.
            **styles (Any): Style of table.
        """
        self.en_type = 'tabular'
        self.dataframe = dataframe
        self._style = Style(**styles)

    @property
    def style(self) -> str:
        return str(self._style)

    @style.setter
    def style(self, **style) -> None:
        self._style = Style(**style)

    def dftotex(self) -> None:
        """Converts DataFrame to TeX table.
        Todo:
            * Implementation
        """
        pass

    def __str__(self) -> str:
        """Table as string in TeX form.

        Returns:
            str: string containing given table formatted by given style in TeX.
        """
        self.write(doublecommand('begin', self.en_type, self.style))
        self.dftotex()
        self.write(command('end', self.en_type))
        return self._text


class List(Environment):
    """List structure. Convert python lists to TeX lists."""

    def __init__(self, arr: Union[Sequence, dict], en_type: str = 'itemize') -> None:
        """Initialize List.

        Args:
            arr (Sequence | Dict): Sequence which is iterated. Only dictionary is compactible with 'descrition'.
            en_type (str): Type of list
        """
        self.en_type = en_type
        if self.en_type == 'description' and not isinstance(arr, dict):
            WrongTypeListError()
        self.write(command('begin', self.en_type))
        self.items(arr)

    def item(self, content: str, label: Optional[str] = None):
        """Add one item in content.

        Args:
            content (str): Main text.
            label (str): Label of item.
        """
        if label is None:
            self.write(f'\\item {content}')
        else:
            self.write(f'\\item[{label}] {content}')

    def items(self, arr: Union[Sequence, dict]) -> None:
        """Includes given Sequence of dictionary in content.

        Args:
            arr (Sequence | Dict): Sequence which is iterated. Only dictionary is compactible with 'descrition'.
            en_type (str): Type of list
        """
        if self.en_type == 'description' and not isinstance(arr, dict):
            WrongTypeListError()

        if isinstance(arr, dict):
            for key, value in arr.items():
                self.item(str(value), str(key))
        else:
            for item in arr:
                self.item(str(item))


class NestedList(List):
    # TODO all
    pass
