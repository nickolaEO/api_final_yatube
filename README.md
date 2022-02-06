# api_final
api final yatube
# Описание.
Данный проект представляет из себя API учебного проекта по социальной сети Yatube, в которой различные пользатели могут размещать свои публикации. API позволяет делать запросы к данным моделей Comment, Follow, Group и Post. Для реализации проекта использованы вьюсеты, для реализации механизма авторизации использованый JWT-токены.
# Как установить?
1. Клонируйте репозиторий:<br/>
> $ git clone git@github.com:mnavicki20/api_final_yatube.git<br/>
> $ cd api_final_yatube<br/>
2. Создайте и активируйте виртуальное окружение.<br/>
> $ python -m venv venv<br/>
> $ source venv/Scripts/activate<br/>
3. Установите требуемые зависимости:<br/>
> (venv) $ pip install -r requirements.txt<br/>
4. Выполните миграции:<br/>
> (venv) $ cd yatube_api<br/>
> (venv) $ python manage.py migrate<br/>
5. Локально запустите сервер:<br/>
> (venv) $ python manage.py runserver<br/>
# Примеры запросов
GET http://127.0.0.1:8000/api/v1/posts/<br/>
<br/>
POST http://127.0.0.1:8000/api/v1/posts/<br/>
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0MTc3MTkxLCJqdGkiOiI3YWU1YzA5ZDk2ZWI0ZmFhYWI4MzNmODA4MWIyYjYyNCIsInVzZXJfaWQiOjJ9.lUcpMOkpdVQxVOCcAARpq3cuUZTLHHTqqv9PnfQlWHw<br/>
Content-Type: application/json<br/>
<br/>
{<br/>
    "text": "Шестая публикация для набивки базы данных"<br/>
}<br/>