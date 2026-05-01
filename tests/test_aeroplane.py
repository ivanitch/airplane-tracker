class TestAirplane:

    def test_airplane_init(self, airplane_factory):
        default_airplane = airplane_factory()
        assert default_airplane.callsign == "AFR123"
        assert default_airplane.country == "France"

        custom_airplane = airplane_factory(callsign="TEST99", altitude=500.0)
        assert custom_airplane.callsign == "TEST99"
        assert custom_airplane.altitude == 500.0

    def test_airplane_validation(self, airplane_factory):
        # Проверка защиты от пустых значений позывного и страны
        empty_airplane = airplane_factory(
            callsign="",
            country=""
        )
        assert empty_airplane.callsign == 'N/A'
        assert empty_airplane.country == 'N/A'

        # Проверка защиты от отрицательной скорости
        airplane = airplane_factory(velocity=-100)
        assert airplane.velocity == 0.0

        # Проверка защиты от отрицательной высоты
        airplane = airplane_factory(altitude=-100)
        assert airplane.altitude == 0.0

    def test_comparison(self, airplane_factory):
        low_plane = airplane_factory(altitude=1000)
        high_plane = airplane_factory(altitude=5000)
        assert low_plane < high_plane
