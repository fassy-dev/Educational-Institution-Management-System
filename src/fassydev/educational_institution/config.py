from pathlib import Path
CURRENT_DIR = Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent.parent
DB_PATH = BASE_DIR / "data" / "db.json"
