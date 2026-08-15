import asyncio
import os
import re
import edge_tts


# ============================================================
# CONFIG
# ============================================================

NARRATION_FILE = "narration.txt"

OUTPUT_DIR = "voice"

VOICE = "en-US-GuyNeural"

DEFAULT_RATE = "+0%"
VOLUME = "+0%"
PITCH = "+0Hz"


# ============================================================
# PER-SCENE VOICE RATE
# ============================================================

# Adjust only scenes whose actual MP3 duration is longer
# than the corresponding rendered animation.

SCENE_RATES = {
    3: "+7%",
    5: "+6%",
    8: "+8%",
    10: "+8%",
    15: "+17%",
    16: "+14%",
    17: "+12%",
    18: "+15%",
    19: "+20%",
}


# ============================================================
# PARSE NARRATION
# ============================================================

def parse_narration(text):

    pattern = re.compile(
        r"\[SCENE\s+(\d+)\]\s*(.*?)(?=\[SCENE\s+\d+\]|\Z)",
        re.DOTALL
    )

    matches = pattern.findall(text)

    scenes = {}

    for number, body in matches:

        number = int(number)

        body = re.sub(
            r"\s+",
            " ",
            body
        ).strip()

        scenes[number] = body

    return scenes


# ============================================================
# GENERATE ONE SCENE
# ============================================================

async def generate_scene(
    scene_number,
    text
):

    output_file = os.path.join(
        OUTPUT_DIR,
        f"scene{scene_number:02d}.mp3"
    )

    rate = SCENE_RATES.get(
        scene_number,
        DEFAULT_RATE
    )

    print(
        f"[{scene_number:02d}/24] "
        f"Generating {output_file} "
        f"(rate={rate})..."
    )

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate=rate,
        volume=VOLUME,
        pitch=PITCH,
    )

    await communicate.save(
        output_file
    )

    print(
        f"[OK] Scene {scene_number:02d}"
    )


# ============================================================
# MAIN
# ============================================================

async def main():

    if not os.path.exists(
        NARRATION_FILE
    ):

        raise FileNotFoundError(
            f"Cannot find {NARRATION_FILE}"
        )

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )

    with open(
        NARRATION_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        text = f.read()

    scenes = parse_narration(
        text
    )

    print(
        f"Loaded {len(scenes)} scenes."
    )

    if len(scenes) != 24:

        raise RuntimeError(
            "Expected exactly 24 scenes."
        )

    print()
    print("=" * 60)
    print("VOICE RATE SETTINGS")
    print("=" * 60)

    for scene_number in range(1, 25):

        rate = SCENE_RATES.get(
            scene_number,
            DEFAULT_RATE
        )

        print(
            f"Scene {scene_number:02d}: {rate}"
        )

    print()
    print("=" * 60)
    print("GENERATING 24 VOICE FILES")
    print("=" * 60)

    for scene_number in range(
        1,
        25
    ):

        await generate_scene(
            scene_number,
            scenes[scene_number]
        )

    print()
    print("=" * 60)
    print("ALL VOICE FILES GENERATED")
    print("=" * 60)


if __name__ == "__main__":

    asyncio.run(
        main()
    )