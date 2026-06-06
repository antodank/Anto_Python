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

    if len(df.columns) >= 2:
        subset = df[[df.columns[0], df.columns[1]]]
        print("Two-column subset:\n", subset.head())

    numeric_cols = df.select_dtypes(include="number").columns
    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        filtered = df[df[col] > df[col].median()]
        print(f"\nRows where {col} is above median:\n", filtered.head())

    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        q = df.query(f"{col} > {df[col].mean()}")
        print(f"\nQuery result where {col} > mean:\n", q.head())

    print("\nFirst 3 rows, first 3 columns using iloc:\n", df.iloc[:3, :3])


if __name__ == "__main__":
    main()
