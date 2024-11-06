import os
from app.config import AUDIO_DIR

def save_audio_file(keyNum, file_path):
    user_dir = os.path.join(AUDIO_DIR, keyNum)
    os.makedirs(user_dir, exist_ok=True)
    audio_file_path = os.path.join(user_dir, os.path.basename(file_path))
    os.rename(file_path, audio_file_path)
    return audio_file_path
