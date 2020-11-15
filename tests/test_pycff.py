"""Tests for the pycff module."""
from datetime import datetime

import pytest
import yatiml

from pycff import pycff


def test_load_simple_cff():
    text = (
            '# YAML 1.2\n'
            '---\n'
            'cff-version: "1.1.0"\n'
            'message: Do cite this\n'
            'title: Testing CFF!\n'
            'version: 0.0.1\n'
            'authors: []\n'
            'date-released: 2020-11-15 00:00:00\n')

    cff = pycff.load(text)
    assert isinstance(cff, pycff.CitationCFF)
    assert cff.cff_version == '1.1.0'
    assert cff.message == 'Do cite this'
    assert cff.title == 'Testing CFF!'
    assert cff.version == '0.0.1'
    assert cff.authors == []
    assert cff.date_released == datetime(2020, 11, 15)


def test_load_reference():
    load = yatiml.load_function(
            pycff.Reference, pycff.Entity, pycff.Person, pycff.Identifier)

    text = (
            'type: conference-paper\n'
            'doi: 10.1234/123-4-567\n'
            'authors:\n'
            '  - family-names: Doe\n'
            '    given-names: John\n'
            'title: Interesting results\n'
            'year: 2020\n'
            'collection-title: Books on Interesting Results\n'
            'volume: 42\n'
            'volume-title: Proceedings of Interesting Results 2020\n'
            'editors:\n'
            '  - family-names: Doe\n'
            '    given-names: Jane\n'
            'start: 1\n'
            'end: 7\n'
            'publisher:\n'
            '  name: Science \'r Us Ltd.\n'
            '  city: Amsterdam\n')

    ref = load(text)
    assert isinstance(ref, pycff.Reference)
    assert ref.typ == 'conference-paper'
    assert ref.doi == '10.1234/123-4-567'
    assert len(ref.authors) == 1
    assert isinstance(ref.authors[0], pycff.Person)
    assert ref.authors[0].family_names == 'Doe'
    assert ref.authors[0].given_names == 'John'
    assert ref.title == 'Interesting results'
    assert ref.year == 2020
    assert ref.collection_title == 'Books on Interesting Results'
    assert ref.volume == 42
    assert ref.volume_title == 'Proceedings of Interesting Results 2020'
    assert len(ref.editors) == 1
    assert isinstance(ref.editors[0], pycff.Person)
    assert ref.editors[0].family_names == 'Doe'
    assert ref.editors[0].given_names == 'Jane'
    assert ref.start == 1
    assert ref.end == 7
    assert isinstance(ref.publisher, pycff.Entity)
    assert ref.publisher.name == 'Science \'r Us Ltd.'
    assert ref.publisher.city == 'Amsterdam'


def test_load_book_reference():
    load = yatiml.load_function(
            pycff.Reference, pycff.BookReference, pycff.Entity, pycff.Person,
            pycff.Identifier)

    text = (
            'type: book\n'
            'title: Introduction to Basic Stuff\n'
            'publisher:\n'
            '  name: Science \'r Us Ltd.\n'
            '  city: Amsterdam\n'
            'year: 2019\n'
            'authors:\n'
            '  - family-names: Wu\n'
            '    given-names: Stacey\n')

    ref = load(text)
    assert isinstance(ref, pycff.BookReference)
