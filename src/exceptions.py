class AeroplaneError(Exception):
    """Базовое исключение приложения"""

    pass


class APIConnectionError(AeroplaneError):
    """Ошибка при подключении к внешним API (Nominatim/OpenSky)"""

    pass
