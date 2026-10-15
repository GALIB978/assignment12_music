import json
import time
from pathlib import Path
from urllib.parse import quote

import requests


# ============================================================
# ACE-Step 1.5 Local Music Generation
# Assignment 12 - AI Music API vs Local Model
# ============================================================

API_URL = "http://127.0.0.1:7860"

MODEL = "acestep-v15-turbo"
DURATION = 165          # 2 minutes 45 seconds
BPM = 128
KEY_SCALE = "E Major"
TIME_SIGNATURE = "4"
INFERENCE_STEPS = 8


PROMPT = """
English, upbeat futuristic electronic pop, energetic drums, punchy synth bass,
bright synthesizers, electric guitar, catchy melody, modern polished production,
inspiring and optimistic mood, male lead vocal with female backing vocals,
memorable anthemic chorus, dynamic arrangement, clear vocals, strong beat,
futuristic technology atmosphere, robotics and artificial intelligence theme,
emotional bridge, powerful final chorus, clean professional studio sound.
""".strip()


LYRICS = """
[Intro]
Lights are coming on tonight
Machines are waking in the light
Step by step, we start again
Building dreams with code and brain

[Verse 1]
I see the circuits come alive
A digital world begins to rise
Robots moving, learning fast
Turning every dream into the future we can grasp

Every question, every try
Takes us one step closer to the sky

[Pre-Chorus]
We don't know what tomorrow brings
But we can build amazing things
With every failure, every try
We learn to reach a little higher

[Chorus]
We code the future, we light the way
Creating tomorrow from today
AI is thinking, robots move
We're finding something new to prove

We code the future, side by side
With innovation as our guide
From imagination to reality
We're building the world we want to see

[Verse 2]
Sensors watching through the night
Making everything work just right
Machines can see and machines can learn
Every new idea makes the whole world turn

Human dreams will lead the way
We're creating something better every day

[Chorus]
We code the future, we light the way
Creating tomorrow from today
AI is thinking, robots move
We're finding something new to prove

We code the future, side by side
With innovation as our guide
From imagination to reality
We're building the world we want to see

[Bridge]
One idea can change the world
One small spark can make it glow
Keep on learning, keep on trying
There is no limit where we can go

[Final Chorus]
We code the future, we light the way
Creating tomorrow from today
AI is thinking, robots move
We're finding something new to prove

We code the future, side by side
With innovation as our guide

[Outro]
We code, we create, we dream, we grow
Together we decide where technology will go
""".strip()


OUTPUT_DIR = Path(__file__).parent
OUTPUT_FILE = OUTPUT_DIR / "generated_song.mp3"
METADATA_FILE = OUTPUT_DIR / "generation_metadata.json"


def submit_generation():
    """Send the music generation task to the local ACE-Step API."""

    payload = {
        "prompt": PROMPT,
        "lyrics": LYRICS,
        "model": MODEL,
        "thinking": False,
        "vocal_language": "en",
        "audio_format": "mp3",
        "bpm": BPM,
        "key_scale": KEY_SCALE,
        "time_signature": TIME_SIGNATURE,
        "audio_duration": DURATION,
        "inference_steps": INFERENCE_STEPS,
        "batch_size": 1,
        "task_type": "text2music",
        "use_random_seed": True,
        "use_cot_caption": False,
        "use_cot_language": False,
    }

    print("Submitting music generation task...")
    print(f"Model: {MODEL}")
    print(f"Target duration: {DURATION} seconds (2:45)")
    print(f"BPM: {BPM}")
    print(f"Key: {KEY_SCALE}")
    print()

    response = requests.post(
        f"{API_URL}/release_task",
        json=payload,
        timeout=60,
    )

    response.raise_for_status()

    data = response.json()

    print("Task submitted successfully.")
    print("Response:", data)

    task_ids = data.get("task_id_list", [])

    if not task_ids:
        raise RuntimeError("No task ID was returned by ACE-Step API.")

    return task_ids[0]


def wait_for_result(task_id):
    """Wait until ACE-Step finishes generating the music."""

    print()
    print("Waiting for ACE-Step to finish...")
    print("This may take several minutes on CPU.")
    print()

    while True:
        response = requests.post(
            f"{API_URL}/query_result",
            json={"task_id_list": [task_id]},
            timeout=60,
        )

        response.raise_for_status()

        data = response.json()

        results = data.get("results", [])

        if results:
            result = results[0]

            status = result.get("status")

            print(f"Task status: {status}")

            if status == 1:
                print("Music generation completed successfully!")
                return result

            if status == 2:
                raise RuntimeError(
                    f"Music generation failed:\n{result}"
                )

        time.sleep(5)


def download_audio(result):
    """Download the generated MP3 from ACE-Step."""

    result_data = result.get("result")

    if isinstance(result_data, str):
        result_data = json.loads(result_data)

    if not isinstance(result_data, dict):
        raise RuntimeError("Could not read generation result.")

    audio_path = result_data.get("audio_path")

    if not audio_path:
        audio_path = result_data.get("file_url")

    if not audio_path:
        raise RuntimeError(
            "ACE-Step completed the task but no audio path was returned."
        )

    print()
    print("Downloading generated audio...")
    print(f"Audio path: {audio_path}")

    if audio_path.startswith("http"):
        audio_url = audio_path
    else:
        audio_url = (
            f"{API_URL}/v1/audio?path={quote(audio_path)}"
        )

    response = requests.get(audio_url, timeout=120)

    response.raise_for_status()

    OUTPUT_FILE.write_bytes(response.content)

    print()
    print(f"MP3 saved successfully:")
    print(OUTPUT_FILE)


def save_metadata(task_id, result):
    """Save the generation settings and task information."""

    metadata = {
        "assignment": "Assignment 12 - AI Music API vs Local Model",
        "group": "Cronous",
        "members": [
            "Prova Zarin",
            "Akther Rubina",
            "Islam K",
            "Bin Mahamud Galib",
        ],
        "model": MODEL,
        "generation_method": "Local ACE-Step 1.5 REST API",
        "task_id": task_id,
        "target_duration_seconds": DURATION,
        "target_duration": "2:45",
        "bpm": BPM,
        "key_scale": KEY_SCALE,
        "time_signature": "4/4",
        "vocal_language": "English",
        "inference_steps": INFERENCE_STEPS,
        "thinking": False,
        "prompt": PROMPT,
        "lyrics": LYRICS,
    }

    METADATA_FILE.write_text(
        json.dumps(metadata, indent=4),
        encoding="utf-8",
    )

    print(f"Metadata saved successfully:")
    print(METADATA_FILE)


def main():
    print("=" * 60)
    print("ACE-Step 1.5 - Assignment 12 Music Generator")
    print("=" * 60)
    print()

    try:
        task_id = submit_generation()

        result = wait_for_result(task_id)

        download_audio(result)

        save_metadata(task_id, result)

        print()
        print("=" * 60)
        print("DONE!")
        print("=" * 60)
        print(f"Song: {OUTPUT_FILE}")
        print(f"Metadata: {METADATA_FILE}")

    except requests.RequestException as error:
        print()
        print("API connection error:")
        print(error)

    except Exception as error:
        print()
        print("Generation error:")
        print(error)


if __name__ == "__main__":
    main()