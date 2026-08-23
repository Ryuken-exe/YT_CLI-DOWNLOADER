YouTube Downloader - README
📥 YouTube Video Downloader
A Python-based YouTube downloader that allows you to download videos in MP4 format or extract audio as MP3 files using yt-dlp.

✨ Features
Download Videos: Save YouTube videos in MP4 format

Extract Audio: Convert YouTube videos to MP3 audio files

Simple Interface: Easy-to-use command-line menu system

High Quality: Downloads best available video and audio quality

Auto-merging: Automatically merges video and audio streams (MP4 option)

🚀 Installation
Prerequisites
Python 3.6 or higher

pip (Python package installer)

FFmpeg (required for audio extraction and merging)

Step 1: Install FFmpeg
Windows:

Download from FFmpeg.org

Add the bin folder to your system PATH

macOS:

bash
brew install ffmpeg
Linux (Ubuntu/Debian):

bash
sudo apt update
sudo apt install ffmpeg
Step 2: Install yt-dlp
bash
pip install yt-dlp
📦 Usage
Run the script:

bash
python youtube_downloader.py
Enter your YouTube URL when prompted

Choose your download format:

Enter 1 for MP4 (Video + Audio)

Enter 2 for MP3 (Audio only)

The file will be downloaded to your current directory

Type exit, clear, stop, or ok to quit the program

🎯 Example
text
Enter Your URL > https://www.youtube.com/watch?v=xxxxxxxxxxx

Choose Download Format:

1. MP4
2. MP3

Enter your choice > 1

DOWNLOAD COMPLETED
📁 Output Files
MP4 files: Saved as [video_title].mp4

MP3 files: Saved as [video_title].mp3

⚙️ Configuration Options
The script includes the following configuration:

MP4 Download
Downloads best available video and audio streams

Merges them into a single MP4 file

MP3 Extraction
Extracts audio in MP3 format

Quality set to 192kbps for good sound quality

⚠️ Limitations
Some YouTube videos may have region restrictions

Very long videos may take time to process

Internet connection required

🔧 Troubleshooting
"FFmpeg not found" error
Ensure FFmpeg is properly installed

Check if FFmpeg is in your system PATH

Download fails
Check your internet connection

Ensure the YouTube URL is valid

Update yt-dlp: pip install --upgrade yt-dlp

Audio/Video quality issues
Some videos may not have high-quality options available

YouTube may restrict download quality for certain content

📝 Dependencies
yt-dlp - YouTube downloading library

FFmpeg - Media processing tool

🔒 Legal Notice
Please respect copyright laws and YouTube's Terms of Service.

Only download content you have permission to download

Use this tool responsibly

The developer is not responsible for any misuse

🤝 Contributing
Feel free to fork this repository and submit pull requests for improvements.

📄 License
This project is open source and available under the MIT License.

📞 Support
For issues, please open an issue on GitHub or check the yt-dlp documentation.

Happy Downloading! 🎵📹