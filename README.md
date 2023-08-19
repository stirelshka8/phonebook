# Телефонная книга на Flask

Простое веб-приложение на Flask для управления телефонной книгой. Приложение позволяет добавлять, редактировать и искать записи в телефонной книге.

## Установка

1. Склонируйте репозиторий:

```bash
git clone https://github.com/stirelshka8/phonebook.git
```

2. Перейдите в папку проекта:

```bash
cd phonebook
```

3. Установите зависимости:

```bash
pip install -r req.txt
```

## Запуск

Запустите приложение, используя следующую команду:

```bash
python app.py
```

Приложение будет доступно по адресу [http://localhost:5000](http://localhost:5000/).

#### Функциональность

###### Главная страница

По умолчанию приложение открывает главную страницу, на которой отображаются записи из телефонной книги. Здесь вы можете просматривать записи и переходить между страницами.

###### Добавление записи

Перейдите на страницу `/add`, чтобы добавить новую запись в телефонную книгу. Введите данные о человеке, такие как фамилия, имя, отчество, организация, рабочий и личный телефоны. После заполнения формы новая запись будет добавлена в книгу.

###### Редактирование записи

Перейдите на страницу `/edit/<index>`, чтобы отредактировать существующую запись по её индексу. Вы сможете обновить данные в форме редактирования и сохранить изменения.

###### Поиск записей

Перейдите на страницу `/search`, чтобы выполнить поиск записей в телефонной книге. Введите запрос, и приложение отобразит результаты, соответствующие вашему запросу.

#### Структура проекта

- `app.py`: Основной файл приложения, содержит роутинг и логику.
- `templates/`: Директория для HTML-шаблонов, используемых для отображения страниц.
- `static/`: Директория где расположены статичные данные, такие как изображения и стили CSS.
- `phonebook.txt`: Файл, в котором хранятся данные телефонной книги.

## Требования

- Python 3.x
- Flask
- Любой веб-браузер

## Автор

stirelshka8

## Лицензия

Этот проект распространяется под лицензией [MIT](https://chat.openai.com/LICENSE).