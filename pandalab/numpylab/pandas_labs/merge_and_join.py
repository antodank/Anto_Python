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

    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    if len(cat_cols) == 0:
        print("No categorical column available for merge example.")
        return

    key = cat_cols[0]
    lookup = (
        df[[key]]
        .dropna()
        .drop_duplicates()
        .assign(category_code=lambda d: range(1, len(d) + 1))
    )

    merged = df.merge(lookup, on=key, how="left")
    print(merged[[key, "category_code"]].head())


if __name__ == "__main__":
    main()
