from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

# Function to download YouTube video or audio
def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        return stream.download(output_path=output_path)
    except Exception as e:
        print("Error:", e)

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        return stream.download(output_path=output_path)
    except Exception as e:
        return str(e)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download_media", methods=["POST"])
def download_media_route():
    link = request.form.get("link")
    print(link)
    audio_only = request.form.get("audio_only")
    if link:
        if audio_only == "true":
            output_dir = "Audio_files"
            os.makedirs(output_dir, exist_ok=True)
            media_file = download_audio(link, output_dir)
            return f"Video file saved at: {media_file}"
        else:
            
            output_dir = "Video_files"
            os.makedirs(output_dir, exist_ok=True)
            media_file = download_video(link, output_dir)
            return f"Video file saved at: {media_file}"
    else:
        return "Please enter a valid YouTube link."

if __name__ == "__main__":
    app.run(debug=True, port=5000)
