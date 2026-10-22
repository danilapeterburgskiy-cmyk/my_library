from src.library import add_book, mark_as_read, count_read, find_by_title, sort_by_author


def test_add_book():
    catalog = []
    add_book(catalog, "Война и мир", "Толстой")
    assert len(catalog) == 1
    assert catalog[0]["title"] == "Война и мир"


def test_mark_as_read():
    catalog = [{"title": "1984", "author": "Оруэлл", "read": False}]
    mark_as_read(catalog, "1984")
    assert catalog[0]["read"] is True


def test_count_read():
    catalog = [
        {"title": "A", "author": "X", "read": True},
        {"title": "B", "author": "Y", "read": False},
        {"title": "C", "author": "Z", "read": True},
    ]
    assert count_read(catalog) == 2


def test_find_by_title():
    catalog = [{"title": "Мастер и Маргарита", "author": "Булгаков", "read": False}]
    found = find_by_title(catalog, "мастер и маргарита")  # проверяем регистр
    assert found is not None
    assert found["author"] == "Булгаков"
    assert find_by_title(catalog, "Несуществующая книга") is None


def test_sort_by_author():
    catalog = [
        {"title": "Книга 1", "author": "Пушкин", "read": True},
        {"title": "Книга 2", "author": "Ахматова", "read": False},
        {"title": "Книга 3", "author": "Толстой", "read": True},
    ]
    sorted_catalog = sort_by_author(catalog)
    authors = [book["author"] for book in sorted_catalog]
    assert authors == ["Ахматова", "Пушкин", "Толстой"]