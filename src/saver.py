from abc import ABC, abstractmethod


class AbstactSaver(ABC):
    @abstractmethod
    def add_airplane(self, airplane):
        pass

    @abstractmethod
    def get_airplanes(self, criteria: dict):
        pass

    @abstractmethod
    def delete_airplane(self, callsign: str):
        pass
