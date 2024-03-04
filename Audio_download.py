from pytube import YouTube
import os

# Function to read links from text file separated by spaces or tabs
def read_links(file_path):
    try:
        with open(file_path, 'r') as file:
            links = file.read().strip().split()
            return [link.strip() for link in links]
    except Exception as e:
        print("Error:", e)

# Function to download YouTube audio
def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        # Get the audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        # Download the audio
        audio_file = audio_stream.download(output_path=output_path)
        # Rename the file to have .mp3 extension
        new_audio_file = os.path.splitext(audio_file)[0] + ".mp3"
        os.rename(audio_file, new_audio_file)
        print("Audio downloaded successfully!")
        return new_audio_file
    except Exception as e:
        print("Error:", e)

# Main function
if __name__ == "__main__":
    # Input text file containing YouTube links separated by spaces or tabs
    input_file = "Alinks.txt"
    # Output directory
    output_dir = "Audio_files"
    # Create output directory if not exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Read links from text file
    links = read_links(input_file)
    if links:
        for link in links:
            # Download audio
            audio_file = download_audio(link, output_dir)
            print("Audio file saved at:", audio_file)
    else:
        print("No links found in the input file.")
