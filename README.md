# Blog API (Django REST Framework + JWT)

REST API для блога с постами и комментариями.

---

## Технологии

- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite (по умолчанию)

---

## Как запустить проект

### 1. Клонировать проект

git clone <ссылка-на-репозиторий>
cd <папка-проекта

### 2. Создать виртуальное окружение
python -m venv venv

Активировать:

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
### 3. Установить зависимости
pip install -r requirements.txt

### 4. Сделать миграции
python manage.py makemigrations
python manage.py migrate

### 6. Создать администратора (необязательно)
python manage.py createsuperuser

### 7. Запустить сервер
python manage.py runserver
