import pandas as pd

#Load the dataset
file_path = "cars_dataset_edited.csv.xlsx"
df = pd.read_excel(file_path)

#Clean string columns FIRST (strip whitespace so groupings work properly)
string_cols = ['vehicle_id', 'make', 'model', 'model_variant', 'body_type']
for col in string_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()


print(f"Duplicates Found: {df.duplicated().sum()}")

df = df.drop_duplicates()

#Fill missing model variants
df['model_variant'] = df['model_variant'].fillna('Standard')

#Impute prices using grouped medians by make and model
df['original_price'] = df['original_price'].fillna(
    df.groupby(['make', 'model'])['original_price'].transform('median')
)
df['original_price'] = df['original_price'].fillna(df['original_price'].median())

df['msrp'] = df['msrp'].fillna(
    df.groupby(['make', 'model'])['msrp'].transform('median')
)
df['msrp'] = df['msrp'].fillna(df['msrp'].median())

#Impute reliability score using grouped median by make
df['reliability_score'] = df['reliability_score'].fillna(
    df.groupby('make')['reliability_score'].transform('median')
)
df['reliability_score'] = df['reliability_score'].fillna(df['reliability_score'].median())


#Save the cleaned dataset
df.to_excel('cars_dataset_cleaned.xlsx', index=False)
print("Data cleaning complete. Cleaned file saved as 'cars_dataset_cleaned.xlsx'.")


