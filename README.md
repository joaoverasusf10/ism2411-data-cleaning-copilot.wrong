Sales Data Cleaning Project
Overview
This project demonstrates data cleaning techniques on a messy sales dataset using Python and pandas. The script standardizes column names, handles missing values, removes invalid entries, and produces a clean dataset ready for analysis.

Project Structure:
ism2411-data-cleaning-copilot/
├── data/
│   ├── raw/
│   │   └── sales_data_raw.csv       # Original messy data
│   └── processed/
│       └── sales_data_clean.csv     # Cleaned output
├── src/
│   └── data_cleaning.py             # Main cleaning script
├── README.md                        # This file
└── reflection.md                    # Assignment reflection
Features

Column Name Standardization: Converts all column names to lowercase with underscores
Whitespace Removal: Strips leading/trailing whitespace from text fields
Missing Value Handling: Removes rows with missing prices or quantities
Invalid Data Removal: Filters out negative prices and quantities

Requirements

Python 3.7+
pandas

Install dependencies:
bashpip install pandas
Usage

Place your raw data file in data/raw/sales_data_raw.csv
Run the cleaning script from the project root:

bashpython src/data_cleaning.py

Find the cleaned data in data/processed/sales_data_clean.csv

Data Cleaning Process

Load raw CSV data
Standardize all column names (lowercase, underscores)
Strip whitespace from text columns
Remove rows with missing critical values (price, quantity)
Remove rows with invalid values (negative numbers)
Export cleaned data

Development Notes
This project was developed with the assistance of GitHub Copilot to demonstrate effective use of AI coding tools. See reflection.md for details on the development process.
Author
Created as part of ISM 2411 coursework on data cleaning and AI-assisted development.
