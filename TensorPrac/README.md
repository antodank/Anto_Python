# Pandas Learning Examples

Minimal usage notes for the pandas example folders in this workspace.

## Prerequisites
- Python 3.10+ (any recent 3.x should work)
- pandas installed in your active environment

## Virtual Environment (optional)
If you want to use the existing virtual environment in this workspace:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install pandas if needed:

```powershell
pip install pandas
```

## Dataset
The examples read the dataset path from a shared config file:

```
config\dataset_config.json
```

Default value:

```
C:\TempFiles\Clean_Dataset.csv
```

Update `dataset_path` in the JSON if your file is elsewhere.

## Run an Example
Each folder has a single script. Run one like this:

```powershell
python 01_load_and_inspect\load_and_inspect.py
```

Other examples:

```powershell
python 02_select_and_filter\select_and_filter.py
python 03_clean_and_transform\clean_and_transform.py
python 04_groupby_and_aggregate\groupby_and_aggregate.py
python 05_merge_and_join\merge_and_join.py
python 06_time_series\time_series.py
```
