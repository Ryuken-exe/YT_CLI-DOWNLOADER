import yt_dlp


# Function to download a video or extract audio
def download_video(url, choice):

    # If the user chooses MP4
    if choice == "1":
        options = {
            # Download the best available video and audio
            # and combine them if necessary
            "format": "bestvideo+bestaudio/best",

            # Save the final merged file as MP4
            "merge_output_format": "mp4"
        }

    # If the user chooses MP3
    elif choice == "2":
        options = {
            # Download the best available audio
            "format": "bestaudio/best",

            # Convert the downloaded audio to MP3
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",

                    # Set the output audio format to MP3
                    "preferredcodec": "mp3",

                    # Set MP3 quality to 192 kbps
                    "preferredquality": "192"
                }
            ]
        }

    # Handle an invalid choice
    else:
        print("Invalid choice")
        return

    # Create a yt-dlp downloader using the selected options
    with yt_dlp.YoutubeDL(options) as ydl:

        # Download the video/audio from the provided URL
        ydl.download([url])


# Keep the program running until the user chooses to exit
while True:

    # Ask the user for the video URL
    url = input("Enter Your URL > ")

    # Commands that will stop the program
    exit_commands = [
        "exit",
        "clear",
        "stop",
        "ok"
    ]

    # Check if the user entered an exit command
    if url in exit_commands:
        print("Thank you")
        break

    # Ask the user which format they want to download
    choice = input("""
        Choose Download Format:

        1. MP4
        2. MP3

        Enter your choice >
        """)

    # Call the download function
    download_video(url, choice)

    # Display a message after the download function finishes
    print("DOWNLOAD COMPLETED")
