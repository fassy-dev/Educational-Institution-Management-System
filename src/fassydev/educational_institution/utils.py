import random
import time
from pathlib import Path
from .config import BASE_DIR

LOGS_PATH = BASE_DIR / "logs" / "actions.log"
LOGS_PATH.parent.mkdir(exist_ok=True)

def log_action(message: str):
    with open(LOGS_PATH, "a", encoding="utf-8") as f:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

def simulate_loading():
    time.sleep(random.uniform(0.1, 0.3))

def validate_id(id_str: str) -> bool:
    return bool(id_str and id_str.strip())

def normalize_input(text: str) -> str:
    return text.strip() if text else ""
