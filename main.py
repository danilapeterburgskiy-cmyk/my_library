from src.library import add_book, mark_as_read, count_read, find_by_title, sort_by_author

if __name__ == "__main__":
    my_books = []
    add_book(my_books, "Война и мир", "Толстой")
    add_book(my_books, "Мастер и Маргарита", "Булгаков")
    add_book(my_books, "Евгений Онегин", "Пушкин")
    
    mark_as_read(my_books, "Война и мир")
    
    print("=== Тест функции поиска ===")
    found = find_by_title(my_books, "мастер и маргарита")
    print(f"Найдена книга: {found['title']} ({found['author']})")
    
    print("\n=== Сортировка по автору ===")
    sorted_books = sort_by_author(my_books)
    for book in sorted_books:
        status = "[V]" if book["read"] else "[ ]"
        print(f"{status} {book['author']} — {book['title']}")
        
    print(f"\nВсего прочитано: {count_read(my_books)} из {len(my_books)}")
