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

    # Find a categorical column and a numeric column for aggregation.
    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    num_cols = df.select_dtypes(include="number").columns

    if len(cat_cols) == 0 or len(num_cols) == 0:
        print("No suitable categorical and numeric columns for groupby example.")
        return

    category = cat_cols[0]
    value = num_cols[0]

    # Group by category and compute summary stats for the numeric column.
    grouped = df.groupby(category)[value].agg(["count", "mean", "min", "max"]).reset_index()
    print(grouped.head())


if __name__ == "__main__":
    main()
