# cs479-final

Local English-to-Korean speech translation — everything runs on my Mac, no cloud APIs.

Tested on an M3 MacBook Air (24GB RAM).

## Goal

Take English audio, turn it into Korean speech: transcribe → translate → TTS. Later, wrap the steps in a Gradio UI.

## Pipeline

1. **Whisper Small (MLX)** — English audio → English text  
2. **Translation** — English text → Korean text  
   - **NLLB-200 distilled 600M** (tested, PyTorch MPS)  
   - **A9 Transformer** (planned alternative to NLLB)  
3. **Qwen3-TTS 1.7B Base (8-bit)** — Korean text → audio (voice clone from a reference recording)  
4. **Gradio** — web UI to run the full pipeline (not built yet)

## Requirements

- Apple Silicon Mac  
- Python 3.11  
- [uv](https://docs.astral.sh/uv/)  
- FFmpeg (`brew install ffmpeg`)

You need internet access the first time you run each step so models can download from Hugging Face; after that, inference stays local.

## Setup (two Python environments)

Whisper and NLLB share the main project. Qwen3-TTS uses a separate `tts/` project because it depends on MLX-Audio.

**Main project (Whisper + NLLB):**

```bash
uv sync --locked
```

**TTS project (MLX-Audio):**

```bash
uv sync --project tts --locked
```

## Local tests

### 1. Whisper

Put a short English clip at `test.m4a` in the project root (local only, gitignored):

```bash
uv run mlx_whisper test.m4a --model mlx-community/whisper-small-mlx --language en
```

### 2. NLLB

```bash
uv run python translate.py
```

Prints English input and Korean translation (model loads on MPS).

### 3. Qwen3-TTS

Place your English reference clip at `tts/reference.wav` (gitignored). The `--ref_text` should match what is actually spoken in that recording. Example Korean text from a successful run:

```bash
uv run --project tts mlx_audio.tts.generate \
  --model mlx-community/Qwen3-TTS-12Hz-1.7B-Base-8bit \
  --text "안녕하세요. 저는 호원입니다. 이것은 제 번역 프로젝트의 테스트입니다." \
  --ref_audio tts/reference.wav \
  --ref_text "Hello, my name is Ho-Won. This is testing testing. Thank you." \
  --lang_code Korean \
  --output_path tts/output
```

Output: `tts/output/audio_000.wav`.

## Progress

- [x] Whisper Small (MLX)  
- [x] NLLB-200 distilled 600M (MPS)  
- [x] Qwen3-TTS 1.7B Base 8-bit (reference voice)  
- [ ] A9 Transformer  
- [ ] Gradio app  