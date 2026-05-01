class Airplane:
    def __init__(self, callsign: str, country: str, velocity: float, altitude: float) -> None:
        self.callsign = self._validate_value(callsign)
        self.country = self._validate_value(country)
        self._velocity = self._validate_positive(velocity)
        self._altitude = self._validate_positive(altitude)

    @staticmethod
    def _validate_value(value: str) -> str:
        return (value or "").strip() or "N/A"

    @staticmethod
    def _validate_positive(value: float) -> float:
        return float(value) if value and value > 0 else 0.0

    @property
    def velocity(self) -> float:
        return self._velocity

    @property
    def altitude(self) -> float:
        return self._altitude

    def __lt__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.altitude < other.altitude

    def __repr__(self) -> str:
        return f"Airplane({self.callsign}, {self.country}, V={self.velocity}, H={self.altitude})"

    @classmethod
    def cast_to_object_list(cls, data_list: list) -> list:
        objects = []
        for item in data_list:
            obj = cls(
                callsign=item[1],  # позывной
                country=item[2],  # страна
                velocity=item[9],  # скорость
                altitude=item[7],  # высота
            )
            objects.append(obj)
        return objects
