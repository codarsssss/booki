from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON
from services.file_handling import book
from database.database import genres, sub_genres


def create_pooling_keyboard() -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()

    # Наполняем клавиатуру кнопками-жанрами
    for button in genres.keys():
        kb_builder.row(InlineKeyboardButton(
            text=f'{button}',
            callback_data=str(button)
        ))

    return kb_builder.as_markup()


def create_sub_genres_keyboard(gener: str) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()

    # Наполняем клавиатуру кнопками-жанрами
    for button in genres[gener]:
        kb_builder.row(InlineKeyboardButton(
            text=f'{button}',
            callback_data=str(button)
        ))
    kb_builder.row(InlineKeyboardButton(
        text='<< назад',
        callback_data='choose_genre'
    ))

    return kb_builder.as_markup()


def create_books_keyboard(genre: str) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    print(sub_genres[genre])
    # Наполняем клавиатуру кнопками-жанрами
    for key, value in sub_genres[genre].items():
        kb_builder.row(InlineKeyboardButton(
            text=f'{key}',
            callback_data=str(value)
        ))
    kb_builder.row(InlineKeyboardButton(
        text='<< назад',
        callback_data='choose_genre'
    ))

    return kb_builder.as_markup()


def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(args):
        kb_builder.row(InlineKeyboardButton(
            text=f'{button} - {book[button][:100]}',
            callback_data=str(button)
        ))
    # Добавляем в клавиатуру в конце две кнопки "Редактировать" и "Отменить"
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['edit_bookmarks_button'],
            callback_data='edit_bookmarks'
        ),
        InlineKeyboardButton(
            text=LEXICON['cancel'],
            callback_data='cancel'
        ),
        width=2
    )
    return kb_builder.as_markup()


def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(args):
        kb_builder.row(InlineKeyboardButton(
            text=f'{LEXICON["del"]} {button} - {book[button][:100]}',
            callback_data=f'{button}del'
        ))
    # Добавляем в конец клавиатуры кнопку "Отменить"
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['cancel'],
            callback_data='cancel'
        )
    )
    return kb_builder.as_markup()
