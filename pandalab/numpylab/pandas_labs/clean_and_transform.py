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

    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    text_cols = df.select_dtypes(include="object").columns
    for col in text_cols:
        df[col] = df[col].fillna("Unknown")

    df = df.rename(columns=lambda c: c.strip().replace(" ", "_"))

    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        df[f"{col}_zscore"] = (df[col] - df[col].mean()) / df[col].std()

    print("Cleaned and transformed sample:\n", df.head())


if __name__ == "__main__":
    main()
