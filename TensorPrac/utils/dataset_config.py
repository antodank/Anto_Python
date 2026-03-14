import json
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parents[1] / "config" / "dataset_config.json"


def get_dataset_path() -> Path:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Config not found at {CONFIG_PATH}. Create config/dataset_config.json."
        )
    with CONFIG_PATH.open(encoding="utf-8") as handle:
        config = json.load(handle)
    dataset_path = config.get("dataset_path")
    if not dataset_path:
        raise ValueError("dataset_path is missing in dataset_config.json")
    return Path(dataset_path)
