import os
import asyncio
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError, ExtractorError
from config import Settings


def _ensure_downloads_dir() -> None:
    Settings.DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)


def _download_audio_sync(url: str) -> str:
    _ensure_downloads_dir()

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(Settings.DOWNLOADS_DIR / "%(title)s.%(ext)s"),
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


def _download_video_sync(url: str) -> str:
    """Blocking video download — run inside a thread."""
    _ensure_downloads_dir()

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": str(Settings.DOWNLOADS_DIR / "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegMerger",          # ← properly merges video+audio
        }],
        "merge_output_format": "mp4",       # ← always outputs .mp4
        "quiet": True,
        "no_warnings": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)


async def download_youtube_audio(url: str) -> str:
    """Non-blocking audio download."""
    try:
        return await asyncio.get_event_loop().run_in_executor(
            None, _download_audio_sync, url
        )
    except DownloadError as e:
        raise ValueError(f"Could not download audio: {e}") from e
    except ExtractorError as e:
        raise ValueError(f"Could not extract info from URL: {e}") from e


async def download_youtube_video(url: str) -> str:
    """Non-blocking video download."""
    try:
        return await asyncio.get_event_loop().run_in_executor(
            None, _download_video_sync, url
        )
    except DownloadError as e:
        raise ValueError(f"Could not download video: {e}") from e
    except ExtractorError as e:
        raise ValueError(f"Could not extract info from URL: {e}") from e