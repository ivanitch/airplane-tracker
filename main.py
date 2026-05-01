from src.open_sky import OpenSkyAPI
from src.airplane import Airplane
from src.json_saver import JSONSaver


def user_interaction():
    api = OpenSkyAPI()
    saver = JSONSaver()

    country = input("Введите страну для поиска (напр. Russian Federation, France, Canada): ")

    # Получаем координаты и данные
    coords = api.get_coordinates(country)
    raw_data = api.get_airplanes(coords)

    if not raw_data:
        print("Самолеты не найдены или ошибка API.")
        return

    # Превращаем в объекты
    planes = Airplane.cast_to_object_list(raw_data)

    # Сохраняем в файл
    for p in planes:
        saver.add_airplane(p)

    # Фильтрация и топ
    top_n = input("Сколько самолетов вывести в ТОП по высоте? ")
    top_n = int(top_n) if top_n.isdigit() else 5

    # Сортировка
    sorted_planes = sorted(planes, reverse=True)

    print(f"\nТОП-{top_n} самолетов по высоте:")
    for p in sorted_planes[:top_n]:
        print(f"Позывной: {p.callsign} | Страна: {p.country} | Высота: {p.altitude}м")


if __name__ == "__main__":
    user_interaction()
