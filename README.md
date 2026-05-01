# Airplane Tracker

Курсовая работа по созданию системы анализа перемещений самометов на Python, реализованная в рамках курса
«Python-разработчик с нуля» от онлайн-университета Skypro.

## Структура проекта

```
project_folder/
├── data/
├── src/
│   ├── __init__.py
│   ├── airplane.py
│   ├── api.py
│   ├── exceptions.py.py
│   ├── json_saver.py
│   ├── open_sky.py
│   └── saver.py
├── tests/
│   ├── __init__.py
│   ├── api_test.py
│   ├── conftest.py
│   ├── test_airplane.py
│   └── test_saver.py
├── .coverage
├── flake8
├── .gitignore
├── coverage.txt
├── lint.sh
├── main.py
├── poetry.loc
├── pyproject.toml
└── README.MD
```

## Установка

Клонируйте репозиторий и установите зависимости через poetry:

```bash
git clone git@github.com:ivanitch/airplane-tracker.git
cd airplane-tracker

# Установить зависимости
poetry install
```

---

## Запуск приложения

```shell
poetry run python main.py
```

Пример работы:

```shell
Введите страну для поиска (напр. Russian Federation, France, Canada): Canada
Сколько самолетов вывести в ТОП по высоте? 5

ТОП-5 самолетов по высоте:
Позывной: CFVLF | Страна: Canada | Высота: 13106.4м
Позывной: N394AJ | Страна: United States | Высота: 13106.4м
Позывной: YEL8 | Страна: United States | Высота: 13106.4м
Позывной: EJM606 | Страна: United States | Высота: 12496.8м
Позывной: ANA102 | Страна: Japan | Высота: 12489.18м
```

---

## Запуск тестов

```bash
# Запуск всех тестов
poetry run pytest
# Подробный вывод
poetry run pytest -v
# С отчётом о покрытии кода
poetry run pytest tests -v --cov=src --cov-report=html
```

### Просмотр покрытия

```bash
poetry run coverage report                 # таблица в консоли
poetry run coverage report > coverage.txt  # направить отчёт в файл `coverage.txt`
poetry run coverage html                   # HTML-отчёт в папке htmlcov/ с интерактивным сайтом (htmlcov/index.html)
```

Файл `coverage.txt`:

```shell
Name                Stmts   Miss  Cover
---------------------------------------
src/__init__.py         0      0   100%
src/airplane.py        31      7    77%
src/api.py              8      2    75%
src/exceptions.py       4      0   100%
src/json_saver.py      32      3    91%
src/open_sky.py        22      0   100%
src/saver.py           11      3    73%
---------------------------------------
TOTAL                 108     15    86%
```

---

## Кодстайл

```bash
poetry run flake8 src tests          # линтер
poetry run black src tests           # форматирование
poetry run isort src tests           # сортировка импортов
poetry run mypy src                  # проверка типов
```

Или запустить все линтеры одной командой:

```bash
poetry run ./lint.sh
```

---


