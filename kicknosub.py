from datetime import datetime
from kickapi import KickAPI
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import questionary

console = Console()

def get_video_stream_url(video_url: str, quality: str) -> str | None:
    try:
        parts = video_url.split("/")
        channel_name = parts[3]
        video_slug = parts[5]

        kick_api = KickAPI()
        channel = kick_api.channel(channel_name)

        for video in channel.videos:
            if video.uuid == video_slug:
                thumbnail_url = video.thumbnail["src"]
                start_time = datetime.strptime(video.start_time, "%Y-%m-%d %H:%M:%S")
                path_parts = thumbnail_url.split("/")
                channel_id, video_id = path_parts[4], path_parts[5]

                stream_url = (
                    f"https://stream.kick.com/ivs/v1/196233775518/"
                    f"{channel_id}/{start_time.year}/{start_time.month}/"
                    f"{start_time.day}/{start_time.hour}/{start_time.minute}/"
                    f"{video_id}/media/hls/{quality}/playlist.m3u8"
                )
                return stream_url
        return None
    except Exception as e:
        return None

def main():
    # Ask for video URL
    video_url = Prompt.ask("[yellow]Enter the Kick video URL[/yellow]")

    # Ask for quality
    quality = questionary.select(
        "Choose video quality:",
        choices=["1080p60", "720p60", "480p30", "360p30", "160p30"]
    ).ask()

    # Get stream URL
    stream_url = get_video_stream_url(video_url, quality)

    if stream_url:
        console.print("\n[bold green]✅ Stream URL found![/bold green]\n")
        console.print(Panel(stream_url, style="bright_blue"))
    else:
        console.print("[bold red]❌ Video not found or stream URL could not be retrieved.[/bold red]")

if __name__ == "__main__":
    main()