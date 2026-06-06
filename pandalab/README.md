# Pandas Learning Examples

This project is now organized as a Python module with submodules.

- Main package: `numpylab`
- Subpackages: `numpylab.utils`, `numpylab.pandas_labs`

Minimal usage notes for the pandas examples in this workspace.

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

## Run as Module/Submodule (recommended)
From the project root, run submodules with `-m`:

```powershell
python -m numpylab.pandas_labs.load_and_inspect
python -m numpylab.pandas_labs.select_and_filter
python -m numpylab.pandas_labs.clean_and_transform
python -m numpylab.pandas_labs.groupby_and_aggregate
python -m numpylab.pandas_labs.merge_and_join
python -m numpylab.pandas_labs.time_series
```

## Optional Install as Editable Package
```powershell
pip install -e .
```
