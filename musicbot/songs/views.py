from django.shortcuts import render, redirect
from rapidfuzz import fuzz
from .models import Song
from django.http import FileResponse
from .scanner import scan_music


def search(request):
    query = request.GET.get("q", "").strip()

    songs = Song.objects.all()

    results = []

    if not query:
        results = songs.order_by("title")

        return render(request, "search.html", {
            "results": results
        })

    for song in songs:
        score_title = fuzz.partial_ratio(query.lower(), song.title.lower())
        score_artist = fuzz.partial_ratio(query.lower(), (song.artist or "").lower())

        score = max(score_title, score_artist)

        if score > 60:
            results.append((score, song))

    results.sort(key=lambda x: (-x[0], x[1].title.lower()))

    return render(request, "search.html", {
        "results": [r[1] for r in results]
    })


def play_song(request, song_id):
    song = Song.objects.get(id=song_id)
    return FileResponse(open(song.file_path, "rb"))


def rescan(request):
    path = "your-local-path"
    scan_music(path)
    return redirect("search")
