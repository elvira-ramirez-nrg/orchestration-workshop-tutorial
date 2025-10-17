import pandas as pd

# Load datasets
population_df = pd.read_csv("/workspaces/orchestration-workshop-tutorial/data/population-with-un-projections.csv")
energy_df = pd.read_csv("/workspaces/orchestration-workshop-tutorial/data/primary-energy-cons.csv")
renewable_df = pd.read_csv("/workspaces/orchestration-workshop-tutorial/data/renewable-share-energy.csv")
taxonomy_df = pd.read_csv("/workspaces/orchestration-workshop-tutorial/data/regional-grouping.csv")

# Rename columns for consistency
population_df = population_df.rename(
    columns={
        "population__sex_all__age_all__variant_estimates": "population",
        "Entity": "entity",
        "Code": "entity_code",
        "Year": "year",
    }
).dropna(subset=["population"])

# Select only the standardized columns
population_df = population_df[["entity", "entity_code", "year", "population"]]

print(population_df.head())
print(population_df.info())
print(population_df.describe())


# Assign types
population_df = population_df.astype({"year": int, "population": int, "entity_code": str, "entity": str})
