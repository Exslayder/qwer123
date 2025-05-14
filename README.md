## Требования
- Python 3.12.3
- PostgreSQL
- Django 5.2.1

## Быстрый старт

### 1. Клонировать репозиторий:
```bash
git clone https://github.com/Exslayder/qwer123.git
cd cd qwer123
```

### 2. Создать виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Установить зависимости:
```bash
pip install -r requirements.txt
```
### 4. Настроить базу django_proj/settings.py 
DATABASES -> указать NAME, USER, PASSWORD.

### 5. Выполнить миграции:
```bash
python manage.py migrate
```
### 6. Запустить сервер:
```bash
python manage.py runserver
```
### 7. Открыть в браузере: http://127.0.0.1:8000/