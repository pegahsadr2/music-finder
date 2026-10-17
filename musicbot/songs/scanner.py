import os
from .models import Song

MUSIC_EXTENSIONS = ['.mp3', '.wav', '.flac', '.ogg', '.m4a']


def scan_music(folder_path):
    print("🔍 Scanning started:", folder_path)

    new_songs = []

    existing_files = set(Song.objects.values_list("file_path", flat=True))

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            if any(file.lower().endswith(ext) for ext in MUSIC_EXTENSIONS):

                full_path = os.path.join(root, file)

                print("🎵 Found:", full_path)

                if full_path not in existing_files:

                    new_songs.append(
                        Song(
                            title=file,
                            file_path=full_path
                        )
                    )

    Song.objects.bulk_create(new_songs)

    print(f"✅ Done. New songs added: {len(new_songs)}")

    return len(new_songs)