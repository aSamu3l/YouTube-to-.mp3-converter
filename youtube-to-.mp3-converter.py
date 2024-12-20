import yt_dlp
import subprocess

def download_youtube_audio(url, output_path="downloads"):
    # Define options for yt-dlp to download audio
    ydl_opts = {
        'format': 'bestaudio/best',  # Choose the best audio quality
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save the file with the title of the video
        'quiet': False,  # Show download progress
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the audio
        info_dict = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info_dict)
        return filename  # Return the filename of the downloaded audio

def convert_to_mp3(input_file, output_file):
    # Convert the downloaded file to mp3 using ffmpeg
    subprocess.run(['ffmpeg', '-i', input_file, output_file])

def main():
    youtube_url = input("Enter the YouTube URL: ")
    download_path = "downloads"  # Folder to save the files

    print(f"Downloading and converting audio from: {youtube_url}")
    downloaded_file = download_youtube_audio(youtube_url, download_path)

    # Convert to mp3
    output_mp3 = downloaded_file.rsplit('.', 1)[0] + '.mp3'
    convert_to_mp3(downloaded_file, output_mp3)
    print(f"Download and conversion complete. MP3 saved as: {output_mp3}")

if __name__ == "__main__":
    main()