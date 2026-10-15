# Assignment 12 – AI Music Generation with ACE-Step 1.5

## Group Information

**Group Name:** Cronous

**Members:**
- Prova Zarin
- Akther Rubina
- Islam K
- Bin Mahamud Galib

---

## Project Description

This project was created for Assignment 12: **AI Music API vs Local Model**.

We used the **ACE-Step 1.5** music generation model locally to generate a complete English song about robotics, artificial intelligence, and the future of technology.

The music was generated locally without using a paid cloud music-generation API.

### Model Used

- **Model:** ACE-Step 1.5
- **Model variant:** `acestep-v15-turbo`
- **Generation type:** Local text-to-music
- **Language:** English
- **Target duration:** 165 seconds (2 minutes 45 seconds)
- **BPM:** 128
- **Key:** E Major
- **Time signature:** 4/4
- **Inference steps:** 8

---

## System Architecture

```text
Python Script
     |
     v
Local ACE-Step REST API
     |
     v
ACE-Step 1.5 Turbo
     |
     v
Generated Music
     |
     v
MP3 File