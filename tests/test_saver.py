class TestSaver:
    def test_add_and_read(self, temp_saver, airplane_factory):
        airplane = airplane_factory(callsign="FLY123")
        temp_saver.add_airplane(airplane)
        results = temp_saver.get_airplanes()
        assert len(results) == 1
        assert results[0]["callsign"] == "FLY123"

    def test_get_with_criteria(self, temp_saver, airplane_factory):
        # два разных самолета
        temp_saver.add_airplane(airplane_factory(callsign="RUS01", country="Russia"))
        temp_saver.add_airplane(airplane_factory(callsign="FRA01", country="France"))

        # фильтр по стране
        russia_planes = temp_saver.get_airplanes({"country": "Russia"})
        assert len(russia_planes) == 1
        assert russia_planes[0]["callsign"] == "RUS01"

    def test_delete_airplane(self, temp_saver, airplane_factory):
        airplane = airplane_factory(callsign="DELETE_ME")
        temp_saver.add_airplane(airplane)
        assert len(temp_saver.get_airplanes()) == 1

        temp_saver.delete_airplane("DELETE_ME")
        assert len(temp_saver.get_airplanes()) == 0

    def test_read_empty_file(self, temp_saver):
        # Проверка работы с несуществующим файлом
        assert temp_saver.get_airplanes() == []
