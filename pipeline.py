import subprocess
from pathlib import Path

import mlx_whisper
from translate import translate

WHISPER = "mlx-community/whisper-small-mlx"
TTS = "mlx-community/Qwen3-TTS-12Hz-1.7B-Base-8bit"


def run(audio):
    result = mlx_whisper.transcribe(
        audio,
        path_or_hf_repo=WHISPER,
        language="en",
    )
    english = result["text"].strip()
    korean = translate(english)

    subprocess.run([
        "uv", "run", "--project", "tts",
        "mlx_audio.tts.generate",
        "--model", TTS,
        "--text", korean,
        "--ref_audio", "tts/reference.wav",
        "--ref_text", "Hello, my name is Ho-Won. This is testing testing. Thank you.",
        "--lang_code", "Korean",
        "--output_path", "tts/output",
    ], check=True)

    output = Path("tts/output/audio_000.wav").resolve()
    return english, korean, str(output)


if __name__ == "__main__":
    print(run("test.m4a"))