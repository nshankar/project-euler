from pathlib import Path


def get_root() -> Path:
    return Path(__file__).parent.parent


def load_data(path: Path):
    with open(path, encoding="utf-8") as file:
        data = [line.strip() for line in file]
    return data

