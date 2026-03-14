import pandas as pd

from utils.dataset_config import get_dataset_path


def load_dataset() -> pd.DataFrame:
    dataset_path = get_dataset_path()
    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {dataset_path}. Update dataset_config.json if needed."
        )
    return pd.read_csv(dataset_path)


def main() -> None:
    df = load_dataset()

    # Show the first few rows to confirm data loaded as expected.
    print("Head:\n", df.head())

    # Summarize columns, types, and null counts to understand the schema.
    print("\nInfo:")
    df.info()

    # Describe numeric columns to get a baseline for ranges and distributions.
    print("\nDescribe (numeric):\n", df.describe())

    # Count missing values per column to identify cleanup needs.
    print("\nMissing values:\n", df.isna().sum())


if __name__ == "__main__":
    main()
