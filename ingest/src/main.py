#!/usr/bin/env python3

"""
Main script
"""

from src.client import PoGoAPIClient
from src.config import ConfigLoader
from src.utils import sanitize
from src.writer import CSVWriter


def main():
    """
    Script start
    """
    config = ConfigLoader() \
        .add_config('config.ini')

    api_url = config.get_string(key='app.client.url')
    assert api_url is not None, 'api base url not set'

    output_filename = config.get_string('app.pokemon.output.path')
    assert output_filename is not None, 'output path not set'

    api = PoGoAPIClient(api_url)
    writer = CSVWriter(should_write_headers=True)

    with open(output_filename, 'w') as file:
        writer.write(file, api.get_fast_moves())


if __name__ == '__main__':
    main()
