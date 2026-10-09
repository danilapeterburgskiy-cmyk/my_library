from src.library import add_book, mark_as_read, count_read


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
