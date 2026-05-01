import pytest
from src.airplane import Airplane
from src.open_sky import OpenSkyAPI


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


@pytest.fixture
def sample_planes(airplane_factory):
    """Список из нескольких типовых самолётов."""
    return [
        airplane_factory(callsign="SBI456", altitude=11000, velocity=300),
        airplane_factory(callsign="UAE789", altitude=12000, velocity=280),
        airplane_factory(callsign="DLH101", altitude=9000, velocity=250),
    ]


@pytest.fixture
def api_client():
    return OpenSkyAPI()
