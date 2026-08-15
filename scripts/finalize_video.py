import os
import re
import subprocess
import imageio_ffmpeg


# ============================================================
# INPUT FILES
# ============================================================

VIDEO_INPUT = "VoxPoser_Full.mp4"
AUDIO_INPUT = "VoxPoser_SyncedVoice.wav"
SUBTITLE_INPUT = "caption.srt"

OUTPUT_VIDEO = "VoxPoser_Final.mp4"


# ============================================================
# GET VIDEO DURATION
# ============================================================

def get_duration(video_path):

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

    cmd = [
        ffmpeg_exe,
        "-i",
        video_path
    ]

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    match = re.search(
        r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)",
        result.stderr
    )

    if not match:
        raise RuntimeError(
            f"Could not read duration: {video_path}"
        )

    hours = int(match.group(1))
    minutes = int(match.group(2))
    seconds = float(match.group(3))

    return (
        hours * 3600
        + minutes * 60
        + seconds
    )


# ============================================================
# CHECK INPUT FILES
# ============================================================

print("=" * 60)
print("CHECKING FINAL INPUT FILES")
print("=" * 60)

for file in [
    VIDEO_INPUT,
    AUDIO_INPUT,
    SUBTITLE_INPUT,
]:

    if not os.path.exists(file):

        print(
            f"[MISSING] {file}"
        )

        raise SystemExit(1)

    print(
        f"[OK] {file}"
    )


# ============================================================
# VIDEO DURATION
# ============================================================

video_duration = get_duration(
    VIDEO_INPUT
)

print(
    f"\nVideo duration: "
    f"{video_duration:.3f}s"
)


# ============================================================
# FFMPEG
# ============================================================

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

print(
    "\nFFmpeg:"
)

print(
    ffmpeg_exe
)


# ============================================================
# SUBTITLE PATH
# ============================================================

subtitle_path = os.path.abspath(
    SUBTITLE_INPUT
)

subtitle_path = subtitle_path.replace(
    "\\",
    "/"
)

subtitle_path = subtitle_path.replace(
    ":",
    r"\:"
)

subtitle_filter = (
    f"subtitles='{subtitle_path}'"
)


# ============================================================
# FFMPEG COMMAND
# ============================================================

print("\n" + "=" * 60)
print("CREATING FINAL VIDEO")
print("=" * 60)

cmd = [
    ffmpeg_exe,

    "-y",

    # Video
    "-i",
    VIDEO_INPUT,

    # Audio
    "-i",
    AUDIO_INPUT,

    # Burn subtitles
    "-vf",
    subtitle_filter,

    # Streams
    "-map",
    "0:v:0",
    "-map",
    "1:a:0",

    # Video
    "-c:v",
    "libx264",
    "-preset",
    "medium",
    "-crf",
    "18",
    "-pix_fmt",
    "yuv420p",
    "-r",
    "60",

    # Audio
    "-c:a",
    "aac",
    "-b:a",
    "192k",
    "-ar",
    "48000",
    "-ac",
    "2",

    # Never use a hard-coded duration.
    # Match the actual merged video.
    "-t",
    str(video_duration),

    # Compatibility
    "-movflags",
    "+faststart",

    OUTPUT_VIDEO,
]


# ============================================================
# RUN
# ============================================================

result = subprocess.run(
    cmd
)


# ============================================================
# RESULT
# ============================================================

if result.returncode != 0:

    print(
        "\n" + "=" * 60
    )

    print(
        "ERROR: FINAL VIDEO CREATION FAILED"
    )

    print(
        "=" * 60
    )

    raise SystemExit(
        result.returncode
    )


print(
    "\n" + "=" * 60
)

print(
    "SUCCESS!"
)

print(
    "=" * 60
)

print(
    f"Final video: "
    f"{OUTPUT_VIDEO}"
)

print(
    f"Duration: "
    f"{video_duration:.3f}s"
)

print(
    "Audio: synchronized voice-over"
)

print(
    "Subtitle: burned into video"
)