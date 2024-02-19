# Тестовое задание python-разработчик it-start

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fastapi?style=plastic)


## Содержание
- [Тестовое задание](#тестовое-задание-python-разработчик-it-start)
    - [Содержание](#содержание)
    - [Описание](#описание)
    - [Установка](#установка)
    - [Запуск](#запуск)
    - [Эндпоинты](#эндпоинты)
    - [Выполненные требования к системе](#выполненные-требования-к-системе)
    - [Контакты](#контакты)


## Описание
Реализована система учета и анализа данных, поступающих с условного устройства. 
Полученные данные привязываются к временной метке и устройству, от которого они поступили, и сохраняются в базу данных. 
Сервис предоставляет возможность добавлять данные с устройства, получать проанализированные данные за весь период работы устройства, 
а также за выбранный промежуток времени.<br>
В качестве базы данных использована PostgreSQL.<br>
Версия Python: 3.11.4.



## Установка

```bash
git clone github.com/SGGM/developer_backend_python_start.git
```


## Запуск

```bash
docker-compose build
docker-compose up
```


## Эндпоинты

Для сбора данных с устройства:
```bash
/api/v1/create_track_point
```
Для получения статистики за все время:
```bash
/api/v1/get_device_stats/{device_id}
```
Для получения статистики за определнный период:
```bash
/api/v1/get_device_stats_in_range
```
Более подробная документация:
```bash
/docs
/redoc
```


## Выполненные требования к системе

- [x] Сбор статистки с устройства по его идентификатору в формате:
```json
{
  "x": "float",
  "y": "float",
  "z": "float",
}
```
- [x] Реализован анализ статистики за все время.
- [x] Реализован анализ статистики за определенный период.
- [x] Результатом анализа являются числовые характеристики:
  - минимальное значение
  - максимальное значение
  - количество
  - сумма
  - медиана
- [x] Сервис и его окружение разворачивается средствами docker + docker-compose


## Контакты
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Stole_your_jet)<br>
gleb_somov@mail.ru


