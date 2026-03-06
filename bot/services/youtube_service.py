import os
import asyncio
from pathlib import Path
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError, ExtractorError
from config import settings




def _ensure_dir() -> None:
    settings.DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)


def _audio_sync(url: str) -> str:
    _ensure_dir()

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(settings.DOWNLOADS_DIR / "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": True,
        "no_warnings": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        return os.path.splitext(filename)[0] + ".mp3"


def _video_sync(url: str, quality: str = "720") -> str:
    _ensure_dir()

    ydl_opts = {
        "format": f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]",
        "outtmpl": str(settings.DOWNLOADS_DIR / "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        "quiet": True,
        "no_warnings": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        base = os.path.splitext(filename)[0]
        return base + ".mp4"


async def download_audio(url: str) -> str:
    try:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, _audio_sync, url)
    except (DownloadError, ExtractorError) as e:
        raise ValueError(f"Download failed: {e}") from e


async def download_video(url: str, quality: str = "720") -> str:
    try:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, _video_sync, url, quality)
    except (DownloadError, ExtractorError) as e:
        raise ValueError(f"Download failed: {e}") from e