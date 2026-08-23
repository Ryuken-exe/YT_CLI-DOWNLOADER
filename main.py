import yt_dlp


def download_video(url, choice):

    if choice == "1":
        options = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4"
        }

    elif choice == "2":
        options = {
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192"
                }
            ]
        }

    else:
        print("Invalid choice")
        return

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

while True:
    url = input("Enter Your URL > ")

    list = [
        "exit","clear","stop","ok"
        ]
    
    if url in list:
        print("Thank you")
        break
    
    choice = input("""
        Choose Download Format:

        1. MP4
        2. MP3

        Enter your choice > 
        """)

    download_video(url, choice)

    print("DOWNLOAD COMPLETED")