import os
import sys

BOOK_PATH = 'book/1.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    punctuation = set(",.!:;?")
    end = start + size
    page_text = text[start:end]

    for index, value in zip(reversed(range(len(page_text))), reversed(page_text)):

        if page_text[index - 1] in punctuation:
            continue

        try:
            flag = not page_text[index + 1] in punctuation
        except:
            flag = True

        if value in punctuation and flag:
            page_text = page_text[:index + 1]
            break

    return page_text, len(page_text)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()

    start = 0
    page_number = 1

    while start < len(text):
        page, size = _get_part_text(text, start, PAGE_SIZE)
        page = page.lstrip()  # Удаление лишних символов из начала текста
        book[page_number] = page
        start += size
        page_number += 1

    return book


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))