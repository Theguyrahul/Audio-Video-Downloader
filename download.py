from flask import Flask, render_template, request, send_file
from pytube import YouTube
import tempfile

app = Flask(__name__)

# Function to download YouTube video or audio
def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        return stream.download(output_path= output_path)
    except Exception as e:
        print("Error:", e)

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        return stream.download(output_path= output_path)
    except Exception as e:
        return str(e)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download_media", methods=["POST"])
def download_media_route():
    link = request.form.get("link")
    audio_only = request.form.get("audio_only")
    if link:
        if audio_only == "true":
            output_dir = tempfile.mkdtemp(prefix="Audio_files_")
            media_file = download_audio(link, output_dir)
            try:
                return send_file(media_file, as_attachment=True)
            except: 
                pass
        
        else:
            output_dir = tempfile.mkdtemp(prefix="Video_files_")
            media_file = download_video(link, output_dir)
            try:
                return send_file(media_file, as_attachment=True)
            except:
                pass
    else:
        return "Please enter a valid YouTube link."

if __name__ == "__main__":
    app.run(debug=True, port=8000)
