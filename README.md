## Тестовое задание на позицию Junior/Middle Django developer
### Емельянов Артём

---

## Запуск проекта
1. Клонирование репозитория
  - `git clone git@github.com:JenIK-s/foodgram-project-react.git`
2. Создание `.env` файла в директории `mirgovorit_backend_test_task/`
3. Установка зависимостей
  - `pip install -r requirements.txt`
4. Копирование содержимого из файла `mirgovorit_backend_test_task/env_production` в созданный `.env`
5. Выполнение миграций из директории `mirgovorit_backend_test_task/test_task/`
  - `python manage.py makemigrations product`
  - `python manage.py migrate`
6. Создание супер пользователя
  - `python manage.py createsuperuser`
