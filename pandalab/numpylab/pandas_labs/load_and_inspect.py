import pandas as pd

from numpylab.utils.dataset_config import get_dataset_path


def load_dataset() -> pd.DataFrame:
    dataset_path = get_dataset_path()
    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {dataset_path}. Update dataset_config.json if needed."
        )
    return pd.read_csv(dataset_path)


def main() -> None:
    df = load_dataset()

    print("Head:\n", df.head())

    print("\nInfo:")
    df.info()

    print("\nDescribe (numeric):\n", df.describe())

    print("\nMissing values:\n", df.isna().sum())


if __name__ == "__main__":
    main()
