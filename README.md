### Описание проекта:
Проект реализует в себе backend часть API для обработки постов. API взаимодействует с постами, их комментариями, группами и подписками пользователей. К проекту подключена авторизация по JWT токену. Для того, чтобы узнать про все запросы к каждому эндпоинту -  можно перейти по эндпоинту /redoc/.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/DoAlvaro/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Пример использования API:
Получение комментария к публикации по id.
![image](https://github.com/DoAlvaro/api_final_yatube/assets/101565798/e869ddc1-f030-4bfd-9779-724f2c1ea6fa)
Полный список запросов к эндпоинтам можно найти в /redoc/
