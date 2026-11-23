
# cs479-final

Local English-to-Korean speech translation with voice cloning. Runs on my Mac without cloud AI APIs.

Tested on an M3 MacBook Air (24GB RAM).

## Goal

Build a local app that converts English speech into Korean speech using speech recognition, machine translation, and voice cloning.

## Pipeline

1. **Whisper Small (MLX)** — English audio → English text
2. **Translation** — English text → Korean text
   - **NLLB-200 distilled 600M** (tested, PyTorch MPS)
   - **A9 Transformer** (my custom model from Assignment 9, planned)
3. **Qwen3-TTS 1.7B Base (8-bit)** — Korean text → Korean speech using a reference voice
4. **Gradio** — Local web interface for uploading audio and viewing results

## Requirements

- Apple Silicon Mac
- Python 3.11
- [uv](https://docs.astral.sh/uv/)
- FFmpeg (`brew install ffmpeg`)

Internet access is required for the initial model downloads. After downloading, model inference runs locally.

## Setup

The project uses two Python environments because NLLB and MLX-Audio require different versions of Transformers.

Clone the repository:

```bash
git clone https://github.com/jhwlds/local-voice-translation-agent.git
cd local-voice-translation-agent
```

Install the main environment (Whisper, NLLB, and Gradio):

```bash
uv sync --locked
```

Install the TTS environment (MLX-Audio):

```bash
uv sync --project tts --locked
```

## Run the App

Qwen3-TTS needs a reference voice recording for voice cloning.

Place a short WAV recording (around 5–15 seconds) at:

```text
tts/reference.wav
```

In `pipeline.py`, update `--ref_text` to match the exact words spoken in the recording.

Start the app:

```bash
uv run python app.py
```

Open the local URL:

```text
http://127.0.0.1:7860
```

The app lets you:

1. Upload or record English audio.
2. Transcribe it using Whisper.
3. Translate the text into Korean using NLLB.
4. Generate Korean speech using Qwen3-TTS.
5. View the transcripts and play the generated audio.

## Individual Tests

### Whisper

Put a short English recording at `test.m4a`:

```bash
uv run mlx_whisper test.m4a --model mlx-community/whisper-small-mlx --language en
```

### NLLB

```bash
uv run python translate.py
```

Prints a sample English sentence and its Korean translation.

### Qwen3-TTS

```bash
uv run --project tts mlx_audio.tts.generate \
  --model mlx-community/Qwen3-TTS-12Hz-1.7B-Base-8bit \
  --text "안녕하세요. 이것은 제 번역 프로젝트입니다." \
  --ref_audio tts/reference.wav \
  --ref_text "Hello, my name is Ho-Won. This is testing testing. Thank you." \
  --lang_code Korean \
  --output_path tts/output
```

Replace `--ref_text` with the transcript of your own reference recording.

### Full Pipeline

```bash
uv run python pipeline.py
```

Uses `test.m4a` as input and saves the generated Korean audio to:

```text
tts/output/audio_000.wav
```

## Current Limitations

- NLLB is currently the only connected translation model.
- Voice cloning uses a fixed reference recording.
- Generated audio uses a fixed output filename.
- The app is currently designed for local use on an Apple Silicon Mac.

## Progress

- [x] Whisper speech recognition
- [x] NLLB English-to-Korean translation
- [x] Qwen3-TTS voice cloning
- [x] Full speech translation pipeline
- [x] Gradio web interface
- [ ] Integrate my A9 Transformer
- [ ] Add translation model selection
- [ ] Add reference voice upload
- [ ] Evaluate translation and speech quality
