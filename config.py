from pathlib import Path

# -----------------------------
# Base project folder
# -----------------------------
BASE_DIR = Path(__file__).parent.resolve()

# -----------------------------
# Kokoro model folder
# -----------------------------
MODEL_DIR = BASE_DIR / "models" / "Kokoro-82M"

# -----------------------------
# Voice packs folder
# -----------------------------
VOICES_DIR = MODEL_DIR / "voices"

# -----------------------------
# TTS settings
# -----------------------------
LANG_CODE = "a"        # 'a' => American English, 'b' => British, etc.
DEFAULT_VOICE = "am_michael"
SAMPLE_RATE = 24000

# -----------------------------
# Hugging Face Hub offline settings
# -----------------------------
# Ensures Kokoro uses the local model folder and does not try to download
HF_HOME = str(MODEL_DIR)
HF_HUB_OFFLINE = True
REPO_ID = "hexgrad/Kokoro-82M"
