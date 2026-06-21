# Local Autoposter

Чистый публичный шаблон локального автопостера.

Репозиторий специально не содержит:

- настоящих токенов;
- файла `.env`;
- базы `autopost.db`;
- личных ссылок;
- привязки к конкретному сайту.

## Быстрый старт

1. Скопируй `.env.example` в `.env`.
2. Заполни `SITE_URL` и `CONTENT_URL`.
3. Добавь токены только тех платформ, которые нужны.
4. Проверь:

```bash
python app.py self-test
python app.py status
python app.py preview --limit 5
```

Тестовая отправка без публикации:

```bash
python app.py send --all --dry
```

Реальная отправка:

```bash
python app.py send --all
```

## Не загружать в GitHub

- `.env`
- `autopost.db`
- логи
- `__pycache__`

Они добавлены в `.gitignore`.
