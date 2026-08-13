import os
import subprocess
import imageio_ffmpeg


# ============================================================
# CONFIG
# ============================================================

VOICE_DIR = "voice"

OUTPUT_AUDIO = "VoxPoser_Voice.mp3"

# Thời lượng thật của 24 scene, lấy từ make_caption.py
SCENE_DURATIONS = [
    51.90,
    36.50,
    28.10,
    30.70,
    34.40,
    49.50,
    41.20,
    35.00,
    37.50,
    25.30,
    26.60,
    30.10,
    43.00,
    30.60,
    24.30,
    27.60,
    24.80,
    24.00,
    26.30,
    43.20,
    32.30,
    33.70,
    35.00,
    43.80,
]


# ============================================================
# KIỂM TRA VOICE FILES
# ============================================================

print("=" * 60)
print("CHECKING 24 VOICE FILES")
print("=" * 60)

voice_files = []

for i in range(1, 25):

    path = os.path.join(
        VOICE_DIR,
        f"scene{i:02d}.mp3"
    )

    if not os.path.exists(path):

        print(
            f"[MISSING] {path}"
        )

        raise SystemExit(1)

    print(
        f"[OK] Scene {i:02d}: {path}"
    )

    voice_files.append(path)


# ============================================================
# FFMPEG
# ============================================================

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()


# ============================================================
# TẠO CONCAT LIST
# ============================================================

concat_file = "voice_concat.txt"

with open(
    concat_file,
    "w",
    encoding="utf-8"
) as f:

    for voice in voice_files:

        absolute = os.path.abspath(
            voice
        ).replace(
            "\\",
            "/"
        )

        f.write(
            f"file '{absolute}'\n"
        )


# ============================================================
# GHÉP 24 VOICE FILE
# ============================================================

print("\n" + "=" * 60)
print("MERGING VOICE FILES")
print("=" * 60)

temp_audio = "VoxPoser_Voice_raw.mp3"

cmd_concat = [
    ffmpeg_exe,
    "-y",
    "-f",
    "concat",
    "-safe",
    "0",
    "-i",
    concat_file,
    "-c:a",
    "libmp3lame",
    "-b:a",
    "192k",
    temp_audio
]

result = subprocess.run(
    cmd_concat
)

if result.returncode != 0:

    print(
        "\nERROR: Failed to merge voice files."
    )

    raise SystemExit(
        result.returncode
    )


# ============================================================
# TẠO AUDIO FINAL
# ============================================================

print("\n" + "=" * 60)
print("CREATING FINAL VOICE TRACK")
print("=" * 60)

cmd_final = [
    ffmpeg_exe,
    "-y",
    "-i",
    temp_audio,

    # Normalize loudness slightly.
    "-af",
    "loudnorm=I=-16:TP=-1.5:LRA=11",

    "-ar",
    "48000",

    "-ac",
    "2",

    "-b:a",
    "192k",

    OUTPUT_AUDIO
]

result = subprocess.run(
    cmd_final
)


# ============================================================
# CLEANUP
# ============================================================

if os.path.exists(
    concat_file
):
    os.remove(
        concat_file
    )

if os.path.exists(
    temp_audio
):
    os.remove(
        temp_audio
    )


# ============================================================
# RESULT
# ============================================================

if result.returncode != 0:

    print(
        "\nERROR: Failed to create final voice track."
    )

    raise SystemExit(
        result.returncode
    )


print(
    "\n" + "=" * 60
)

print(
    "VOICE TRACK CREATED SUCCESSFULLY"
)

print(
    "=" * 60
)

print(
    f"Output: {OUTPUT_AUDIO}"
)