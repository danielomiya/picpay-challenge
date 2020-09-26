import datetime
import io
import pytest
import requests
from src.client import PoGoAPIClient


def set_requests_get_response(response, mp):
    mp.setattr(requests, 'get', lambda *args, **kwargs: response)


def test_get_fast_moves_non_2xx_status(monkeypatch):
    with monkeypatch.context() as m:
        res = requests.Response()
        res.status_code = 500

        set_requests_get_response(res, m)

        api = PoGoAPIClient()

        with pytest.raises(RuntimeError):
            api.get_fast_moves()


def test_get_fast_moves_no_content_response(monkeypatch):
    with monkeypatch.context() as m:
        res = requests.Response()
        res.status_code = 204

        set_requests_get_response(res, m)

        api = PoGoAPIClient()

        assert api.get_fast_moves() == []


def test_get_fast_moves_ok(monkeypatch):
    with monkeypatch.context() as m:
        res = type('ResponseMock', (object,), {
            'json': lambda self: [
                {
                    'duration': 400,
                    'energy_delta': 6,
                    'move_id': 200,
                    'name': 'Fury Cutter',
                    'power': 3,
                    'stamina_loss_scaler': 0.01,
                    'type': 'Bug'
                }
            ],
            'status_code': 200
        })()

        api = PoGoAPIClient()
        set_requests_get_response(res, m)
        now = datetime.datetime.today()

        class puredatetime:
            @classmethod
            def now():
                return now

        m.setattr(datetime, 'datetime', puredatetime)

        expected = [
            {
                'id': 1,  # auto-inc
                'created_at': now.isoformat(' '),
                'duration': 400,
                'energy_delta': 6,
                'name': 'Fury Cutter',
                'power': 3,
                'stamina_loss_scaler': 0.01,
                'type': 'Bug',
                'total_damage': 400*3  # duration*power
            }
        ]

        assert list(api.get_fast_moves()) == expected
