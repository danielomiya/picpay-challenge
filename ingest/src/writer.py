"""
Helper class to write CSVs.
"""
from src.utils import sanitize

class CSVWriter:
    def __init__(self, should_write_headers=False):
        """
        CSV writer

        Args:
            should_write_headers (bool, optional): flags whether to put headers. Defaults to False.
        """
        self.should_write_headers = should_write_headers


    def write(self, file, rows):
        """
        Writes a dict to any file-like object

        Args:
            file (file): file to write to
            rows (dict): data to be written (keys must be string)
        """
        for idx, row in enumerate(rows):
            if idx == 0 and self.should_write_headers:  # adds headers on first row
                print(','.join(row.keys()), file=file)

            print(','.join(map(sanitize, row.values())), file=file)
