# 🎬 GTA VI — Vice City Videos

Сайт для просмотра трейлеров GTA VI в неоновой вайс-сити эстетике.
Написан на **Python + Flask**, легко деплоится куда угодно.

## ✨ Особенности

- 🎨 Ретро-неоновый дизайн (розовый/бирюзовый, сетка, солнце)
- 📺 Встроенный плеер YouTube (видео доступны всем)
- 🗂️ Видео хранятся в `videos.json` — легко добавлять свои
- ⚡ Адаптивная вёрстка, плавные анимации
- 🔌 REST API: `GET /api/videos`

## 🚀 Локальный запуск

```bash
# 1. Клонируй репозиторий
git clone https://github.com/ТВОЙ_НИК/gta6-vice-video-site.git
cd gta6-vice-video-site

# 2. Виртуальное окружение
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Установка зависимостей
pip install -r requirements.txt

# 4. Запуск
python app.py
```

Открой http://127.0.0.1:5000

## ➕ Как добавить своё видео

Открой `videos.json` и добавь объект:

```json
{
  "id": "my-video",
  "title": "Название",
  "description": "Описание",
  "thumbnail": "https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg",
  "embed": "https://www.youtube.com/embed/VIDEO_ID",
  "duration": "3:21",
  "tags": ["Fan"]
}
```

Где `VIDEO_ID` — идентификатор ролика на YouTube
(например, для `youtube.com/watch?v=QdBZY2fkU-0` это `QdBZY2fkU-0`).

## 📤 Публикация на GitHub

```bash
git init
git add .
git commit -m "Initial commit: GTA VI Vice City video site"
git branch -M main
git remote add origin https://github.com/ТВОЙ_НИК/gta6-vice-video-site.git
git push -u origin main
```

## 🌐 Деплой (бесплатно)

- **Render.com** — подключи репозиторий, укажи `python app.py` или gunicorn:
  ```
  gunicorn app:app
  ```
  (добавь `gunicorn` в `requirements.txt`).
- **Railway.app** — автоопределит Flask.
- **PythonAnywhere** — ручная настройка WSGI.

## 📄 Лицензия

MIT — используй свободно. Фанатский проект, не связан с Rockstar Games.