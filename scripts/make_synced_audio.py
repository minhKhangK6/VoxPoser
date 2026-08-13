import os
import subprocess
import imageio_ffmpeg


# ============================================================
# CONFIG
# ============================================================

VOICE_DIR = "voice"

OUTPUT_AUDIO = "VoxPoser_SyncedVoice.wav"

# Thời lượng thật của từng scene
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
# CHECK VOICE FILES
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
# TÍNH START TIME CỦA TỪNG SCENE
# ============================================================

scene_start_times = []

current_time = 0.0

for duration in SCENE_DURATIONS:

    scene_start_times.append(
        current_time
    )

    current_time += duration


total_video_duration = current_time

print("\n" + "=" * 60)
print(
    f"TOTAL VIDEO TIMELINE: "
    f"{total_video_duration:.2f} seconds"
)
print("=" * 60)


# ============================================================
# TẠO FILE FILTER SCRIPT CHO FFMPEG
# ============================================================
#
# Mỗi voice được:
#   1. delay đến đúng thời điểm scene bắt đầu
#   2. convert sang stereo 48kHz
#
# Sau đó tất cả audio được mix thành một track.
#
# Nếu voice ngắn hơn scene:
#   phần còn lại = silence
#
# ============================================================

filter_parts = []

audio_inputs = []

for i, (
    voice_file,
    start_time
) in enumerate(
    zip(
        voice_files,
        scene_start_times
    )
):

    delay_ms = int(
        round(
            start_time * 1000
        )
    )

    # Input index
    input_index = i

    # audio stream
    filter_parts.append(
        f"[{input_index}:a]"
        f"aformat="
        f"sample_fmts=fltp:"
        f"sample_rates=48000:"
        f"channel_layouts=stereo,"
        f"adelay="
        f"{delay_ms}|{delay_ms}"
        f"[a{i}]"
    )

    audio_inputs.append(
        f"[a{i}]"
    )


# ============================================================
# AMIX
# ============================================================

filter_complex = ";".join(
    filter_parts
)

filter_complex += (
    ";"
    + "".join(audio_inputs)
    + f"amix="
      f"inputs={len(audio_inputs)}:"
      f"duration=longest:"
      f"dropout_transition=0,"
      f"apad="
    + "[mixed]"
)

# ============================================================
# INPUT ARGUMENTS
# ============================================================

cmd = [
    ffmpeg_exe,
    "-y",
]

for voice_file in voice_files:

    cmd.extend(
        [
            "-i",
            voice_file
        ]
    )

# ============================================================
# FILTER
# ============================================================

cmd.extend(
    [
        "-filter_complex",
        filter_complex,

        "-map",
        "[mixed]",

        "-t",
        str(total_video_duration),

        "-ar",
        "48000",

        "-ac",
        "2",

        "-c:a",
        "pcm_s16le",

        OUTPUT_AUDIO,
    ]
)


# ============================================================
# RUN
# ============================================================

print("\n" + "=" * 60)
print("CREATING SYNCHRONIZED VOICE TRACK")
print("=" * 60)

result = subprocess.run(
    cmd
)


# ============================================================
# RESULT
# ============================================================

if result.returncode != 0:

    print(
        "\nERROR: Failed to create synchronized audio."
    )

    raise SystemExit(
        result.returncode
    )


print("\n" + "=" * 60)
print("SUCCESS!")
print("=" * 60)

print(
    f"Output: {OUTPUT_AUDIO}"
)

print(
    f"Duration: {total_video_duration:.2f} seconds"
)