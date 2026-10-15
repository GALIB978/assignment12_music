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

[Intro]<br>
Lights are coming on tonight<br>
Machines are waking in the light<br>
Step by step, we start again<br>
Building dreams with code and brain<br><br>

[Verse 1]<br>
I see the circuits come alive<br>
A digital world begins to rise<br>
Robots moving, learning fast<br>
Turning every dream into the future we can grasp<br><br>

Every question, every try<br>
Takes us one step closer to the sky<br><br>

[Pre-Chorus]<br>
We don't know what tomorrow brings<br>
But we can build amazing things<br>
With every failure, every try<br>
We learn to reach a little higher<br><br>

[Chorus]<br>
We code the future, we light the way<br>
Creating tomorrow from today<br>
AI is thinking, robots move<br>
We're finding something new to prove<br><br>

We code the future, side by side<br>
With innovation as our guide<br>
From imagination to reality<br>
We're building the world we want to see<br><br>

[Verse 2]<br>
Sensors watching through the night<br>
Making everything work just right<br>
Machines can see and machines can learn<br>
Every new idea makes the whole world turn<br><br>

Human dreams will lead the way<br>
We're creating something better every day<br><br>

[Chorus]<br>
We code the future, we light the way<br>
Creating tomorrow from today<br>
AI is thinking, robots move<br>
We're finding something new to prove<br><br>

We code the future, side by side<br>
With innovation as our guide<br>
From imagination to reality<br>
We're building the world we want to see<br><br>

[Bridge]<br>
One idea can change the world<br>
One small spark can make it glow<br>
Keep on learning, keep on trying<br>
There is no limit where we can go<br><br>

[Final Chorus]<br>
We code the future, we light the way<br>
Creating tomorrow from today<br>
AI is thinking, robots move<br>
We're finding something new to prove<br><br>

We code the future, side by side<br>
With innovation as our guide<br><br>

[Outro]<br>
We code, we create, we dream, we grow<br>
Together we decide where technology will go

## Generation Settings

- Model: ACE-Step 1.5 Turbo
- Variant: acestep-v15-turbo
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

The generated song has a duration of **165 seconds (2:45)**.

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