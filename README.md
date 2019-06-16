# UserStore
Простое Django-приложение, которое выводит на странице всех заведённых пользователей в БД.

#### Запуск приложения:
Можно воспользоваться сценарием запуска
`sh start.sh`

Или в ручном режиме путем последовательного запуска команд из каталога приложения

```docker-compose build```# сборка контейнера<br>
```docker-compose run app python manage.py migrate --noinput``` # запуск миграций<br>
```docker-compose up``` # запуск сервера
#### Создание суперпользователя:
Для доступа в административную панель необходимо предварительно создать пользователя с правами администратора.<br>

```docker-compose run app python manage.py createsuperuser```

#### Создание пользователей:

Для добавления рядовых пользователей можно воспользоваться командой `createuser`.

```
docker-compose run app python manage.py createuser
Starting userstore_db_1 ... done
Имя пользователя: Jon
Имя: Иван
Отчество: Иванович
Фамилия: Иванов
Адрес электронной почты: jonson.j@email.local
Password: 
Password (again): 
User created successfully.
```

#### Заполнить базу тестовыми данными:

```docker-compose run app python manage.py loaddata dump.json```