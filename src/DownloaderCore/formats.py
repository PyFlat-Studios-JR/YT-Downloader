BASE_YOUTUBE_OPTIONS = {
    "socket_timeout": 15,
    "quiet": True,
    "noprogress": True,
    "overwrites": None,
    "ffmpeg_location": None,
    "outtmpl": None,
    "progress_hooks": [],
    "postprocessor_hooks": [],
}

BASE_YOUTUBE_OPTIONS_VIDEO = {
    **BASE_YOUTUBE_OPTIONS,
    "concurrent_fragments": 2,
    "outtmpl": "{}/%(title)s (%(height)sp).%(ext)s"
}

YOUTUBE_VIDEO = {
    "webpage_url_domain": "youtube.com",
    "video_formats": [
        {
            "extension": "MP4",
            "ID": "video/mp4/custom_res",
            "best_format": False,
            "yt_dlp_options": {
                **BASE_YOUTUBE_OPTIONS_VIDEO,
                "merge_output_format": "mp4",
                "format": "bv[height<={}]+ba[ext=m4a]/b",
            },
        },
        {
            "extension": "MP4",
            "ID": "video/mp4/best",
            "best_format": True,
            "yt_dlp_options": {
                **BASE_YOUTUBE_OPTIONS_VIDEO,
                "merge_output_format": "mp4",
                "format": "bv*+ba[ext=m4a]/b",
            },
        }
    ],
    "audio_formats": [
        {
            "extension": "MP3",
            "ID": "audio/mp3/best",
            "best": True,
            "yt_dlp_options": {
                **BASE_YOUTUBE_OPTIONS,
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            },
        }
    ],
}
