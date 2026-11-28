from pathlib import Path
import pandas as pd

# Find the data folder relative to this script, not the launch directory.
data_folder = Path(__file__).resolve().parent
print("SCRIPT DIRECTORY", data_folder)
file_path = data_folder / 'raw' / 'cars_dataset.csv'
print("FILE PATH", file_path)
output_path = data_folder / 'processed' / 'cars_dataset_cleaned.csv'
print("OUTPUT PATH", output_path)


# Read the original workbook. It is never used as an output file.
df = pd.read_csv(file_path)
before = {
    'Rows': len(df),
    'Columns': len(df.columns),
    'Missing values': int(df.isna().sum().sum()),
    'Duplicate rows': int(df.duplicated().sum())
}
missing_before = df.isna().sum()

# Trim extra spaces without turning missing text into the word "nan".
# Treat empty or whitespace-only text as missing. Keep original spelling
# and capitalization: changing names such as BMW or CX-5 could be misleading.
string_cols = ['vehicle_id', 'make', 'model', 'model_variant', 'body_type']
for col in string_cols:
    if col in df.columns:
        df[col] = df[col].astype('string').str.strip()
        df[col] = df[col].replace('', pd.NA)

# Remove only exact repeated rows after trimming text. Keep all columns.
# A repeated vehicle ID alone is not enough reason to delete a record.
duplicates_removed = int(df.duplicated().sum())
df = df.drop_duplicates()

# Leave unknown values missing. A missing variant does not mean "Standard".
# Median-filled prices could reduce variation and distort brand comparisons.
# Reliability estimates could also change relationships in later analysis.
# The team should agree on any imputation before adding it here.

# Flag possible problems for review; do not replace prices or remove outliers.
print('\nPrice values needing review:')
for col in ['original_price', 'msrp']:
    print(f'{col}: {df[col].isna().sum()} missing, '
          f'{(df[col] == 0).sum()} zero, {(df[col] < 0).sum()} negative')
print(f'Repeated vehicle IDs after cleaning: {df["vehicle_id"].duplicated().sum()}')

# Save a separate cleaned workbook. Future runs replace only this output.
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

# Show what changed, including missing values in each column.
after = {
    'Rows': len(df),
    'Columns': len(df.columns),
    'Missing values': int(df.isna().sum().sum()),
    'Duplicate rows': int(df.duplicated().sum())
}
print('\nBefore-and-after summary:')
print(pd.DataFrame({'Before': before, 'After': after}))
print(f'\nExact duplicate rows removed: {duplicates_removed}')
print('\nMissing values by column:')
print(pd.DataFrame({'Before': missing_before, 'After': df.isna().sum()}))
print(f'\nData cleaning complete. Saved to: {output_path}')
