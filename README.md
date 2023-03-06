# QUESTIONNAIRE
##### Сервис для прохождения опросов

## Стек технологий:
- Python
- Django
- HTML
- CSS
- PostgreSQL

## Запуск проекта в dev-режиме
Клонировать репозиторий и перейти в него в командной строке:
``` 
git clone git@github.com:IgorKrupko-94/questionnaire.git 
```
``` 
cd questionnaire
```
Установите и активируйте виртуальное окружение c учётом версии Python 3.9 (выбираем python не ниже 3.7):
``` 
py -3.9 -m venv venv 
```
Для пользователей Windows:
``` 
source venv/Scripts/activate 
```
Для пользователей Linux и macOS:
``` 
source venv/bin/activate 
```
Обновляем до последней версии пакетный менеджер pip:
``` 
python -m pip install --upgrade pip 
```
Затем нужно установить все зависимости из файла requirements.txt:
``` 
pip install -r requirements.txt 
```
Проект настроен к использованию СУБД PostgreSQL, 
поэтому для начала необходимо создать базу данных. 
Инструкцию по настройке можно найти тут:
https://docs.djangoproject.com/en/2.2/intro/tutorial02/
Выполняем миграции:
``` 
python manage.py makemigrations
python manage.py migrate 
```
Запускаем проект:
``` 
python manage.py runserver 
```
### Autor
Igor Krupko