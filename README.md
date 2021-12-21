# ToDo Rest

## Реализованная функциональность
  - [x] регистрация пользователей;
  - [x] редактирование профиля пользователя;
  - [x] добавление / удаление / редактирования задачи (Task);
  - [x] добавление / удаление поста (Post);
  - [x] добавление / удаление / редактирования комментария к посту (Comment);
  - [x] поиск задачи в арсенале пользователя.

## Зависимости
  - Python - основной язык программирования
  - Django - backend-часть приложения
  - SQLite - основная база данных

## Окружение
1. Развёртывание производится на операционной системе Windows 10
2. Требуется предустановленный интерпретатор python версии 3.9.6
3. Необходимые к установке пакеты перечислены в pyproject.toml

## Развёртывание локально
Запуск самого Django сервера производится в папке проекта при помощи следующей команды:
```bash
python manage.py runserver
```