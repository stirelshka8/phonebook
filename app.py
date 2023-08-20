from flask import Flask, render_template, request, redirect, url_for
from typing import List

from werkzeug import Response

app = Flask(__name__)


def load_data() -> List[List[str]]:
    """
    Загружает данные из файла 'phonebook.txt'.

    Returns:
        List[List[str]]: Список записей телефонной книги, где каждая запись представлена списком строк.
    """
    try:
        with open('phonebook.txt', 'r') as f:
            lines = f.readlines()
            data = [line.strip().split('*') for line in lines]
            return data
    except FileNotFoundError:
        return []


def save_data(data: List[List[str]]) -> None:
    """
    Сохраняет данные в файл 'phonebook.txt'.

    Args:
        data (List[List[str]]): Список записей телефонной книги для сохранения.
    """
    with open('phonebook.txt', 'w') as f:
        for entry in data:
            f.write('*'.join(entry) + '\n')


@app.route('/')
def index() -> str:
    """
    Отображает главную страницу с записями телефонной книги.

    Returns:
        str: HTML-страница с отображением записей телефонной книги.
    """
    page = request.args.get('page', 1, type=int)
    entries_per_page = 10
    data = load_data()
    total_entries = len(data)
    start_idx = (page - 1) * entries_per_page
    end_idx = start_idx + entries_per_page
    entries = data[start_idx:end_idx]
    # print(start_idx)
    total_pages = (total_entries + entries_per_page - 1) // entries_per_page
    return render_template('index.html',
                           entries=entries,
                           current_page=page,
                           total_pages=total_pages,
                           index_increase=start_idx)


@app.route('/add', methods=['GET', 'POST'])
def add_entry() -> Response | str:
    """
    Обрабатывает добавление новой записи в телефонную книгу.

    Returns:
        str: HTML-страница для добавления новой записи или перенаправление на главную страницу.
    """
    if request.method == 'POST':
        new_entry = [
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['organization'],
            request.form['work_phone'],
            request.form['personal_phone']
        ]
        data = load_data()
        data.append(new_entry)
        save_data(data)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_entry(index: int) -> Response | str:
    """
    Обрабатывает редактирование существующей записи в телефонной книге.

    Args:
        index (int): Индекс записи, которую нужно отредактировать.

    Returns:
        str: HTML-страница для редактирования записи или перенаправление на главную страницу.
    """
    data = load_data()
    entry = data[index]
    if request.method == 'POST':
        edited_entry = [
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['organization'],
            request.form['work_phone'],
            request.form['personal_phone']
        ]
        data[index] = edited_entry
        save_data(data)
        return redirect(url_for('index'))
    return render_template('edit.html', entry=entry, index=index)


@app.route('/search', methods=['GET', 'POST'])
def search_entries() -> str:
    """
    Обрабатывает поиск записей в телефонной книге по заданному запросу.

    Returns:
        str: HTML-страница с результатами поиска или пустая страница поиска.
    """
    if request.method == 'POST':
        query = request.form['query'].lower()
        data = load_data()
        search_results = []
        for entry in data:
            if any(query in field.lower() for field in entry):
                search_results.append(entry)
        return render_template('search.html', query=query, search_results=search_results)
    return render_template('search.html', query=None, search_results=None)


if __name__ == '__main__':
    app.run(debug=True)
