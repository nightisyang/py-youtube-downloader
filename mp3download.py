from pytube import YouTube
from tqdm import tqdm
import os

def download_audio(youtube_url):
    try:
        yt = YouTube(youtube_url)

        # Select the audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        file_size = audio_stream.filesize

        # Callback function to update the progress bar
        def progress_function(stream, chunk, bytes_remaining):
            current = ((file_size - bytes_remaining) / file_size)
            percent = '{0:.1f}'.format(current * 100)
            progress = int(50 * current)
            status = f"Downloading: [{percent}%] [{'=' * progress}{' ' * (50 - progress)}]"
            tqdm.write(status, end="\r")

        yt.register_on_progress_callback(progress_function)

        # Creating a 'downloads' folder in the current directory
        download_folder = os.path.join(os.getcwd(), 'downloads')
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Downloading the audio stream
        print(f"Downloading audio: '{yt.title}")
        audio_stream.download(output_path=download_folder)

        # Renaming to MP3
        default_filename = os.path.join(download_folder, audio_stream.default_filename) 
        mp3_filename = default_filename.replace('.mp4', '.mp3')
        os.rename(default_filename, mp3_filename)

        print(f"\nDownloaded and converted to MP3: '{mp3_filename}' in '{download_folder}'")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        youtube_url = input("Enter the YouTube video link (press Ctrl + v to paste): ")
        download_audio(youtube_url)
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        input("Press enter to exit...")

if __name__ == "__main__":
    main()








