# KickNoSub 🎥

KickNoSub is a simple command-line tool that demonstrates how to extract **direct stream URLs** from Kick VODs.  
It is designed purely for **educational and research purposes**, showing how Kick video metadata and streaming formats can be parsed programmatically.  

## 🚀 Features
- Input a Kick video URL  
- Select desired video quality:  
  - 1080p60  
  - 720p60  
  - 480p30  
  - 360p30  
  - 160p30  
- Outputs the **raw stream URL**  
- Example use with **VLC**, **FFmpeg**, or other HLS-compatible players  

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
? Choose video quality:  1080p60
```

Output:
```
✅ Stream URL found!

https://stream.kick.com/...../playlist.m3u8
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

## ⚠️ Legal Disclaimer
This project is provided strictly **for educational, research, and personal learning purposes only**.  

KickNoSub is a demonstration of how public metadata and stream information can be programmatically accessed from Kick’s platform.  
It is **not designed or intended** to:
- Circumvent subscriber-only restrictions or paywalls.  
- Facilitate piracy, redistribution, or unauthorized downloading of content.  
- Be used in any way that violates [Kick Terms of Service](https://kick.com/terms-of-service) or applicable laws.  

By using this project, you agree that:
- You are solely responsible for your actions and any consequences that result.  
- The authors and contributors assume **no liability** for misuse of this tool.  
- You will comply with all relevant laws, regulations, and platform rules.  

If you enjoy content on Kick, please support the creators by subscribing and engaging through the official platform.  

## 🙌 Support
If you find KickNoSub useful, consider giving the project a ⭐ on GitHub!

## 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.