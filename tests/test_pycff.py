"""Tests for the pycff module."""
from datetime import datetime

import pytest

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
