from src.airplane import Airplane
from src.open_sky import OpenSkyAPI

if __name__ == '__main__':
    airplane = Airplane("SWR438A", "Canada", -0.0168, 51.0888) # SWR438A

    print(airplane.callsign)
    print(airplane.country)
    print(airplane.velocity)
    print(airplane.altitude)

    api = OpenSkyAPI()

    country = input("Введите страну для поиска (напр. Russian Federation, France, Canada): ")

    coords = api.get_coordinates(country)

    print(coords) # [41.6765597, 83.3362128, -141.00275, -52.3237664]

