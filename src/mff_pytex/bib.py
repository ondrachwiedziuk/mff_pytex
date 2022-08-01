"""Utilities for bibliography."""

from typing import Optional
from dataclasses import dataclass

@dataclass
class Bib:
    name: str

    def __str__(self) -> str:
        text = '@' + self.__class__.__name__.lower() + '{'
        for field in self.__dataclass_fields__:
            if getattr(self, field) is not None:
                if field == 'name':
                    text += f"{getattr(self, field)},\n"
                else:
                    text += f"  {field} = \"{str(getattr(self, field))}\" ,\n"
        return text + '}'


@dataclass
class Article(Bib):
    title: str
    year: int
    author: str
    journal: str
    month: Optional[str] = None
    note: Optional[str] = None
    number: Optional[int] = None
    pages: Optional[str] = None
    volume: Optional[str] = None


@dataclass
class Book(Bib):
    title: str
    year: int
    author: str
    publisher: str
    address: Optional[str] = None
    edition: Optional[str] = None
    editor: Optional[str] = None
    month: Optional[str] = None
    note: Optional[str] = None
    number: Optional[int] = None
    series: Optional[str] = None
    volume: Optional[str] = None


@dataclass
class Booklet(Bib):
    title: str
    author: Optional[str] = None
    howpublished: Optional[str] = None
    year: Optional[int] = None
    month: Optional[str] = None
    note: Optional[str] = None


@dataclass
class Conference(Bib):
    author: str
    title: str
    booktitle: str
    year: int
    editor: Optional[str] = None
    number: Optional[int] = None
    volume: Optional[str] = None
    series: Optional[str] = None
    address: Optional[str] = None
    page: Optional[str] = None
    month: Optional[str] = None
    organization: Optional[str] = None
    publisher: Optional[str] = None
    note: Optional[str] = None


@dataclass
class InBook(Bib):
    title: str
    year: int
    author: str
    publisher: str
    pages: str
    chapter: Optional[str] = None
    address: Optional[str] = None
    edition: Optional[str] = None
    editor: Optional[str] = None
    month: Optional[str] = None
    note: Optional[str] = None
    number: Optional[int] = None
    series: Optional[str] = None
    volume: Optional[str] = None


@dataclass
class InCollection(Bib):
    author: str
    title: str
    booktitle: str
    year: int
    publisher: str
    editor: Optional[str] = None
    number: Optional[int] = None
    volume: Optional[str] = None
    series: Optional[str] = None
    typ: Optional[str] = None
    chapter: Optional[str] = None
    pages: Optional[str] = None
    address: Optional[str] = None
    edition: Optional[str] = None
    month: Optional[str] = None
    note: Optional[str] = None


class InProceedings(Conference):
    pass


@dataclass
class Manual(Bib):
    title: str
    author: Optional[str] = None
    organization: Optional[str] = None
    address: Optional[str] = None
    edition: Optional[str] = None
    month: Optional[str] = None
    year: Optional[int] = None
    note: Optional[str] = None


@dataclass
class MasterThesis(Bib):
    author: str
    title: str
    school: str
    year: int
    typ: Optional[str] = None
    address: Optional[str] = None
    month: Optional[str] = None
    note: Optional[str] = None


@dataclass
class Misc(Bib):
    author: Optional[str] = None
    title: Optional[str] = None
    howpublished: Optional[str] = None
    month: Optional[str] = None
    year: Optional[int] = None
    note: Optional[str] = None


class PhdThesis(MasterThesis):
    pass


@dataclass
class Proceedings(Bib):
    title: str
    year: int
    editor: Optional[str] = None
    number: Optional[int] = None
    volume: Optional[str] = None
    series: Optional[str] = None
    address: Optional[str] = None
    month: Optional[str] = None
    organization: Optional[str] = None
    publisher: Optional[str] = None
    note: Optional[str] = None


@dataclass
class TechReport(Bib):
    author: str
    title: str
    institution: str
    year: int
    typ: Optional[str] = None
    number: Optional[int] = None
    address: Optional[str] = None
    month: Optional[str] = None
    note: Optional[str] = None


@dataclass
class Unpublished(Bib):
    author: str
    title: str
    note: str
    month: Optional[str] = None
    year: Optional[int] = None


class Bibliography:
    pass
