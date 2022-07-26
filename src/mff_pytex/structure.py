"""Module containing basic structure of file."""

from datetime import date as datum
from typing import Any, Optional


TEMPLATE = "path_to_template"


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


class TexFile:
    """Basic TeX file structure.

    Attributes:
        file_path (str): Path to initialized file.
        preamble (Preamble): Preamble of file.
        body (Body): Body of a file.
    """

    def __init__(self, file_path: Optional[str] = None) -> None:
        """Initialize TexFile

        Args:
            file_path (str | None): Path to initialized file. If None, than use blank template.
        """
        if file_path is None:
            file_path = TEMPLATE

        self.file_path = file_path
        self._load_doc()

    def _load_doc(self) -> None:
        """Load pytex document by source .tex file.
        """
        pass

    def _print_doc(self, path: str) -> None:
        """Prints pytex document to .tex file. """
        pass

    def _create_pdf(self, path: str) -> None:
        """Create pdf file from pytex document. """
        pass


class Preamble:
    """Preamble contains basic info about author and document.

    Attributes:
        title (str): Title of document
        author (str): Author's name
        date (date): Date of creation of document
        packages (list[Package]): packages to use
    """
    def __init__(self,
                 title: Optional[str] = None,
                 author: Optional[str] = None,
                 date: Optional[datum] = None,
                 packages: list[Any] = []) -> None:
        """Initialize Preamble

        Args:
            title (str): Title of document, defaults None
            author (str): Author's name, defaults None
            date (date): Date of creation of document, defaults None
            packages (list[Package]): packages to use, defaults []
        """
        self._title = title
        self._author = author
        self._date = date
        self._packages = packages

    @property
    def title(self) -> str | None:
        """Title getter returns title as TeX command

        Returns:
            str: Title command
        """
        return command('title', self._title) if self._title is not None else None

    @title.setter
    def title(self, title: str) -> None:
        """Title setter

        Args:
            title (str): New title
        """
        self._title = title

    @property
    def author(self) -> str | None:
        """Author getter returns author as TeX command

        Returns:
            str: Author command
        """
        return command('author', self._author) if self._author is not None else None

    @author.setter
    def author(self, author: str) -> None:
        """Author setter

        Args:
            author (str): New author
        """
        self._author = author

    @property
    def date(self) -> str | None:
        """Date getter returns date as TeX command

        Returns:
            str: Date command
        """
        return command('date', str(self._date)) if self._date is not None else None

    @date.setter
    def date(self, date: datum) -> None:
        """Date setter

        Args:
            date (str): New date
        """
        self._date = date

    @property
    def packages(self) -> str | None:
        """Packages getter returns packages as TeX commands

        Returns:
            str: package commands
        """
        text = Writing()
        for package in self._packages:
            text.write(str(package))
        return str(text)

    @packages.setter
    def packages(self, packages: list[Any]) -> None:
        """Packages setter

        Args:
            packages (list[Packages]): New packages to use
        """
        if packages is None:
            packages = []
        self._packages = packages

    def __str__(self) -> str:
        """Returns Preamble as string in TeX form.

        Returns:
            str: Preamble in TeX form.
        """
        text = Writing()
        if self.packages != "":
            text.write(self.packages)
        text.write('')
        text.write(self.title)
        text.write(self.author)
        text.write(self.date)
        return str(text)


class Writing:
    _text = ""

    def __str__(self) -> str:
        return self._text

    def _writeline(self, text: str) -> None:
        """Write single line to the TeX file.

        Args:
            text (str): Line of text intended for insert to content.
        """
        self._text += f"{text}\n"

    def write(self, *lines: str | None) -> None:
        """Write multiple lines to the TeX file.

        Args:
            *lines (str): Lines of text intended for insert to content.
        """
        for line in lines:
            if line is not None:
                self._writeline(line)

    def add(self, environment: Any) -> None:
        """Writes environment to the TeX file.

        Args:
            environment (Any): Figure to use.
        """
        self.write(str(environment))


class Environment(Writing):
    """Basic environment structure.

    Attributes:
        en_type (str): Type of environment
        _text (str): Content of environment,
    """

    def __init__(self, en_type: str, *params: str) -> None:
        """Initialize Environment.

        Args:
            en_type (str): Type of environment
            *params (str): Optional parameters for environment
        """
        self.en_type = en_type
        if params:
            self.write(command('begin', self.en_type, *params))
        else:
            self.write(command('begin', self.en_type))

    def __str__(self) -> str:
        """Returns content string encapsuled by environment.

        Returns:
            str: Content
        """
        return self._text + command('end', self.en_type)

    def math(self, formula: str) -> None:
        self.write(f"\\[ {formula} \\]")


class Document(Environment):
    """Content of document."""

    def __init__(self) -> None:
        """Initialize document.
        """
        self._text = ""
        self.en_type = "document"
        self.write(command('begin', self.en_type))

    def tableofcontents(self) -> None:
        """Add a tableofcontents command to the TeX file."""
        self.write(command('tableofcontents'))

    def maketitle(self) -> None:
        """Add a maketitle command to the TeX file."""
        self.write(command('maketitle'))

    def newpage(self) -> None:
        """Add a newpage command to the TeX file."""
        self.write(command('newpage'))

    def clearpage(self) -> None:
        """Add a clearpage command to the TeX file."""
        self.write(command('clearpage'))


class Table(Environment):
    pass

class Package:
    def __init__(self, name: str, *params: str) -> None:
        self.name = name
        self.optional = params

    def __str__(self) -> str:
        return command('usepackage', self.name, *self.optional)
