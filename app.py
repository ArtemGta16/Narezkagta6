from flask import Flask, render_template, abort, jsonify
import json
from pathlib import Path

app = Flask(__name__)

DATA_FILE = Path(__file__).parent / "videos.json"


def load_videos():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def index():
    videos = load_videos()
    return render_template("index.html", videos=videos)


@app.route("/video/<video_id>")
def video_page(video_id):
    videos = load_videos()
    video = next((v for v in videos if v["id"] == video_id), None)
    if not video:
        abort(404)
    others = [v for v in videos if v["id"] != video_id][:3]
    return render_template("video.html", video=video, others=others)


@app.route("/api/videos")
def api_videos():
    return jsonify(load_videos())


@app.errorhandler(404)
def not_found(e):
    return render_template("index.html", videos=load_videos()), 404


if __name__ == "__main__":
    app.run(debug=True)
