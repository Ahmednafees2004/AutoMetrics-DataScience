# AutoMetrics

Final group project for **CSC 3780 — Fundamentals of Data Science**, developed by a team of four.

## Project overview

**Research question: Why are some car brands more expensive than others?**

We plan to use a Kaggle automotive dataset to explore how vehicle brand, type, performance, safety, and other available characteristics relate to vehicle prices. The dataset has not yet been selected or added. Specific comparisons will depend on the fields actually available; observational associations alone will not establish causation.

## Research questions

- How do vehicle price distributions differ across brands?
- If available, how do vehicle type, performance, and safety characteristics relate to price?
- Which available characteristics might help explain price differences between brands?
- How might missing values, duplicates, outliers, or uneven brand representation affect our comparisons?

## Planned deliverables

- Exploratory data analysis (EDA), data cleaning, and visualizations.
- A reproducible Jupyter Notebook documenting the workflow.
- A final PDF report and a group presentation.
- Machine learning is optional and is not part of the initial setup.

## Directory structure

```text
AutoMetrics-DataScience/
├── data/
│   ├── raw/              # Original local dataset downloads; preserve unchanged
│   └── processed/        # Future cleaned or derived datasets
├── notebooks/
│   └── 01_dataset_exploration.ipynb
├── figures/              # Exported plots for the report and presentation
├── report/               # Report source files and final PDF
├── presentation/         # Slides and presentation materials
├── README.md
├── requirements.txt
└── .gitignore
```

Empty output folders contain `.gitkeep` placeholders so they can be tracked by Git. Local dataset files under `data/` are ignored.

## Local setup

From the project root:

```bash
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
jupyter notebook
```

Open `notebooks/01_dataset_exploration.ipynb`. It currently contains Markdown headings only; no data loading, cleaning, analysis, or models have been implemented.

## Collaboration and reproducibility

- Before analysis, record the selected dataset's Kaggle URL, author, version or download date, license, and exact filenames here so all four teammates can obtain the same input.
- Keep original downloads in `data/raw/` unchanged. Save future derived data in `data/processed/`.
- Use relative paths in notebooks (for example, `../data/raw/` when running from `notebooks/`) rather than machine-specific absolute paths.
- Coordinate ownership of notebooks and deliverables to reduce edit conflicts. Use descriptive branches and review changes together.
- Document cleaning decisions and assumptions in the notebook. Before delivery, restart the kernel and run all cells in order to verify reproducibility.
- Keep shared dependencies in `requirements.txt`. Versions are initially unpinned; record tested versions when the team establishes its analysis environment.

This repository currently provides project structure only. No dataset columns or results are assumed.
