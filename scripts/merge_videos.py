import os
import subprocess
import imageio_ffmpeg


# ============================================================
# DANH SÁCH 24 SCENE
# ============================================================

videos = [
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


# ============================================================
# SCENE 1 FALLBACK
# ============================================================
# Bạn chưa cần render lại Scene 1.
# Nếu VoxPoserScene1.mp4 chưa tồn tại, script sẽ dùng
# file VoxPoserScene1V2.mp4 hiện tại của bạn.

scene1_fallback = (
    r"media/videos/scene1_intro_v2/1080p60/"
    r"VoxPoserScene1V2.mp4"
)


# ============================================================
# KIỂM TRA TẤT CẢ SCENE
# ============================================================

print("=" * 60)
print("CHECKING 24 SCENES")
print("=" * 60)

resolved_videos = []
missing = []

for i, video in enumerate(videos, start=1):

    # Scene 1: dùng file mới nếu đã đổi tên
    if i == 1:

        if os.path.exists(video):

            resolved_videos.append(video)

            print(
                f"[OK] Scene 01: {video}"
            )

        elif os.path.exists(scene1_fallback):

            resolved_videos.append(
                scene1_fallback
            )

            print(
                "[OK] Scene 01: "
                "using existing "
                "VoxPoserScene1V2.mp4"
            )

        else:

            missing.append(video)

            print(
                f"[MISSING] Scene 01: {video}"
            )

    # Các scene còn lại
    else:

        if os.path.exists(video):

            resolved_videos.append(video)

            print(
                f"[OK] Scene {i:02d}: {video}"
            )

        else:

            missing.append(video)

            print(
                f"[MISSING] Scene {i:02d}: {video}"
            )


# ============================================================
# NẾU THIẾU FILE
# ============================================================

if missing:

    print("\n" + "=" * 60)
    print("ERROR: MISSING SCENE FILES")
    print("=" * 60)

    print("\nCác file đang thiếu:\n")

    for file in missing:
        print(file)

    print(
        "\nKiểm tra lại tên file hoặc thư mục "
        "rồi chạy lại."
    )

    raise SystemExit(1)


# ============================================================
# LẤY FFMPEG
# ============================================================

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

print("\nFFmpeg:")
print(ffmpeg_exe)


# ============================================================
# TẠO CONCAT LIST
# ============================================================

list_file = "concat_list.txt"

with open(
    list_file,
    "w",
    encoding="utf-8"
) as f:

    for video in resolved_videos:

        abs_path = os.path.abspath(
            video
        ).replace(
            "\\",
            "/"
        )

        f.write(
            f"file '{abs_path}'\n"
        )


# ============================================================
# OUTPUT
# ============================================================

output_video = "VoxPoser_Full.mp4"


# ============================================================
# GHÉP 24 SCENE
# ============================================================

print("\n" + "=" * 60)
print("MERGING 24 SCENES...")
print("=" * 60)

cmd = [
    ffmpeg_exe,

    "-y",

    "-f",
    "concat",

    "-safe",
    "0",

    "-i",
    list_file,

    "-c",
    "copy",

    output_video
]


result = subprocess.run(cmd)


# ============================================================
# XÓA FILE TẠM
# ============================================================

if os.path.exists(list_file):

    os.remove(
        list_file
    )


# ============================================================
# KẾT QUẢ
# ============================================================

if result.returncode == 0:

    print("\n" + "=" * 60)
    print("SUCCESS!")
    print("=" * 60)

    print(
        f"Final video: {output_video}"
    )

else:

    print("\n" + "=" * 60)
    print("ERROR: FFmpeg failed.")
    print("=" * 60)

    raise SystemExit(
        result.returncode
    )