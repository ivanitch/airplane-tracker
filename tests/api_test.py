from unittest.mock import patch, MagicMock
from src.exceptions import APIConnectionError

import pytest


class TestAPI:
    def test_get_coordinates_success(self, api_client):
        # Имититация ответа от Nominatim
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {"boundingbox": ["55.0", "56.0", "37.0", "38.0"]}
        ]

        with patch('requests.get', return_value=mock_response):
            coords = api_client.get_coordinates("Russia")
            assert coords == [55.0, 56.0, 37.0, 38.0]
            assert isinstance(coords[0], float)

    def test_get_coordinates_empty(self, api_client):
        # Страна не найдена
        mock_response = MagicMock()
        mock_response.json.return_value = []

        with patch('requests.get', return_value=mock_response):
            coords = api_client.get_coordinates("NonExistentCountry")
            assert coords == []

    def test_get_aeroplanes_success(self, api_client):
        # Имититация успешного ответа от OpenSky
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "states": [
                ["icao1", "CALL123", "France", 1705415400, 1705415400, 2.3, 48.8, 10000, False, 250.0, 180, 0, None,
                 10000,
                 "1234", False, 0]
            ]
        }

        with patch('requests.get', return_value=mock_response):
            planes = api_client.get_airplanes([55.0, 56.0, 37.0, 38.0])
            assert len(planes) == 1
            assert planes[0][1] == "CALL123"

    def test_get_aeroplanes_fail(self, api_client):
        # Ошибка сервера (код не 200) выбрасывается исключение APIConnectionError
        mock_response = MagicMock()
        mock_response.status_code = 404

        with patch('requests.get', return_value=mock_response):
            with pytest.raises(APIConnectionError):
                api_client.get_airplanes([0, 0, 0, 0])

    def test_get_aeroplanes_no_bbox(self, api_client):
        # Проверка обработки пустого ввода координат
        planes = api_client.get_airplanes([])
        assert planes == []
