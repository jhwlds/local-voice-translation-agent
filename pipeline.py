import subprocess
import mlx_whisper

from translate import translate

AUDIO = "test.m4a"
WHISPER = "mlx-community/whisper-small-mlx"

# 1. Speech to text
result = mlx_whisper.transcribe(
    AUDIO,
    path_or_hf_repo=WHISPER,
    language="en",
)
english = result["text"].strip()
print("English:", english)

# 2. Translation
korean = translate(english)
print("Korean:", korean)

# 3. Text to speech
subprocess.run([
    "uv", "run", "--project", "tts",
    "mlx_audio.tts.generate",
    "--model", "mlx-community/Qwen3-TTS-12Hz-1.7B-Base-8bit",
    "--text", korean,
    "--ref_audio", "tts/reference.wav",
    "--ref_text", "Hello, my name is Ho-Won. This is testing testing. Thank you.",
    "--lang_code", "Korean",
    "--output_path", "tts/output",
], check=True)

print("Saved to tts/output/audio_000.wav")