from src.airplane import Airplane

if __name__ == '__main__':
    airplane = Airplane("SWR438A", "Canada", -0.0168, 51.0888) # SWR438A

    print(airplane.callsign)
    print(airplane.country)
    print(airplane.velocity)
    print(airplane.altitude)
