"""Module containing basic structure of file."""

from datetime import date as datum
from typing import Optional
from mff_pytex.utils import command, get_dir, Writing, Environment, TemplateProperty
import os

# TODO importing and another document structuring


class PreambleProperty(TemplateProperty):
    """Template for preamble attribute properties.

        Example:
            class Example:
                attr = PreambleProperty()

            obj = Example()
            obj.attr = 'name' # set attr as 'name' string

            print(obj.attr) # return attribute as TeX command string.
        """

    def __get__(self, obj, objtype=None) -> Optional[str]:
        """Getter template.

        Args:
            obj: Object that use this template for given property.
            objtype: type of object.

        Returns:
            str: String in form of TeX command for this attribute.
        """
        value = getattr(obj, self.private_name)
        return command(self.public_name, str(value)) if value is not None else None

    def __set__(self, obj, value) -> None:
        """Setter template.

        Args:
            obj: Object that use this template for given property.
            value: New value of attribute.
        """
        setattr(obj, self.private_name, value)


class Preamble:
    """Preamble contains basic info about author and document.
    """

    title = PreambleProperty()
    author = PreambleProperty()
    date = PreambleProperty()

    def __init__(self,
                 title: Optional[str] = None,
                 author: Optional[str] = None,
                 date: Optional[datum] = None,
                 packages: list = []) -> None:
        """Initialize Preamble

        Args:
            title (str): Title of document, defaults None
            author (str): Author's name, defaults None
            date (date): Date of creation of document, defaults None
            packages (list[Package]): packages to use, defaults []
        """
        self.title = title
        self.author = author
        self.date = date
        self.packages = packages

    @property
    def packages(self) -> Optional[str]:
        text = Writing()
        for package in self._packages:
            text.write(str(package))
        return str(text)

    @packages.setter
    def packages(self, packages: list) -> None:
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
        text.write(str(self.date))
        return str(text)


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


class TexFile:
    """Basic TeX file structure.

    Attributes:
        file_path (str): Path to initialized file.
        body (Body): Body of a file.
    """

    preamble = Preamble()
    document = Document()

    def __init__(self, file_name: str) -> None:
        """Initialize TexFile

        Args:
            file_name str: Name of file which will be created.
        """

        self.file_path = f"{get_dir()}/{file_name}.tex"

    def create(self, mode: str = 'w+') -> None:
        """Creates file and writes its content.

        Args:
            mode (str): mode of given file. Same as open() function.
        """
        tex = open(self.file_path, mode)
        tex.write(str(self.preamble))
        tex.write(str(self.document))
        tex.close()

    def make_pdf(self, mode: str = 'r') -> None:
        """Creates pdf file, if neccessary writes its content and create pdf document.

        Args:
            mode (str): mode of given file. Same as open() function.
        """
        if mode not in ['r']:
            self.create(mode)
        os.system(f"pdflatex {self.file_path}")
