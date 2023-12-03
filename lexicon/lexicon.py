LEXICON: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/start': '<b>Привет, читатель!</b>🤗'
              '\nЯ помогу тебе подобрать книгу и, даже, дам почитать полную версию!🤓'
              '\n\nДля начала давай определимся, что ты любишь, с помощью небольшого опроса...',
    '/help': '<b>Это бот-читалка</b>\n\nДоступные команды:\n\n/beginning - '
             'перейти в начало книги\n/continue - продолжить '
             'чтение\n/bookmarks - посмотреть список закладок\n/help - '
             'справка по работе бота\n\nЧтобы сохранить закладку - '
             'нажмите на кнопку с номером страницы\n\n<b>Приятного чтения!</b>',
    '/bookmarks': '<b>Это список ваших закладок:</b>',
    'edit_bookmarks': '<b>Редактировать закладки</b>',
    'edit_bookmarks_button': '❌ РЕДАКТИРОВАТЬ',
    'del': '❌',
    'cancel': 'ОТМЕНИТЬ',
    'no_bookmarks': 'У вас пока нет ни одной закладки.\n\nЧтобы '
                    'добавить страницу в закладки - во время чтения '
                    'книги нажмите на кнопку с номером этой '
                    'страницы\n\n/continue - продолжить чтение',
    'cancel_text': '/continue - продолжить чтение',
    'lets_polling': 'Давай пройдет тест',
    'choose_sub_genre': 'Теперь уточним настроение'
}

LEXICON_COMMANDS: dict[str, str] = {
    '/choose_genre': 'Выбрать жанр',
    '/beginning': 'В начало книги',
    '/continue': 'Продолжить чтение',
    '/bookmarks': 'Мои закладки',
    '/help': 'Справка по работе бота'
}