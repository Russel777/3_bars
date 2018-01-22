# Ближайшие бары

Модуль для json-файла со списками москвоских баров из data.mos.ru, с помощью него можно вычислить:
-самый большой бар
-самый маленький бар
-(опционально) близжайший бар

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python
Biggest bar is Спорт бар «Красная машина»
Smallest bar is БАР. СОКИ
Closest bar is Кальян-бар Shisha Room

```
Запуск с координатами
```bash

$ python bars.py 37.750290923482424 55.618706140521169
Biggest bar is Спорт бар «Красная машина»
Smallest bar is БАР. СОКИ
Closest bar is Кальян-бар Shisha Room

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
