from abc import ABC, abstractmethod


class AbstarctAPI(ABC):
    @abstractmethod
    def get_coordinates(self, country: str):
        pass

    @abstractmethod
    def get_airplanes(self, bbox: list):
        pass
