Название проекта: Test_Oracle
тестовое задание для Oracle Digital
## Установка

1. Клонируйте репозиторий:

   ```shell
   git clone https://github.com/ваш-проект.git
   Перейдите в каталог проекта:
   **cd ваш-проект
   Создайте виртуальное окружение:
   python3 -m venv venv
   Активируйте виртуальное окружение:
   venv source/bin/activate
   Установите зависимости:
   pip install -r requirements.txt
   Выполните миграции базы данных:
   python manage.py make migrations
   python manage.py migrate
   python manage.py runserver
   Откройте терминал и перейдите в директорию с проектом.
   Запустите следующую команду для сборки и запуска контейнера Docker:
   docker-compose up
  