import pytest
from src.airplane import Airplane


@pytest.fixture
def airplane_factory():
    """Фабрика для создания объектов самолетов с дефолтными значениями"""

    def _make_airplane(**kwargs):
        params = {
            "callsign": "AFR123",
            "country": "France",
            "velocity": 250.0,
            "altitude": 10000.0,
        }
        params.update(kwargs)
        return Airplane(**params)

    return _make_airplane
