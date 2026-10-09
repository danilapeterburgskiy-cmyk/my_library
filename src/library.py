def add_book(catalog, title, author):
    """Добавляет книгу в каталог."""
    catalog.append({"title": title, "author": author, "read": False})
    return catalog


def mark_as_read(catalog, title):
    """Помечает книгу как прочитанную."""
    for book in catalog:
        if book["title"] == title:
            book["read"] = True
    return catalog


def count_read(catalog):
    """Возвращает количество прочитанных книг."""
    return sum(1 for book in catalog if book["read"])
