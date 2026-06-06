import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"],
}   
df = pd.DataFrame(data)

print(df)

df1 = pd.read_csv("00_loaddata/cities.csv")
df1.columns = df1.columns.str.strip(' "')  # Remove spaces and quotes from column names
print(df1.head())

# ========================================
# PANDAS EXAMPLES USING CITIES DATASET
# ========================================

# ===== SERIES EXAMPLE =====
# A Series is a single column from a DataFrame
print("\n===== SERIES EXAMPLE =====")
city_series = df1["City"]
print("Type:", type(city_series))
print("First 3 cities:")
print(city_series.head(3))

# ===== HEAD EXAMPLE =====
# Show first N rows (default is 5)
print("\n===== HEAD EXAMPLE =====")
print("First 3 rows:")
print(df1.head(3))

# ===== TAIL EXAMPLE =====
# Show last N rows (default is 5)
print("\n===== TAIL EXAMPLE =====")
print("Last 3 rows:")
print(df1.tail(3))

# ===== INFO EXAMPLE =====
# Display DataFrame structure: columns, types, non-null counts, memory usage
print("\n===== INFO EXAMPLE =====")
df1.info()

# ===== DESCRIBE EXAMPLE =====
# Statistical summary of numeric columns
print("\n===== DESCRIBE EXAMPLE =====")
print(df1.describe())

# ===== COLUMNS EXAMPLE =====
# List all column names
print("\n===== COLUMNS EXAMPLE =====")
print("Column names:")
print(df1.columns.tolist())
print("\nNumber of columns:", len(df1.columns))

# ===== CONDITIONS EXAMPLE =====
# Filter rows based on conditions
print("\n===== CONDITIONS EXAMPLE =====")

# Single condition: Cities with LatD greater than 45
northern_cities = df1[df1["LatD"] > 45]
print("Cities with LatD > 45 (northernmost cities):")
print(northern_cities[["City", "State", "LatD"]].head())

# Multiple conditions: Cities in CA or WA
west_coast = df1[(df1["State"] == "CA") | (df1["State"] == "WA")]
print("\nCities in CA or WA:")
print(west_coast[["City", "State"]].head())

# AND condition: Cities in CA with LatD > 37
ca_north = df1[(df1["State"] == "CA") & (df1["LatD"] > 37)]
print("\nCities in CA with LatD > 37:")
print(ca_north[["City", "State", "LatD"]])

# ===== FIND AND REPLACE EXAMPLE =====
# Replace values in a column
print("\n===== FIND AND REPLACE EXAMPLE =====")
df1_copy = df1.copy()
df1_copy["NS"] = df1_copy["NS"].replace("N", "North")
df1_copy["EW"] = df1_copy["EW"].replace("W", "West")
print("After replacing N->North and W->West:")
print(df1_copy[["City", "NS", "EW"]].head())

# ===== GROUPBY EXAMPLE =====
# Group data by a column and aggregate
print("\n===== GROUPBY EXAMPLE =====")

# Count cities per state
cities_per_state = df1.groupby("State").size().reset_index(name="City_Count")
print("Number of cities per state:")
print(cities_per_state.sort_values("City_Count", ascending=False).head(10))

# Average latitude by state
avg_lat = df1.groupby("State")["LatD"].mean().reset_index()
avg_lat.columns = ["State", "Avg_Latitude"]
print("\nAverage latitude by state:")
print(avg_lat.sort_values("Avg_Latitude", ascending=False).head(10))

# Multiple aggregations
state_stats = df1.groupby("State")["LatD"].agg(["count", "mean", "min", "max"]).reset_index()
print("\nMultiple statistics by state:")
print(state_stats.head(10))

# ===== SORT EXAMPLE =====
# Sort data by one or more columns
print("\n===== SORT EXAMPLE =====")

# Sort by single column (ascending)
sorted_asc = df1.sort_values("City")
print("Cities sorted alphabetically:")
print(sorted_asc[["City", "State"]].head())

# Sort by single column (descending)
sorted_desc = df1.sort_values("LatD", ascending=False)
print("\nCities sorted by latitude (highest first):")
print(sorted_desc[["City", "State", "LatD"]].head())

# Sort by multiple columns
sorted_multi = df1.sort_values(["State", "City"])
print("\nCities sorted by State, then City:")
print(sorted_multi[["City", "State"]].head(10))