import os
import re
import subprocess
import imageio_ffmpeg


# ============================================================
# CONFIG
# ============================================================

VOICE_DIR = "voice"

OUTPUT_AUDIO = "VoxPoser_SyncedVoice.wav"

# 24 rendered scene files
SCENE_FILES = [
    r"media/videos/scene1_intro/1080p60/VoxPoserScene1.mp4",
    r"media/videos/scene2_language/1080p60/VoxPoserScene2.mp4",
    r"media/videos/scene3_architecture/1080p60/VoxPoserScene3.mp4",
    r"media/videos/scene4_perception/1080p60/VoxPoserScene4.mp4",
    r"media/videos/scene5_valuemap_types/1080p60/VoxPoserScene5.mp4",
    r"media/videos/scene6_composition/1080p60/VoxPoserScene6.mp4",
    r"media/videos/scene7_motion_planning/1080p60/VoxPoserScene7.mp4",
    r"media/videos/scene8_6dof_action/1080p60/VoxPoserScene8.mp4",
    r"media/videos/scene9_closed_loop/1080p60/VoxPoserScene9.mp4",
    r"media/videos/scene10_experiments/1080p60/VoxPoserScene10.mp4",
    r"media/videos/scene11_commonsense/1080p60/VoxPoserScene11.mp4",
    r"media/videos/scene12_language_correction/1080p60/VoxPoserScene12.mp4",
    r"media/videos/scene13_multistep/1080p60/VoxPoserScene13.mp4",
    r"media/videos/scene14_dynamics/1080p60/VoxPoserScene14.mp4",
    r"media/videos/scene15_contribution/1080p60/VoxPoserScene15.mp4",
    r"media/videos/scene16_summary/1080p60/VoxPoserScene16.mp4",
    r"media/videos/scene17_results/1080p60/VoxPoserScene17.mp4",
    r"media/videos/scene18_sim_vs_real/1080p60/VoxPoserScene18.mp4",
    r"media/videos/scene19_limitations/1080p60/VoxPoserScene19.mp4",
    r"media/videos/scene20_full_pipeline/1080p60/VoxPoserScene20.mp4",
    r"media/videos/scene21_final/1080p60/VoxPoserScene21.mp4",
    r"media/videos/scene22_llm_program/1080p60/VoxPoserScene22.mp4",
    r"media/videos/scene23_zero_shot/1080p60/VoxPoserScene23.mp4",
    r"media/videos/scene24_aha/1080p60/VoxPoserScene24.mp4",
]

# Scene 1 fallback
SCENE1_FALLBACK = (
    r"media/videos/scene1_intro_v2/1080p60/"
    r"VoxPoserScene1V2.mp4"
)


# ============================================================
# GET VIDEO DURATION
# ============================================================

def get_duration(video_path):
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

    cmd = [
        ffmpeg_exe,
        "-i",
        video_path,
    ]

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="ignore",
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
# RESOLVE SCENE PATH
# ============================================================

def resolve_scene_path(index, path):

    if os.path.exists(path):
        return path

    if index == 1 and os.path.exists(SCENE1_FALLBACK):
        print(
            "[INFO] Scene 1: using existing "
            "VoxPoserScene1V2.mp4"
        )
        return SCENE1_FALLBACK

    return None


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

        print(f"[MISSING] {path}")

        raise SystemExit(1)

    print(
        f"[OK] Scene {i:02d}: {path}"
    )

    voice_files.append(path)


# ============================================================
# CHECK SCENES + GET ACTUAL DURATIONS
# ============================================================

print("\n" + "=" * 60)
print("READING ACTUAL SCENE DURATIONS")
print("=" * 60)

scene_start_times = []

current_time = 0.0

resolved_scenes = []

for i, path in enumerate(
    SCENE_FILES,
    start=1
):

    resolved = resolve_scene_path(
        i,
        path
    )

    if not resolved:
        print(
            f"[MISSING] Scene {i:02d}: {path}"
        )
        raise SystemExit(1)

    duration = get_duration(
        resolved
    )

    resolved_scenes.append(resolved)

    scene_start_times.append(
        current_time
    )

    print(
        f"Scene {i:02d}: "
        f"{duration:.3f}s | "
        f"start = {current_time:.3f}s"
    )

    current_time += duration


total_video_duration = current_time

print("\n" + "=" * 60)
print(
    f"TOTAL VIDEO DURATION: "
    f"{total_video_duration:.3f}s"
)
print("=" * 60)


# ============================================================
# FFMPEG
# ============================================================

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()


# ============================================================
# BUILD FILTER
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
        round(start_time * 1000)
    )

    filter_parts.append(
        f"[{i}:a]"
        f"aformat="
        f"sample_fmts=fltp:"
        f"sample_rates=48000:"
        f"channel_layouts=stereo,"
        f"adelay={delay_ms}|{delay_ms}"
        f"[a{i}]"
    )

    audio_inputs.append(
        f"[a{i}]"
    )


filter_complex = ";".join(
    filter_parts
)

filter_complex += (
    ";"
    + "".join(audio_inputs)
    + f"amix="
      f"inputs={len(audio_inputs)}:"
      f"duration=longest:"
      f"dropout_transition=0:"
      f"normalize=0,"
      f"apad"
      f"[mixed]"
)


# ============================================================
# BUILD COMMAND
# ============================================================

cmd = [
    ffmpeg_exe,
    "-y",
]

for voice_file in voice_files:

    cmd.extend([
        "-i",
        voice_file
    ])

cmd.extend([
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
])


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
    f"Duration: "
    f"{total_video_duration:.3f} seconds"
)