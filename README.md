# music-finder
# Music Finder

A Django-based music search application that scans local folders for music files and lets users search for songs by title or artist.

## Features

- Scan folders for music files.
- Search songs by title or artist.
- Fuzzy search using RapidFuzz.
- Play songs directly from the application.
- Sort search results alphabetically when no search query is provided.

## Tech Stack

- Python
- Django
- SQLite (Django's default database, if configured)
- RapidFuzz
- HTML and CSS

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/pegahsadr2/music-finder.git
   cd music-finder
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r musicbot/requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python musicbot/manage.py migrate
   ```

## Running the Application

```bash
python musicbot/manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser, provided your Django URL configuration routes the root path to the search page.

## Configuration

Update the music folder path in the application before scanning your own music library. The current scanner view uses a local folder path, which may need to be changed for your computer.

## License

MIT (add a LICENSE file if you choose this license).

