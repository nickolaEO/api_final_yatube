# **Yatube API**

### _API для социальной сети Yatube_

# Описание

Проект представляет собой API для социальной сети Yatube.  
Пользователь может зарегестрироваться в Yatube, получить свой JWT-токен для аутентификации и постить публикации.  
_Токен дается всего на одну неделю, поэтому его необходимо периодически обновлять_.
Помимо этого, пользователю предоставляется возможность прикреплять _изображения_ к постам, а также можно добавлять свои посты в различные _группы_. Например, пользователь-кулинар может запостить рецепт приготовления пюрешки с котлеткой, дополнить фотографией ингредиентов и добавить пост в группу "Кулинарные мастера".  
В Yatube также есть возможность _подписываться_ на других пользователей и _комментировать_ посты.

# Технологии

- [Python 3.8.8](https://www.python.org/downloads/release/python-388/)
- [Django 2.2.16](https://www.djangoproject.com/)
- [Django Rest Framework 3.12.4](https://www.django-rest-framework.org/)

# Установка

Клонируйте репозиторий и перейдите в него в командной строке:
```sh
git clone https://github.com/nickolaEO/api_final_yatube.git
```
```sh
cd api_final_yatube
```
Создайте и активируйте виртуальное окружение:
```sh
python -m venv venv
```
```sh
source venv/Scripts/activate
```
Установите зависимости из файла _requirements.txt_:
```sh
python -m pip install --upgrade pip
```
```sh
pip install -r requirements.txt
```
Выполните миграции:
```sh
python manage.py migrate
```
Запустите проект:
```sh
python manage.py runserver
```

# Примеры запросов

**GET**: http://127.0.0.1:8000/api/v1/posts/  
Пример ответа:
```json
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2021-10-14T20:41:29.648Z",
    "image": "string",
    "group": 0
}
```

**POST**: http://127.0.0.1:8000/api/v1/posts/  
Тело запроса:
```json
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
Пример ответа:
```json
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```

**GET**: http://127.0.0.1:8000/api/v1/posts/0/comments/  
Пример ответа:
```json
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "created": "2019-08-24T14:15:22Z",
        "post": 0
    }
]
```

**POST**: http://127.0.0.1:8000/api/v1/posts/0/comments/  
Тело запроса:
```json
{
    "text": "string"
}
```
Пример ответа:
```json
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```

## License

MIT

**Free Software**
