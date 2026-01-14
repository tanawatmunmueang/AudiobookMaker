import os
import soundfile as sf
from kokoro import KPipeline
from config import MODEL_DIR, VOICES_DIR, LANG_CODE, DEFAULT_VOICE, SAMPLE_RATE, HF_HOME, HF_HUB_OFFLINE, REPO_ID

# -----------------------------
# Set Hugging Face Hub to offline mode
# -----------------------------
os.environ["HF_HOME"] = HF_HOME
os.environ["HF_HUB_OFFLINE"] = "1" if HF_HUB_OFFLINE else "0"

# -----------------------------
# Initialize Kokoro pipeline
# -----------------------------
pipeline = KPipeline(
    lang_code=LANG_CODE,
    repo_id=REPO_ID
)

# -----------------------------
# Detect available voices dynamically
# -----------------------------
available_voices = [f.stem for f in VOICES_DIR.glob("*.pt")]
if not available_voices:
    raise RuntimeError(f"No voices found in {VOICES_DIR}. Run the download script first!")

print(f"Available voices ({len(available_voices)}): {available_voices}")

# -----------------------------
# Select voice
# -----------------------------
voice_to_use = DEFAULT_VOICE
if voice_to_use not in available_voices:
    print(f"Warning: default voice '{voice_to_use}' not found. Using first available voice instead.")
    voice_to_use = available_voices[0]

print(f"Using voice: {voice_to_use}")

# -----------------------------
# Text to synthesize
# -----------------------------
text = """
 After another violent rumbling, his head hit the headboard of the bed, filling him with yet another outburst of unbearable pain as he passed out soon after .

 Nobody knew how long it had been, perhaps one day or perhaps several days, when he finally regained consciousness and could feel his body once more .

 He heard the soft sound of a door closing .

 "Has mother left already?" A girl’s voice asked .
"""

# -----------------------------
# Generate audio
# -----------------------------
generator = pipeline(
    text,
    voice=voice_to_use,
    speed=1,
    split_pattern=r"\n+"
)

for i, (gs, ps, audio) in enumerate(generator):
    print(f"Generated chunk {i}")
    print("Text:", gs)
    print("Phonemes:", ps)
    sf.write(f"{i}.wav", audio, SAMPLE_RATE)

print("All audio files generated successfully.")
