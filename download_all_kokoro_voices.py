from pathlib import Path
from huggingface_hub import HfApi, hf_hub_download
from config import MODEL_DIR, VOICES_DIR, HF_HOME, HF_HUB_OFFLINE, REPO_ID
import os

# -----------------------------
# Ensure folders exist
# -----------------------------
MODEL_DIR.mkdir(parents=True, exist_ok=True)
VOICES_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Set HF Hub to offline-friendly
# -----------------------------
os.environ["HF_HOME"] = HF_HOME
os.environ["HF_HUB_OFFLINE"] = "1" if HF_HUB_OFFLINE else "0"

# -----------------------------
# Hugging Face API
# -----------------------------
api = HfApi()
all_files = api.list_repo_files(REPO_ID)

# Only download relevant files
relevant_files = [
    f for f in all_files if f.startswith(("config/", "model/", "tokenizer/", "voices/"))
]

print(f"Found {len(relevant_files)} files to check/download.")

# -----------------------------
# Counters for summary
# -----------------------------
downloaded_count = 0
skipped_count = 0

# -----------------------------
# Helper function
# -----------------------------
def download_repo_file(file_path: str, index: int, total: int):
    """Download a file from HF Hub preserving folder structure, skip if exists."""
    global downloaded_count, skipped_count
    local_path = MODEL_DIR / file_path
    local_path.parent.mkdir(parents=True, exist_ok=True)

    if local_path.exists():
        print(f"[{index}/{total}] [SKIP] {file_path} already exists.")
        skipped_count += 1
        return

    print(f"[{index}/{total}] [DL] {file_path} downloading...")
    hf_hub_download(
        repo_id=REPO_ID,
        filename=file_path,
        local_dir=MODEL_DIR,
        local_dir_use_symlinks=False
    )
    downloaded_count += 1

# -----------------------------
# Download all files
# -----------------------------
for idx, f in enumerate(relevant_files, start=1):
    download_repo_file(f, idx, len(relevant_files))

# -----------------------------
# Summary
# -----------------------------
print("\n===== DOWNLOAD SUMMARY =====")
print(f"Total files checked: {len(relevant_files)}")
print(f"Files downloaded : {downloaded_count}")
print(f"Files skipped    : {skipped_count}")
print("=============================")
print(f"All Kokoro model files and voices are in: {MODEL_DIR}")
