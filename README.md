# cs479-final

English speech in, Korean speech out — runs fully on your Mac, no cloud APIs.

## Goal

Build a local English-to-Korean speech translation app: transcribe English audio, translate to Korean, synthesize Korean speech, and wrap it in a simple Gradio UI.

## Planned pipeline

1. **Whisper** (OpenAI Whisper Small, mlx-community/whisper-small-mlx) — speech to English text  
2. **A9 or NLLB** — English text to Korean text  
3. **Qwen3-TTS** — Korean text to speech  
4. **Gradio** — upload audio and hear the result  

## Requirements

- Apple Silicon Mac  
- Python 3.11  
- [uv](https://docs.astral.sh/uv/)  
- FFmpeg (not a Python package — install with Homebrew)

## Setup

```bash
uv sync --locked
brew install ffmpeg