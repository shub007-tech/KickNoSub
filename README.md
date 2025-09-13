# KickNoSub 🎥

KickNoSub is a simple command-line tool that extracts the **direct stream URL** from Kick VODs (subscriber-only).  
It allows you to get the `.m3u8` playlist link in your preferred quality and use it with media players or downloaders.  

## 🚀 Features
- Input a Kick video URL  
- Select desired video quality:  
  - 1080p60  
  - 720p60  
  - 480p30  
  - 360p30  
  - 160p30  
- Outputs the **raw stream URL**  
- Works with **VLC**, **FFmpeg**, or any HLS-compatible player  

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Enmn/KickNoSub.git
   cd KickNoSub
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Required libraries:
   - [`kickapi`](https://pypi.org/project/kickapi/)  
   - [`rich`](https://pypi.org/project/rich/)  
   - [`questionary`](https://pypi.org/project/questionary/)  

## 🖥️ Usage

Run the script:
```bash
python kicknosub.py
```

Example:
```
Enter the Kick video URL: https://kick.com/somechannel/video/abcdef
? Choose video quality: 1080p60
```

Output:
```
✅ Stream URL found!

https://stream.kick.com/.../playlist.m3u8
```

## 🎯 Examples

### Play in VLC
1. Open VLC  
2. Go to **Media → Open Network Stream**  
3. Paste the extracted URL  

### Download with FFmpeg
```bash
ffmpeg -i "https://stream.kick.com/.../playlist.m3u8" -c copy output.mp4
```

## 📂 Project Structure
```
KickNoSub/
├── kicknosub.py       # Main script
├── requirements.txt   # Dependencies
└── README.md          # Documentation
```

## ⚠️ Disclaimer
This tool is for **educational purposes only**.  
Please respect content creators and Kick’s **Terms of Service** before using it.  

## 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.