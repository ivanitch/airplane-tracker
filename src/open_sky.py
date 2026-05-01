import requests

from src.api import AbstarctAPI


class OpenSkyAPI(AbstarctAPI):
    def get_coordinates(self, country: str) -> list:
        url = f"https://nominatim.openstreetmap.org/search?country={country}&format=json"
        headers = {"User-Agent": "AeroplaneApp/1.0"}
        response = requests.get(url, headers=headers)
        data = response.json()

        if not data:
            return []

        # Возвращает [south, north, west, east]
        return [float(x) for x in data[0]["boundingbox"]]

    def get_aeroplanes(self, bbox: list) -> list:
        if not bbox:
            return []

        params = f"{bbox[0]}&lomin={bbox[2]}&lamax={bbox[1]}&lomax={bbox[3]}"
        url = f"https://opensky-network.org/api/states/all?lamin={params}"
        response = requests.get(url)

        if response.status_code != 200:
            return []

        data = response.json()

        return data.get("states", [])
