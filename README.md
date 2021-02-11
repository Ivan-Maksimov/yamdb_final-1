# Yamdb_final

[![yamdb_final workflow](https://github.com/SergeyMMedvedev/yamdb_final/workflows/yamdb_final%20workflow/badge.svg)](https://github.com/SergeyMMedvedev/yamdb_final/actions?query=workflow%3A%22yamdb_final+workflow%22)

[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646??style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![GitHub](https://img.shields.io/badge/-GitHub-464646??style=flat-square&logo=GitHub)](https://github.com/)
[![docker](https://img.shields.io/badge/-Docker-464646??style=flat-square&logo=docker)](https://www.docker.com/)
[![NGINX](https://img.shields.io/badge/-NGINX-464646??style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646??style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)

Проект Yamdb_final создан для демонстрации методики DevOps (Development Operations) и идеи Continuous Integration (CI),
суть которых заключается в интеграции и автоматизации следующих процессов:
* синхронизация изменений в коде
* сборка, запуск и тестерование приложения в среде, аналогичной среде боевого сервера
* деплой на сервер после успешного всех прохождения тестов
* уведомление об успешном прохождении всех этапов

Само приложение взято из проекта [api_yamdb](https://github.com/SergeyMMedvedev/api_yamdb), который представляет собой API сервиса отзывов о фильмах, книгах и музыке.
Зарегистрированные пользователи могут оставлять отзывы (Review) на произведения (Title).
Произведения делятся на категории (Category): «Книги», «Фильмы», «Музыка». 
Список категорий может быть расширен администратором. Приложение сделано с помощью Django REST Framework.

Для Continuous Integration в проекте используется облачный сервис GitHub Actions.
Для него описана последовательность команд (workflow), которая будет выполняться после события push в репозиторий.

## Начало

Клонирование проекта:
```
git clone https://github.com/SergeyMMedvedev/yamdb_final.git
```
Теперь необходимо добавить файл .env с настройками базы данных на сервер. Для этого:

Установить соединение с сервером по протоколу ssh:
```
ssh username@server_address
```
Где username - имя пользователя, под которым будет выполнено подключение к серверу.

server_address - IP-адрес сервера.

Например:
```
ssh praktikum@84.201.176.52
```
В домашней директории проекта
Создать папку www/:
```
mkdir www
```
В ней создать папку yamdb_final/:
```
mkdir www/yamdb_final
```
В папке yamdb_final создать файл .env:
```
touch www/yamdb_final/.env
```

Добавить настройки в файл .env:
```
sudo nano www/yamdb_final/.env
```
Пример настроек:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=postgres
DB_PORT=5432
```


### Подготовка

На сервер нео

В корне проекта находятся два файла:
* docker-compose.yaml
* Dockerfile

docker-compose.yaml - файл, предназначенный для управления взаимодействием контейнеров. В нем содержится инструкция по разворачиванию всего проекта, в том числе описание контейнеров, которые будут развернуты. 

Образ для одного из контейнеров (db) - postgres:13.1. Включает в себя все необходимое для работы базы данных проекта.

Образ для второго контейнера (web) будте создан по инструкции, указанной в файле Dockerfile.
Эта инструкция создает образ на основе базового слоя python:3.8.5. и включает установку всех необходимых зависимостей для работы проекта api_yamdb.
При запуске контейнера выполнится команда, запускающая wsgi-сервер Gunicorn.

Для запуска сборки необходимо перейтив корневую директорию проекта и выполнить 
```
$ docker-compose up
```

Проект будет развернуты два контейнера (db и web).
Посмотреть информацию о состоянии которых можно с помощью команды:

```
$ docker container ls
```

Далее необходимо скопировать CONTAINER ID контейнера web (полное название infra_sp2_web)
и выполинть команду для входа в контейнер:
 
```
$ docker exec -it <CONTAINER ID> bash
```

Будет осуществлен вход в изолированный контейнер со своей операционной системой, интерпритатором и файлами проекта api_yamdb.

Теперь необходимо выполнить миграции:
```
$ python manage.py migrate
```

Для наполнения базы данных тестовыми данными необходимо выполнить:
```
$ python3 manage.py shell
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()

$ python manage.py dumpdata > fixtures.json
```

Для создания суперпользователя, выполните команду:
```
$ python manage.py createsuperuser
```
и далее укажите 
```
Email:
Username:
Password:
Password (again):
```

## Проверка работоспособности

Теперь можно обращаться к API проекта api_yamdb:

* http://localhost:8000/api/v1/auth/token/
* http://localhost:8000/api/v1/users/
* http://localhost:8000/api/v1/categories/
* http://localhost:8000/api/v1/genres/
* http://localhost:8000/api/v1/titles/
* http://localhost:8000/api/v1/titles/{title_id}/reviews/
* http://localhost:8000/api/v1/titles/{title_id}/reviews/{review_id}/
* http://localhost:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/

Подробнее о методах и структурах запросов в см. в проекте api_yamdb.

Для изменения содержания базы данных монжо воспользоваться админкой Django:
* http://localhost:8000/admin/


## Автор

* **Сергей Медведев** -  [SergeyMMedvedev](https://github.com/SergeyMMedvedev)







