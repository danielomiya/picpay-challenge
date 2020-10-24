"""
Pokemon Go API client

Author: Daniel Omiya
"""

import datetime
import itertools
import requests


class PoGoAPIClient:
    """
    Makes requests to the Pokemon Go API
    """

    def __init__(self, base_url=None):
        """
        PoGoAPIClient constructor

        Args:
            base_url (str, optional): API's base url. Defaults to None.
        """
        self.base_url = base_url or 'https://pogoapi.net/api/v1/'


    def get_fast_moves(self):
        """
        Gets Pokemons' fast moves

        Raises:
            RuntimeError: raised if API doesn't return acceptable status codes

        Returns:
            list: pokemons' fast moves
        """
        moves = requests.get(f'{self.base_url}fast_moves.json')

        if 200 <= moves.status_code < 300:
            if moves.status_code in (204, 205):
                return []

            return map(self._create_mapper(), moves.json())

        raise RuntimeError(f'PoGoAPI.get_fast_moves() returned {moves.status_code} status code')


    @staticmethod
    def _create_mapper():
        """
        Creates a mapper function

        Returns:
            function: function that adds extra info to origin records
        """
        seq = itertools.count(start=1)
        now = datetime.datetime.today().isoformat('T')

        def _(move):
            del move['move_id']

            return dict(move,
                        id=next(seq),
                        total_damage=move.get('power')*move.get('duration'),
                        created_at=now)

        return _
