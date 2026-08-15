# VoxPoser – Physical AI Course Project

## 1. Project Overview

**Team:** NKT  
**Class:** 24C04  

This project presents an educational 3Blue1Brown-inspired visualization of:

> **VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models**

Authors: Wenlong Huang, Chen Wang, Ruohan Zhang, Yunzhu Li, Jiajun Wu, Li Fei-Fei.

Publication venue: **The 7th Conference on Robot Learning (CoRL 2023)**, Proceedings of Machine Learning Research, Volume 229, pages 540–562.

Official publication:
https://proceedings.mlr.press/v229/huang23b.html

Project website:
https://voxposer.github.io/

## 2. What the Video Explains

The video follows the main idea of VoxPoser from a natural-language instruction to physical robot motion:

```text
Language instruction
        ↓
LLM reasoning / code generation
        ↓
Vision-language grounding
        ↓
3D value maps
        ↓
Value-map composition
        ↓
Model-based motion planning
        ↓
6-DoF robot trajectory
        ↓
Closed-loop execution
        ↓
Online adaptation / replanning
```

The visualization covers:

- Language-to-geometry grounding
- RGB-D scene understanding
- Affordance and avoidance value maps
- Rotation, velocity, and gripper maps
- Value-map composition
- Model-based trajectory planning
- 6-DoF end-effector actions
- Closed-loop replanning
- Simulation and real-robot evaluation
- Behavioral commonsense reasoning
- Fine-grained language correction
- Multi-step visual programs
- Online dynamics learning
- Limitations and failure modes

## 3. Video

The completed animation contains **24 Manim scenes** and is approximately **13 minutes 35 seconds** before final submission encoding.

The final submission video should be uploaded separately through the course submission form. The GitHub repository is intended primarily for source code, narration, subtitles, documentation, and reproducibility materials rather than as the storage location for the submission video.

## 4. Repository Structure

Recommended clean repository:

```text
VoxPoser/
├── README.md
│   ├── narration.txt
|   ├──VoxPoser_Full.mp4
|   └──VoxPoser_Voice.mp3
|
│
├── scenes/
│   ├── scene1_intro.py
│   ├── scene2_language.py
│   ├── scene3_architecture.py
│   ├── scene4_perception.py
│   ├── scene5_valuemap_types.py
│   ├── scene6_composition.py
│   ├── scene7_motion_planning.py
│   ├── scene8_6dof_action.py
│   ├── scene9_closed_loop.py
│   ├── scene10_experiments.py
│   ├── scene11_commonsense.py
│   ├── scene12_language_correction.py
│   ├── scene13_multistep.py
│   ├── scene14_dynamics.py
│   ├── scene15_contribution.py
│   ├── scene16_summary.py
│   ├── scene17_results.py
│   ├── scene18_sim_vs_real.py
│   ├── scene19_limitations.py
│   ├── scene20_full_pipeline.py
│   ├── scene21_final.py
│   ├── scene22_llm_program.py
│   ├── scene23_zero_shot.py
│   └── scene24_aha.py
│
├── scripts/
│   ├── merge_videos.py
│   ├── make_caption.py
│   ├── make_voice.py
│   ├── make_audio.py
│   ├── make_synced_audio.py
│   └──finalize_video.py
│
├── media/
│   └── ...
|
├── voice/
│   └── ...
│
product/
│   ├── caption.srt
│   └── caption.docx
|   └──VoxPoser_Final.mp4
```

The exact folder structure can be simplified if preferred, but keeping scenes, build scripts, and submission documents separated makes the repository easier to understand.

## 5. Tools and Environment

The animation was developed with:

- Python
- Manim Community Edition 0.20.1
- FFmpeg
- Edge TTS for free English narration
- Windows + Miniconda

The Manim scenes were rendered at 1920×1080 and 60 FPS.

## 6. Workflow Used

### Step 1 – Create individual Manim scenes

Each part of the paper was implemented as a separate Python scene.

### Step 2 – Render and inspect scenes

Each scene was rendered individually with Manim and visually checked before continuing.

Typical command:

```powershell
manim -pqh scene1_intro.py VoxPoserScene1
```

### Step 3 – Merge the 24 scenes

`merge_videos.py` concatenates the rendered scene videos into:

```text
VoxPoser_Full.mp4
```

### Step 4 – Prepare narration

`narration.txt` contains the English narration corresponding to the 24 scenes.

### Step 5 – Generate subtitles

`make_caption.py` reads the actual scene durations and generates:

```text
caption.srt
```

The subtitle timeline follows the individual scene boundaries.

### Step 6 – Generate narration audio

`make_voice.py` uses free Edge TTS voices to create:

```text
voice/
├── scene01.mp3
├── ...
└── scene24.mp3
```

### Step 7 – Synchronize narration to the video

`make_synced_audio.py` places each scene's narration at its actual video start time and creates:

```text
VoxPoser_SyncedVoice.wav
```

with the same total duration as the animation.

### Step 8 – Final encoding

`finalize_video.py` combines:

```text
VoxPoser_Full.mp4
+
VoxPoser_SyncedVoice.wav
+
caption.srt
```

into the final submission video.

## 7. Why the Repository Does Not Include Render Caches

Manim generates many intermediate files under:

```text
media/
```

including partial movie files and render caches.

These are generated artifacts and should not be committed to GitHub.

The same applies to:

```text
voice/
```

rendered MP4 files, temporary concat lists, test audio, and intermediate outputs.

They can be regenerated from the source and scripts.

## 8. Recommended Files to Keep

### Keep

- All 24 final `scene*.py` source files
- `merge_videos.py`
- `make_caption.py`
- `make_voice.py`
- `make_audio.py`
- `make_synced_audio.py`
- `finalize_video.py`
- `narration.txt`
- `media/`
- `voice/`
- `caption.srt`
- `caption.txt`
- `caption.docx`
- `VoxPoser_Full.mp4`
- `VoxPoser_Voice.mp3`
- `VoxPoser_SyncedVoice.wav`
- `VoxPoser_Final.mp4`
- `README.md`

### Do Not Commit

- partial Manim movie files
- `concat_list.txt`
- `voice_concat.txt`
- `test_voice.mp3`
- `VoxPoser_SyncedVoice.wav`
- rendered intermediate MP4 files
- duplicate Scene 1 files
- old experiment/test scripts
- old SRT files
- temporary screenshots/contact sheets
- Python `__pycache__/`
- `.pyc` files

The final submission video can be kept outside the Git repository and uploaded through the course form.

## 9. Submission Caption

The submission caption is stored in:

```text
docs/caption.docx
```

The caption describes the selected publication, its central technical idea, and the content/style of the video.

## 10. Subtitle

The final subtitle file is:

```text
docs/caption.srt
```

It is a single-language English subtitle file synchronized to the scene-based timeline.

## 11. Reproducibility

To reproduce the visual part:

1. Install Python and Manim Community Edition.
2. Render each scene with Manim.
3. Run `merge_videos.py`.
4. Run `make_caption.py`.
5. Install `edge-tts`.
6. Run `make_voice.py`.
7. Run `make_synced_audio.py`.
8. Run `finalize_video.py`.

## 12. Academic Reference

Huang, W., Wang, C., Zhang, R., Li, Y., Wu, J., & Fei-Fei, L. (2023).

**VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models.**

Proceedings of The 7th Conference on Robot Learning, PMLR 229, 540–562.

Official link:
https://proceedings.mlr.press/v229/huang23b.html

Project page:
https://voxposer.github.io/

## 13. Team

**Team NKT – Class 24C04**

This repository contains the team's Manim-based educational visualization and supporting materials for the Physical AI course project.