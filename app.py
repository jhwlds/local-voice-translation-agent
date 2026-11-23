import gradio as gr
from pipeline import run


def process(audio):
    if audio is None:
        raise gr.Error("Please upload or record an audio file.")

    print("Audio input:", audio)
    return run(str(audio))


demo = gr.Interface(
    fn=process,
    inputs=gr.Audio(
        sources=["upload", "microphone"],
        type="filepath",
        label="English Audio",
    ),
    outputs=[
        gr.Textbox(label="English Transcript"),
        gr.Textbox(label="Korean Translation"),
        gr.Audio(label="Korean Audio"),
    ],
    title="Local Voice Translator",
    description="English speech to Korean speech, running locally.",
)

demo.launch(server_name="127.0.0.1", share=False)