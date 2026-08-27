# 🎬CLI YouTube Videos Downloader

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/yt--dlp-Powered-red?style=for-the-badge" alt="yt-dlp">
  <img src="https://img.shields.io/badge/FFmpeg-Required-007808?style=for-the-badge&logo=ffmpeg&logoColor=white" alt="FFmpeg">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

<p align="center">
  <b>⚡ A simple, fast & powerful YouTube downloader built with Python.</b>
  <br>
  Download videos in high-quality MP4 or extract audio as MP3 with ease.
</p>

<p align="center">
  🎥 Video &nbsp; • &nbsp; 🎵 Audio &nbsp; • &nbsp; ⚡ Fast &nbsp; • &nbsp; 🐍 Python
</p>

---

## ✨ Features

| Feature                | Description                                                  |
| ---------------------  | ------------------------------------------------------------ |
| 🎥 **MP4 Download**   | Download YouTube videos with the best available quality      |
| 🎵 **MP3 Extraction** | Extract audio and save it as a high-quality MP3              |
| ⚡ **Best Quality**   | Automatically selects the best available video/audio streams |
| 🔀 **Auto Merge**     | Automatically merges video and audio using FFmpeg            |
| 🖥️ **Simple CLI**     | Clean and beginner-friendly command-line interface           |
| 📁 **Auto Naming**    | Files are automatically saved using the video title          |
| 🛠️ **Easy Setup**     | Minimal dependencies and straightforward installation        |

---

## 🖼️ How It Works

```text
       ┌──────────────────────┐
       │   🔗 YouTube URL     │
       └──────────┬───────────┘
                  │
                  ▼
       ┌──────────────────────┐
       │   📋 Select Format   │
       └──────────┬───────────┘
                  │
          ┌───────┴───────┐
          ▼               ▼
     ┌─────────┐      ┌─────────┐
     │ 🎥 MP4  │      │ 🎵 MP3 │
     └────┬────┘      └────┬────┘
          │                │
          ▼                ▼
     ┌─────────────────────────┐
     │       ⚡ yt-dlp         │
     │       🔧 FFmpeg         │
     └────────────┬────────────┘
                  │
                  ▼
          📁 Downloaded File
```

---

## 🚀 Installation

### 📋 Prerequisites

Before starting, make sure you have:

* 🐍 **Python 3.6 or higher**
* 📦 **pip**
* 🔧 **FFmpeg**
* 🌐 A working internet connection

---

### 1️⃣ Install FFmpeg

FFmpeg is required for:

* 🔀 Merging video + audio
* 🎵 Extracting MP3 audio
* 🎚️ Media conversion

#### 🪟 Windows

Download FFmpeg from the official website and add its `bin` directory to your system `PATH`.

#### 🍎 macOS

```bash
brew install ffmpeg
```

#### 🐧 Ubuntu / Debian

```bash
sudo apt update
sudo apt install ffmpeg
```

Verify the installation:

```bash
ffmpeg -version
```

---

### 2️⃣ Install yt-dlp

Install the required Python package:

```bash
pip install yt-dlp
```

To update yt-dlp later:

```bash
pip install --upgrade yt-dlp
```

---

## 📥 Usage

Clone or download this project and run:

```bash
python main.py
```

You'll see a simple menu:

```text
╔════════════════════════════════════╗
║      🎬 YOUTUBE DOWNLOADER         ║
╚════════════════════════════════════╝

Enter Your URL > https://www.youtube.com/watch?v=xxxxxxxxxxx

Choose Download Format:

1. 🎥 MP4
2. 🎵 MP3

Enter your choice > 1
```

Once the download is complete:

```text
╔════════════════════════════════════╗
║       ✅ DOWNLOAD COMPLETED        ║
╚════════════════════════════════════╝
```

🎉 Your file will be saved in the current working directory.

---

## 🎥 Download MP4

Select:

```text
1. MP4
```

The downloader will:

1. 🔎 Find the best available video stream
2. 🔊 Find the best available audio stream
3. 📥 Download both streams
4. 🔀 Merge them using FFmpeg
5. 💾 Save the final file as `.mp4`

Example:

```text
📁 My Awesome Video.mp4
```

---

## 🎵 Extract MP3

Select:

```text
2. MP3
```

The downloader extracts the audio and converts it to MP3.

Default audio quality:

```text
🎚️ 192 kbps
```

Example:

```text
📁 My Awesome Video.mp3
```

---

## 📁 Output Structure

Downloaded files are stored in your current directory:

```text
📂 youtube-downloader/
│
├── 🐍 main.py
│
├── 🎥 Video Title.mp4
├── 🎵 Music Title.mp3
│
└── 📄 README.md
```

---

## ⚙️ Configuration

### 🎥 MP4

The MP4 option is configured to:

```text
Best Video
     +
Best Audio
     ↓
  FFmpeg
     ↓
  MP4 File
```

This allows the downloader to obtain the highest-quality streams available and combine them into one file.

### 🎵 MP3

The MP3 option:

```text
YouTube Audio
      ↓
   FFmpeg
      ↓
  MP3 192 kbps
```

---

## 🛑 Exit Commands

You can quit the program using:

```text
exit
clear
stop
ok
```

---

## 🔧 Troubleshooting

### ❌ `FFmpeg not found`

Make sure FFmpeg is installed correctly.

Check:

```bash
ffmpeg -version
```

If the command isn't recognized, add FFmpeg's `bin` folder to your system `PATH`.

---

### ❌ Download Failed

Try the following:

```bash
pip install --upgrade yt-dlp
```

Then verify:

* 🌐 Your internet connection
* 🔗 The YouTube URL
* 📦 yt-dlp installation
* 🔧 FFmpeg installation

---

### ❌ Poor Audio / Video Quality

Quality depends on what streams are available for the specific video.

Some videos may not provide higher-quality streams.

---

### ❌ Region Restricted Video

Some YouTube content may be unavailable in your region.

In such cases, the downloader may not be able to access the video.

---

## 📦 Dependencies

### 🐍 Python

The application is written in Python.

### 📥 yt-dlp

Handles video/audio downloading and stream selection.

### 🔧 FFmpeg

Used for:

* Video + audio merging
* Audio extraction
* Format conversion

---

## 🔐 Legal & Responsible Use

> ⚠️ **Important:** Please use this project responsibly.

Only download content when you have the necessary rights or permission to do so.

You are responsible for complying with:

* ©️ Copyright laws
* 📜 YouTube's Terms of Service
* 🌍 Applicable local laws and regulations

The developer is **not responsible for misuse** of this software.

---

## 🤝 Contributing

Contributions are welcome! ❤️

If you have an idea or improvement:

1. 🍴 Fork the repository
2. 🌿 Create a new branch
3. ✨ Make your changes
4. 💾 Commit your changes
5. 🚀 Open a Pull Request

Example:

```bash
git checkout -b feature/my-new-feature
git commit -m "Add new feature"
git push origin feature/my-new-feature
```

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute the project according to the license terms.

---

## 💬 Support

Found a bug or have a suggestion?

🐛 Open an issue on GitHub.

📚 For yt-dlp related problems, check the official yt-dlp documentation.

---

## ⭐ Show Your Support

If this project helped you, consider giving it a ⭐ on GitHub!

It really helps support the project. ❤️

```text
╔══════════════════════════════════════════╗
║                                          ║
║       🎬 Happy Downloading! 🎵          ║
║                                          ║
║          Made with ❤️ & Python 🐍       ║
║                                          ║
╚══════════════════════════════════════════╝
```

<p align="center">
  <b>⭐ Star the repository if you like it!</b>
</p>
