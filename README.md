# Название проекта

TreeMenuApp - древовидное меню.

## Технологии

- Django
- Python

## Описание проекта

Это приложение Django, в котором с использованием template tags реализовано древовидное меню. 
Меню редактируется в админке Django. 
Вы можете отрисовать меню на любой странице вашего приложения, используя следующие теги:

{% load draw_menu %}
{% draw_menu '<название меню>' %}

## Установка

- git clone https://github.com/Axireerrer/TreeMenuApp.git
- сd Project
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py loaddata admin.txt
- python manage.py runserver

## Админка

Для доступа к админке создайте суперпользователя. Подробности смотрите в файле admin.txt:
python manage.py createsuperuser
После создания суперпользователя, войти в админку по адресу http://127.0.0.1:8000/admin/ для редактирования древовидного меню.
