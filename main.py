import yt_dlp
import os

# Set the download path to the Download folder in internal storage
DOWNLOAD_PATH = '/storage/emulated/0/Download/'

def download_audio(url):
    options = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audio-format': 'mp3',
        'outtmpl': os.path.join(DOWNLOAD_PATH, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }
    
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

# Show progress bar
def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} - {d['_eta_str']} left")
    if d['status'] == 'finished':
        print("Download complete. Converting to audio...")

if __name__ == '__main__':
    url = input("Enter YouTube URL: ")
    download_audio(url)
    print(f"Audio saved to: {DOWNLOAD_PATH}")

