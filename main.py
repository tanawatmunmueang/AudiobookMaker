import gradio as gr
from kokoro import KPipeline
import numpy as np
import torch

# 1. Initialize with explicit repo_id to stop the warning
# We also detect device here for speed
device = 'cuda' if torch.cuda.is_available() else 'cpu'
pipeline = KPipeline(lang_code='a', device=device, repo_id='hexgrad/Kokoro-82M')

def tts_engine(text, voice, speed):
    # Kokoro returns a generator; we process it into a single audio array
    generator = pipeline(text, voice=voice, speed=speed, split_pattern=r'\n+')

    all_audio = []
    for _, _, audio in generator:
        all_audio.append(audio)

    if not all_audio:
        return None

    # Concatenate and convert to 16-bit PCM for Gradio compatibility
    full_audio = np.concatenate(all_audio)
    audio_int16 = (full_audio * 32767).astype(np.int16)

    return (24000, audio_int16)

def main():
    # Blocks setup
    with gr.Blocks(title="Audiobook Maker") as demo:
        gr.HTML("""
        <div style="text-align: center; margin-bottom: 1rem;">
          <h1 style="font-size: 2.5em; background: linear-gradient(to right, #0083B0, #00B4DB); -webkit-background-clip: text; background-clip: text; color: transparent;">
            ☁️ The Cozy Narration Station 💖
          </h1>
          <p style="color: #666;">High-speed local TTS powered by Kokoro-82M</p>
        </div>
        """)

        with gr.Row():
            with gr.Column():
                input_text = gr.Textbox(label="Input Text", placeholder="Paste your story here...", lines=10)
                voice_opt = gr.Dropdown(
                    label="Voice",
                    choices=["af_heart", "af_bella", "af_nicole", "af_sarah", "am_adam", "am_echo"],
                    value="af_heart"
                )
                speed_slider = gr.Slider(label="Speed", minimum=0.5, maximum=2.0, value=1.0, step=0.1)
                generate_btn = gr.Button("Generate Narration", variant="primary")

            with gr.Column():
                audio_output = gr.Audio(label="Result", type="numpy")

        # Connect the button to the function
        generate_btn.click(
            fn=tts_engine,
            inputs=[input_text, voice_opt, speed_slider],
            outputs=audio_output
        )

    # 2. Corrected launch (theme moved here for Gradio 6.0 compatibility)
    # Set share=True if you want to send a link to a friend
    demo.launch(inbrowser=True, theme=gr.themes.Monochrome(), share=False)

if __name__ == "__main__":
    main()
