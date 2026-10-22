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


def find_by_title(catalog, title):
    """Возвращает книгу по точному названию или None, если не найдена."""
    for book in catalog:
        if book["title"].lower() == title.lower():
            return book
    return None


def sort_by_author(catalog):
    """Возвращает новый список книг, отсортированный по имени автора (А-Я)."""
    return sorted(catalog, key=lambda book: book["author"])