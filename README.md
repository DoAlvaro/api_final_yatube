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
Получение списка всех публикаций. При указании параметров limit и offset выдача работает с пагинацией.
![image](https://github.com/DoAlvaro/api_final_yatube/assets/101565798/00ad3b15-262e-40ef-ac93-52d08a8fcb88)

----
Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
![image](https://github.com/DoAlvaro/api_final_yatube/assets/101565798/66b2f12d-d004-42d0-8e13-f231e20d20fb)

----
Получение JWT-токена
![image](https://github.com/DoAlvaro/api_final_yatube/assets/101565798/0c7d980f-42e3-4572-9b2e-a7230cc98e27)

----
Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.
![image](https://github.com/DoAlvaro/api_final_yatube/assets/101565798/82defbbd-0614-4b45-a507-cbce0c46f8cb)

----
Получение комментария к публикации по id.
![image](https://github.com/DoAlvaro/api_final_yatube/assets/101565798/e869ddc1-f030-4bfd-9779-724f2c1ea6fa)

----
Полный список запросов к эндпоинтам можно найти в /redoc/
