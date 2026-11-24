# AutoMetrics

CSC 3780 — Fundamentals of Data Science group project.

**Research question: Why are some car brands more expensive than others?**

We explore how brand, body type, performance, listed safety features, and vehicle age relate to prices in an edited Kaggle automotive dataset. The current cleaned workbook contains 100,000 rows and 26 columns. These analyses describe associations, not causal explanations. Original price is the primary price measure; MSRP provides a secondary comparison.

## Project structure

```text
AutoMetrics-DataScience/
├── data/
│   ├── raw/cars_dataset_edited.csv.xlsx       # Local input; ignored by Git
│   ├── processed/cars_dataset_cleaned.xlsx    # Shared local analysis input; ignored
│   └── Data_Cleaning_Script.py
├── notebooks/
│   ├── 01_dataset_exploration.ipynb
│   ├── 02_brand_price_comparison.ipynb
│   └── 03_price_measure_comparison.ipynb
├── figures/                                 # Reserved for final figure exports
├── report/                                  # Reserved for report source and final PDF
├── presentation/                            # Reserved for slides
├── README.md
├── requirements.txt
└── .gitignore
```

Historical backups, validation copies, and older supporting exports are kept outside the repository. They are not required to run the notebooks. Empty local directories may not appear in a fresh clone; tracked `.gitkeep` files preserve the main output folders.

## Notebooks

| Notebook | Purpose |
| --- | --- |
| `01_dataset_exploration.ipynb` | Dataset preview, dimensions, types, missing values, duplicates, descriptive statistics, brand/body-type counts, and original-price relationships with vehicle characteristics. |
| `02_brand_price_comparison.ipynb` | Original-price comparisons by brand and within SUVs/sedans, performance/safety correlations, and median MSRP by brand. Includes Dachi's corrected missing-value explanations and statistics. |
| `03_price_measure_comparison.ipynb` | Price availability, paired original-price/MSRP differences, comparison of correlations, and MSRP plots by body type, performance, and vehicle age. |

All three notebooks read the same cleaned workbook and contain saved outputs. Plots are generated from data rather than loaded from exported PNGs. The luxury grouping in Notebook 02 is manually defined (Mercedes-Benz, BMW, Audi, Lexus), not a dataset classification. The original MSRP visualization contribution is represented across Notebooks 02 and 03.

## Data and cleaning

Obtain the team's agreed input workbook and place it at `data/raw/cars_dataset_edited.csv.xlsx`. Dataset files are not distributed through GitHub. A fresh clone therefore requires local data before execution.

`data/Data_Cleaning_Script.py`:

- Loads the first worksheet using paths relative to the script.
- Trims surrounding whitespace in text columns and treats blank text as missing.
- Removes exact duplicate rows after text normalization and retains all columns.
- Preserves missing prices, reliability scores, and model variants; it does not impute values.
- Reports missing, zero, and negative prices and repeated vehicle IDs without automatically removing unusual prices.
- Saves a separate cleaned workbook and prints before/after counts.

The raw workbook is never overwritten. **Running the cleaning script replaces the processed workbook**, so use it only when intentionally regenerating the agreed cleaned input. To review existing analysis, use the existing shared cleaned workbook without rerunning cleaning.

The current cleaned dataset has 1,000 missing original prices and 2,000 missing MSRP values. Original-price summaries use 99,000 available values; MSRP summaries use 98,000; paired-price comparisons use 97,022 complete pairs. Notebook-specific temporary selections do not modify the workbook. No predictive models are implemented; machine learning is optional for this project.

## Environment and dependencies

Python 3.12 was used for verification. From the project root:

```bash
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

`requirements.txt` includes pandas, NumPy, Matplotlib, Seaborn, scikit-learn, Jupyter, and openpyxl. Openpyxl reads the Excel workbook; scikit-learn is listed but is not used by the current EDA. Dependencies are currently unpinned.

## Run the analysis

With the virtual environment active and the shared cleaned workbook available:

```bash
jupyter notebook
```

Open the three notebooks under `notebooks/` in numerical order. Select the project's virtual environment as the kernel, restart the kernel, and run all cells. Each notebook loads its own data and can run independently. Paths support starting from either the project root or the notebooks directory. Preserve any unsaved editor changes separately before replacing or reloading notebook files.

Alternatively, from the project root:

```bash
python -m jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=180 notebooks/01_dataset_exploration.ipynb notebooks/02_brand_price_comparison.ipynb notebooks/03_price_measure_comparison.ipynb
```

This command refreshes saved notebook outputs; it does not write datasets. The latest complete verification passed 21, 8, and 13 code cells respectively, producing 6, 4, and 7 plots. The subsequent Section 8 correlation-chart formatting update in Notebook 03 was executed and visually checked separately.

To intentionally regenerate the cleaned workbook from the agreed raw input:

```bash
python data/Data_Cleaning_Script.py
```

## Interpretation and remaining deliverables

The notebooks document descriptive findings and limitations. Price measures are nearly perfectly correlated, and the brand premium index has an unverified definition; neither should be treated as an independent causal explanation. Safety-feature counts are not crash-test ratings. Age comparisons do not follow the same vehicles over time and cannot establish depreciation.

Before final submission, record the exact Kaggle source URL, author, dataset version/download date, license, and editing history. Currency, price definitions, and score construction still require source confirmation; plots therefore use dataset units. Do not invent these details. The final PDF report and group presentation remain to be prepared.

Keep datasets, virtual environments, notebook checkpoints, backups, and validation copies out of commits. Review explicit file selections before staging. Coordinate notebook changes with teammates and review the integration branch before merging into main.
