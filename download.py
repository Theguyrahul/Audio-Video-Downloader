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
def download_Video(url, output_path):
    try:
        yt = YouTube(url) 
        #Select the highest resolution stream
        stream = yt.streams.get_highest_resolution()
        # Download the video
        return stream.download(output_path=output_path)
    except Exception as e:
        print("Error:", e)

# Main function
if __name__ == "__main__":
    # Input text file containing YouTube links separated by spaces or tabs
    input_file = "Vlinks.txt"
    # Output directory
    output_dir = "Video_files"
    # Create output directory if not exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Read links from text file
    links = read_links(input_file)
    if links:
        for link in links:
            # Download Video
            Video_file = download_Video(link, output_dir)
            print("Video file saved at:", Video_file)
    else:
        print("No links found in the input file.")