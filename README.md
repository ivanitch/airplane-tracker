# Airplane tracker

Курсовая работа по созданию системы анализа перемещений самометов на Python, реализованная в рамках курса
«Python-разработчик с нуля» от онлайн-университета Skypro.

```shell
poetry run python main.py
```


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
