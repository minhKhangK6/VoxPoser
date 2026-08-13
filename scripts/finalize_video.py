import os
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
        print(f"[MISSING] {file}")
        raise SystemExit(1)

    print(f"[OK] {file}")


# ============================================================
# FFMPEG
# ============================================================

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

print("\nFFmpeg:")
print(ffmpeg_exe)


# ============================================================
# PREPARE SUBTITLE PATH
# ============================================================

subtitle_path = os.path.abspath(SUBTITLE_INPUT)

# FFmpeg subtitle filter on Windows:
# 1. convert backslashes to forward slashes
# 2. escape drive-letter colon
subtitle_path = subtitle_path.replace("\\", "/")
subtitle_path = subtitle_path.replace(":", r"\:")

# Avoid the complicated force_style syntax that caused
# the previous parsing error.
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

    # Video input
    "-i",
    VIDEO_INPUT,

    # Audio input
    "-i",
    AUDIO_INPUT,

    # Burn subtitles
    "-vf",
    subtitle_filter,

    # Map video and audio
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

    # Keep exact video length
    "-t",
    "815.40",

    # Better MP4 compatibility
    "-movflags",
    "+faststart",

    OUTPUT_VIDEO,
]


# ============================================================
# RUN
# ============================================================

result = subprocess.run(cmd)


# ============================================================
# RESULT
# ============================================================

if result.returncode != 0:

    print("\n" + "=" * 60)
    print("ERROR: FINAL VIDEO CREATION FAILED")
    print("=" * 60)

    raise SystemExit(result.returncode)


print("\n" + "=" * 60)
print("SUCCESS!")
print("=" * 60)

print(f"Final video: {OUTPUT_VIDEO}")
print("Duration target: 13:35.40")
print("Audio: synchronized voice-over")
print("Subtitle: burned into video")