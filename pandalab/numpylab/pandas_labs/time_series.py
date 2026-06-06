import pandas as pd
from pandas._libs.tslibs.nattype import NaTType

from numpylab.utils.dataset_config import get_dataset_path


def load_dataset() -> pd.DataFrame:
    dataset_path = get_dataset_path()
    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {dataset_path}. Update dataset_config.json if needed."
        )
    return pd.read_csv(dataset_path)


def find_datetime_column(df: pd.DataFrame) -> str | None:
    for col in df.columns:
        parsed: pd.Timestamp | NaTType = pd.to_datetime(df[col], errors="coerce")
        if parsed.notna().mean() > 0.7:
            df[col] = parsed
            return col
    return None


def main() -> None:
    df = load_dataset()

    dt_col = find_datetime_column(df)
    if dt_col is None:
        print("No datetime-like column detected for time series example.")
        return

    df = df.set_index(dt_col).sort_index()

    monthly_counts = df.resample("M").size().rename("records")
    print(monthly_counts.head())


if __name__ == "__main__":
    main()
