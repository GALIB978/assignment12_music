# Assignment 12 – AI Music Generation

## Group Information

**Group:** Cronous

**Members:**
- Prova Zarin
- Akther Rubina
- Islam K
- Bin Mahamud Galib

## Project

We generated a complete music track using the **ACE-Step 1.5 local music generation model**.

## Model Used

**ACE-Step 1.5 – acestep-v15-turbo**

The model was run locally on a CPU using the ACE-Step application.

## System Architecture

Computer → Python Code → Local ACE-Step 1.5 API → Generated Music (MP3)

## Music Prompt

English, upbeat futuristic electronic pop, energetic drums, punchy synth bass, bright synthesizers, electric guitar, catchy melody, modern polished production, inspiring and optimistic mood, male lead vocal with female backing vocals, memorable anthemic chorus, dynamic arrangement, clear vocals, strong beat, futuristic technology atmosphere, robotics and artificial intelligence theme, emotional bridge, powerful final chorus, clean professional studio sound.

## Lyrics

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

## Generation Settings

- Model: ACE-Step 1.5 Turbo
- Language: English
- BPM: 128
- Key: E Major
- Time Signature: 4/4
- Duration: 165 seconds (2:45)
- Inference Steps: 8
- Task: Text-to-Music
- Thinking: Off
- Audio Format: MP3

## Python Code

The complete Python generation code is included in this repository in:

`generate_music.py`

The code sends our prompt and lyrics to the local ACE-Step API, waits for the generation to finish, downloads the generated MP3 file, and saves the generation metadata.

## Project Files

- `generate_music.py` – complete Python code
- `generated_song.mp3` – generated music
- `generation_metadata.json` – generation information
- `lyrics.txt` – song lyrics
- `prompt.txt` – music generation prompt
- `requirements.txt` – Python dependencies
- `README.md` – project documentation

## How to Run

1. Install and start ACE-Step 1.5 locally.
2. Start the ACE-Step API.
3. Activate the Python environment.
4. Run `generate_music.py`.
5. The generated song is saved as `generated_song.mp3`.

## Why ACE-Step Local?

We selected ACE-Step 1.5 because it can generate music locally without requiring a paid cloud music-generation API. It also gives control over the prompt, lyrics, BPM, key, duration, and other generation settings.

## Result

The final output is a complete English electronic pop song about robotics, artificial intelligence, innovation, and the future of technology.

## Limitations

The generation was performed on a CPU, so the generation process was slower than it would be on a suitable GPU.

## What We Learned

Through this assignment, we learned how a local AI music generation model can create music from natural-language prompts and lyrics. We also learned how to control music generation using parameters such as BPM, key, time signature, duration, and inference steps.

## Technologies

- Python
- ACE-Step 1.5
- Local REST API
- AI Music Generation
- FFmpeg
- MP3

## GitHub Repository

[GitHub Repository](https://github.com/GALIB978/assignment12_music)

## Conclusion

ACE-Step 1.5 successfully generated a complete music track from our own prompt and lyrics. Using a local model gave us more control over the generation process and avoided depending on a paid cloud music-generation service.