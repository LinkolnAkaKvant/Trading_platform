# Trading_platform

A small application that shows relationships with suppliers.

### Технические требования:
- Python 3.10  
- Django 4.2.1 
- DRF 3.14.0 
- PostgreSQL 10+  

При выполнении тестового задания вы можете дополнительно использовать любые сторонние Python библиотеки, без всяких ограничений.

### Задание
- Создайте веб-приложение, с API интерфейсом и админ-панелью.
- Создайте базу данных используя миграции Django.
---
Требования к реализации:

1. **Необходимо реализовать модель сети по продаже электроники.**  
Сеть должна представлять собой иерархическую структуру из 3 уровней:
- Завод;
- Розничная сеть;
- Индивидуальный предприниматель.

Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т. е. завод всегда находится на 0 уровне, а если розничная сеть относится напрямую к заводу, минуя остальные звенья — её уровень — 1.

2. **Каждое звено сети должно обладать следующими элементами:** 
- Название;  
- Контакты:    
    - Email;
    - Страна;
    - Город;
    - Улица;
    - Номер дома;
- Продукты:
    - Название;
    - Модель;
    - Дата выхода продукта на рынок;  
- Поставщик (предыдущий по иерархии объект сети);
- Задолженность перед поставщиком в денежном выражении с точностью до копеек;
- Время создания (заполняется автоматически при создании).
3. **Сделать вывод в админ-панели созданных объектов**  
На странице объекта сети добавить:
- ссылку на «Поставщика»;
- фильтр по названию города;
- «admin action», очищающий задолженность перед поставщиком у выбранных объектов.

4. **Используя DRF, создать набор представлений:**

-CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»);  

-Добавить возможность фильтрации объектов по определенной стране.

5. **Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.**

# Запуск проекта:
## Клонируем репозиторий на локальный компьютер.
Установить зависимости.

Создаем базу данных командой docker run --name trading_platform_postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres

Создать и накатить миграции в базе данных командами ./manage.py makemigrations и ./manage.py migrate.

Запустить веб-сервер для разработки командой './manage.py runserver'

Backend будет доступен по адресу 'http://127.0.0.1:8000/'

## Дополнительные сведения

Для работы с приложением нужно создать пользователя и залогиниться

Для работы с админ панелью, нужно создать суперюзера командой ./manage.py createsuperuser
 
