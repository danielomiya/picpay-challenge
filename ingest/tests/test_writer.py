import io
import pytest
from src.writer import CSVWriter


def test_writer_write_with_headers():
    data = [{'a': 2, 'b': 3}, {'a': 11, 'b': 5}]
    expected = 'a,b\n2,3\n11,5\n'
    writer = CSVWriter(True)

    file = io.StringIO()

    writer.write(file, data)

    assert file.getvalue() == expected


def test_writer_write_without_headers():
    data = [{'a': 3, 'b': 2}, {'a': 4, 'b': 6}]
    expected = '3,2\n4,6\n'
    writer = CSVWriter(False)

    file = io.StringIO()

    writer.write(file, data)

    assert file.getvalue() == expected
