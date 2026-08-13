import os
import re
import subprocess
import imageio_ffmpeg


# ============================================================
# FILE CẤU HÌNH
# ============================================================

NARRATION_FILE = "narration.txt"
OUTPUT_SRT = "caption.srt"

# 24 scene theo đúng thứ tự final video
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

# Scene 1 fallback nếu bạn chưa đổi tên lại file MP4.
SCENE1_FALLBACK = (
    r"media/videos/scene1_intro_v2/1080p60/"
    r"VoxPoserScene1V2.mp4"
)

# ============================================================
# GIỌNG ĐỌC ƯỚC LƯỢNG
# ============================================================
# 145 từ/phút là tốc độ tương đối dễ nghe.
# Script sẽ dùng giá trị này để kiểm tra narration có vừa scene không.
WORDS_PER_MINUTE = 145.0

# Subtitle nên ngắn, dễ đọc.
MAX_WORDS_PER_CAPTION = 14

# Khoảng nghỉ giữa các caption.
CAPTION_GAP = 0.08


# ============================================================
# TIME FORMAT
# ============================================================

def format_srt_time(seconds):
    """Convert seconds -> HH:MM:SS,mmm"""

    if seconds < 0:
        seconds = 0

    milliseconds = int(round(seconds * 1000))

    hours = milliseconds // 3_600_000
    milliseconds %= 3_600_000

    minutes = milliseconds // 60_000
    milliseconds %= 60_000

    secs = milliseconds // 1000
    milliseconds %= 1000

    return (
        f"{hours:02d}:"
        f"{minutes:02d}:"
        f"{secs:02d},"
        f"{milliseconds:03d}"
    )


# ============================================================
# FFPROBE
# ============================================================

def get_duration(video_path):
    """Get exact video duration using FFmpeg bundled with imageio."""

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

    # ffprobe is normally not bundled separately by imageio-ffmpeg.
    # Instead, use ffmpeg itself to inspect duration.
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

    output = result.stderr

    # Example:
    # Duration: 00:00:49.03
    match = re.search(
        r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)",
        output
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
# RESOLVE SCENE 1
# ============================================================

def resolve_scene_path(index, path):
    if os.path.exists(path):
        return path

    if index == 1 and os.path.exists(SCENE1_FALLBACK):
        print(
            "[INFO] Scene 1: "
            "using existing VoxPoserScene1V2.mp4"
        )
        return SCENE1_FALLBACK

    return None


# ============================================================
# READ NARRATION
# ============================================================

def read_narration():
    if not os.path.exists(NARRATION_FILE):
        raise FileNotFoundError(
            f"Cannot find {NARRATION_FILE}"
        )

    with open(
        NARRATION_FILE,
        "r",
        encoding="utf-8"
    ) as f:
        return f.read()


# ============================================================
# PARSE SCENES
# ============================================================

def parse_scene_narration(text):
    """
    Read:
        [SCENE 01]
        narration...

        [SCENE 02]
        narration...

    Return:
        {
            1: "...",
            2: "...",
            ...
        }
    """

    pattern = re.compile(
        r"\[SCENE\s+(\d+)\]\s*(.*?)(?=\[SCENE\s+\d+\]|\Z)",
        re.DOTALL
    )

    matches = pattern.findall(text)

    scene_text = {}

    for number, body in matches:
        number = int(number)
        body = body.strip()

        scene_text[number] = body

    return scene_text


# ============================================================
# SPLIT SENTENCES
# ============================================================

def split_sentences(text):
    """
    Split narration into sentence-like chunks.
    """

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    # Split after ., !, ?
    sentences = re.split(
        r"(?<=[.!?])\s+",
        text
    )

    return [
        s.strip()
        for s in sentences
        if s.strip()
    ]


# ============================================================
# SPLIT LONG SENTENCE
# ============================================================

def split_long_sentence(sentence):
    words = sentence.split()

    if len(words) <= MAX_WORDS_PER_CAPTION:
        return [sentence]

    chunks = []

    current = []

    for word in words:

        current.append(word)

        if len(current) >= MAX_WORDS_PER_CAPTION:

            chunks.append(
                " ".join(current)
            )

            current = []

    if current:
        chunks.append(
            " ".join(current)
        )

    return chunks


# ============================================================
# MAKE CAPTIONS
# ============================================================

def make_caption_chunks(text):

    sentences = split_sentences(text)

    chunks = []

    for sentence in sentences:

        parts = split_long_sentence(sentence)

        for part in parts:

            word_count = len(
                part.split()
            )

            # Estimated reading time
            duration = (
                word_count
                / WORDS_PER_MINUTE
                * 60.0
            )

            # Give very short captions a readable minimum
            duration = max(
                duration,
                1.2
            )

            chunks.append(
                {
                    "text": part,
                    "duration": duration
                }
            )

    return chunks


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 65)
    print("VOXPOSER SUBTITLE GENERATOR")
    print("=" * 65)

    # ------------------------------------------------------------
    # Load narration
    # ------------------------------------------------------------

    narration = read_narration()

    scene_narration = parse_scene_narration(
        narration
    )

    print(
        f"\nLoaded narration for "
        f"{len(scene_narration)} scenes."
    )

    # ------------------------------------------------------------
    # Check all 24 scenes
    # ------------------------------------------------------------

    scene_durations = {}

    print("\nReading actual scene durations...\n")

    for i, path in enumerate(
        SCENE_FILES,
        start=1
    ):

        resolved = resolve_scene_path(
            i,
            path
        )

        if not resolved:

            raise FileNotFoundError(
                f"Scene {i:02d} not found:\n"
                f"{path}"
            )

        duration = get_duration(
            resolved
        )

        scene_durations[i] = duration

        print(
            f"Scene {i:02d}: "
            f"{duration:.2f} sec"
        )

    # ------------------------------------------------------------
    # Generate captions
    # ------------------------------------------------------------

    all_entries = []

    current_global_time = 0.0

    warnings = []

    entry_number = 1

    print("\nChecking narration timing...\n")

    for scene_number in range(
        1,
        25
    ):

        scene_duration = scene_durations[
            scene_number
        ]

        text = scene_narration.get(
            scene_number,
            ""
        )

        if not text:

            warnings.append(
                f"Scene {scene_number:02d}: "
                "NO NARRATION"
            )

            current_global_time += scene_duration
            continue

        chunks = make_caption_chunks(
            text
        )

        estimated_voice_duration = sum(
            chunk["duration"]
            for chunk in chunks
        )

        print(
            f"Scene {scene_number:02d}: "
            f"animation = {scene_duration:.2f}s, "
            f"estimated narration = "
            f"{estimated_voice_duration:.2f}s"
        )

        # --------------------------------------------------------
        # Warning if voice is too long
        # --------------------------------------------------------

        if estimated_voice_duration > scene_duration:

            difference = (
                estimated_voice_duration
                - scene_duration
            )

            warnings.append(
                f"Scene {scene_number:02d}: "
                f"narration is about "
                f"{difference:.1f}s too long"
            )

        # --------------------------------------------------------
        # Temporarily scale chunks to fit scene
        #
        # IMPORTANT:
        # This does NOT change narration speed.
        # It only creates a preliminary SRT timeline.
        # We will use the warning above to revise narration.
        # --------------------------------------------------------

        scene_start = current_global_time

        available_duration = max(
            scene_duration - 0.15,
            0.5
        )

        total_estimated = max(
            estimated_voice_duration,
            0.001
        )

        scale = min(
            1.0,
            available_duration
            / total_estimated
        )

        cursor = scene_start

        for chunk in chunks:

            duration = (
                chunk["duration"]
                * scale
            )

            start_time = cursor

            end_time = min(
                cursor + duration,
                scene_start
                + available_duration
            )

            all_entries.append(
                {
                    "number": entry_number,
                    "start": start_time,
                    "end": end_time,
                    "text": chunk["text"]
                }
            )

            entry_number += 1

            cursor = (
                end_time
                + CAPTION_GAP
            )

        current_global_time += scene_duration

    # ------------------------------------------------------------
    # Write SRT
    # ------------------------------------------------------------

    with open(
        OUTPUT_SRT,
        "w",
        encoding="utf-8"
    ) as f:

        for entry in all_entries:

            f.write(
                f"{entry['number']}\n"
            )

            f.write(
                f"{format_srt_time(entry['start'])}"
                f" --> "
                f"{format_srt_time(entry['end'])}\n"
            )

            f.write(
                f"{entry['text']}\n\n"
            )

    # ------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------

    total_duration = sum(
        scene_durations.values()
    )

    print("\n" + "=" * 65)
    print("DONE")
    print("=" * 65)

    print(
        f"Video duration: "
        f"{total_duration:.2f} sec"
    )

    print(
        f"SRT file: "
        f"{OUTPUT_SRT}"
    )

    print(
        f"Subtitle entries: "
        f"{len(all_entries)}"
    )

    if warnings:

        print("\n" + "=" * 65)
        print("IMPORTANT WARNINGS")
        print("=" * 65)

        for warning in warnings:
            print(
                "[WARNING]",
                warning
            )

        print(
            "\nThe SRT was generated, "
            "but narration should be revised "
            "for scenes with timing warnings."
        )

    else:

        print(
            "\nNo narration timing warnings."
        )


if __name__ == "__main__":
    main()