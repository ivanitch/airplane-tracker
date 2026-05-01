import json
import os

from src.saver import AbstactSaver


class JSONSaver(AbstactSaver):
    def __init__(self, filename="data/airplaneplanes.json"):
        self.path = filename
        dirname = os.path.dirname(self.path)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)

    def _read_file(self):
        if not os.path.exists(self.path):
            return []
        with open(self.path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def add_airplane(self, airplane):
        data = self._read_file()
        data.append(
            {
                "callsign": airplane.callsign,
                "country": airplane.country,
                "velocity": airplane.velocity,
                "altitude": airplane.altitude,
            }
        )
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_airplanes(self, criteria: dict = None):
        data = self._read_file()
        if not criteria:
            return data
        return [item for item in data if all(item.get(k) == v for k, v in criteria.items())]

    def delete_airplane(self, callsign: str):
        data = self._read_file()
        new_data = [item for item in data if item.get("callsign") != callsign]
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)
