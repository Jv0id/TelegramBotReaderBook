import os

import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub

BOOK_PATH = os.environ.get("BOOK_PATH") or "book/three-body.txt"
PAGE_SIZE = os.environ.get("PAGE_SIZE") or "500"

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    seps = ['《', '》', '——', '……', '“', '～', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', ']', '【', '】', '{',
            '}', '「', '」', '‘', '（', '）', ',', '.', '!', ';', ':', '?', '，', '。', '！', '；', '：', '？']

    page = text[start:start + size] if start + size <= len(text) else text[start:]
    curr_size = len(page)
    if len(page) >= size:
        finish_sign = text[size + start - 1] if size + start - 1 <= len(text) else text[-1]

        while (finish_sign not in seps or finish_sign == ' ') or (
                finish_sign in seps and text[curr_size + start] in seps):
            curr_size -= 1
            finish_sign = text[curr_size + start - 1]

    return text[start:start + curr_size], curr_size


def prepare_book(path: str, text=None) -> None:
    if text is None:
        text = ''
    if path.endswith(".txt"):
        with open(path, 'r') as r:
            text = r.read()
            pages = len(text) // (int(PAGE_SIZE)) + 1
            start = 0
            for page_num in range(1, pages + 1):
                page_text, page_length = _get_part_text(text, start, int(PAGE_SIZE))
                book[page_num] = page_text.lstrip()
                start += page_length
    elif path.endswith(".epub"):
        read = epub.read_epub(path)
        chapters = []
        for item in read.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                chapters.append(item)
        for chapter in chapters:
            soup = BeautifulSoup(chapter.get_content(), 'html.parser')
            text += soup.get_text()

        pages = len(text) // (int(PAGE_SIZE)) + 1
        start = 0
        for page_num in range(1, pages + 1):
            page_text, page_length = _get_part_text(text, start, int(PAGE_SIZE))
            book[page_num] = page_text.lstrip()
            start += page_length


prepare_book(BOOK_PATH)
