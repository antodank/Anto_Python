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

    # Fill missing numeric values with the column median to avoid bias.
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Fill missing text values with a clear placeholder.
    text_cols = df.select_dtypes(include="object").columns
    for col in text_cols:
        df[col] = df[col].fillna("Unknown")

    # Rename columns to a consistent style for easier access later.
    df = df.rename(columns=lambda c: c.strip().replace(" ", "_"))

    # Create a derived column using a numeric column if present.
    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        df[f"{col}_zscore"] = (df[col] - df[col].mean()) / df[col].std()

    print("Cleaned and transformed sample:\n", df.head())


if __name__ == "__main__":
    main()
