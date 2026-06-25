import json
from pathlib import Path
from .config import DB_PATH
from .logger import logger
from .utils import simulate_loading


def load_data() -> dict:
    simulate_loading()
    if not DB_PATH.exists():
        return {"students": {}, "teachers": {}}

    try:
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return {
                "students": data.get("students", {}),
                "teachers": data.get("teachers", {})
            }
    except (json.JSONDecodeError, IOError):
        logger.error(f"Ошибка чтения базы данных: {e}")
        print("Ошибка чтения базы данных. Создаю новую.")
        return {"students": {}, "teachers": {}}


def save_data(students: dict, teachers: dict) -> None:
    data = {
        "students": students,
        "teachers": teachers
    }
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logger.debug("Данные успешно сохранены в базу.")
    except IOError as e:
        logger.critical(f"Критическая ошибка при сохранении базы: {e}")
