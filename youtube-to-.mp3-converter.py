import yt_dlp
import subprocess
import os


def download_youtube_audio(url: str, output_path: str = "downloads") -> None:
    # Ensure the output path exists
    os.makedirs(output_path, exist_ok=True)

    # Define options for yt-dlp to download audio and select the output path
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Specify output path
    }

    # Download the audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url, download=True)


def main():
    youtube_url = input("Enter the YouTube URL: ")
    download_path = "downloads"  # Folder to save the files (OPTIONAL)

    download_youtube_audio(youtube_url, download_path)


if __name__ == "__main__":
    main()
