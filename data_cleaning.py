"""
Data Cleaning Script for Sales Dataset
This script loads raw sales data, performs data cleaning operations including
standardizing column names, handling missing values, and removing invalid entries,
then exports the cleaned data for analysis.
"""

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load raw sales data from CSV file.
    
    Args:
        file_path: Path to the raw CSV file
        
    Returns:
        DataFrame containing the raw sales data
    """
    # Copilot-assisted: Basic file loading with error handling
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {len(df)} rows from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        raise
    except Exception as e:
        print(f"Error loading data: {e}")
        raise


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names to lowercase with underscores.
    This ensures consistency and makes columns easier to reference in code.
    
    Args:
        df: DataFrame with potentially messy column names
        
    Returns:
        DataFrame with standardized column names
    """
    # Copilot-assisted: Column name standardization
    # Modified to be more explicit about the transformation steps
    df = df.copy()
    df.columns = df.columns.str.strip()  # Remove leading/trailing whitespace
    df.columns = df.columns.str.lower()  # Convert to lowercase
    df.columns = df.columns.str.replace(' ', '_')  # Replace spaces with underscores
    df.columns = df.columns.str.replace('[^a-z0-9_]', '', regex=True)  # Remove special chars
    print(f"Cleaned column names: {list(df.columns)}")
    return df


def strip_text_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove leading and trailing whitespace from text columns.
    Whitespace in product names and categories causes issues with grouping and filtering.
    
    Args:
        df: DataFrame with potential whitespace in text fields
        
    Returns:
        DataFrame with cleaned text fields
    """
    df = df.copy()
    # Strip whitespace from common text columns (adjust based on actual column names)
    text_columns = df.select_dtypes(include=['object']).columns
    for col in text_columns:
        df[col] = df[col].str.strip() if df[col].dtype == 'object' else df[col]
    print(f"Stripped whitespace from {len(text_columns)} text columns")
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values in critical columns.
    Drop rows with missing prices or quantities since these are essential for sales analysis.
    
    Args:
        df: DataFrame potentially containing missing values
        
    Returns:
        DataFrame with missing values handled
    """
    df = df.copy()
    initial_rows = len(df)
    
    # Identify numeric columns that likely represent price and quantity
    # Adjust these column names based on your actual data
    critical_columns = [col for col in df.columns if 'price' in col or 'quantity' in col or 'qty' in col]
    
    if critical_columns:
        df = df.dropna(subset=critical_columns)
        rows_removed = initial_rows - len(df)
        print(f"Removed {rows_removed} rows with missing critical values in {critical_columns}")
    else:
        print("Warning: No critical columns identified. Check column names.")
    
    return df


def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows with invalid data entries.
    Negative prices and quantities represent data entry errors and should be excluded.
    
    Args:
        df: DataFrame potentially containing invalid entries
        
    Returns:
        DataFrame with invalid rows removed
    """
    df = df.copy()
    initial_rows = len(df)
    
    # Remove rows with negative quantities
    quantity_cols = [col for col in df.columns if 'quantity' in col or 'qty' in col]
    for col in quantity_cols:
        if pd.api.types.is_numeric_dtype(df[col]):
            df = df[df[col] >= 0]
    
    # Remove rows with negative prices
    price_cols = [col for col in df.columns if 'price' in col]
    for col in price_cols:
        if pd.api.types.is_numeric_dtype(df[col]):
            df = df[df[col] >= 0]
    
    rows_removed = initial_rows - len(df)
    print(f"Removed {rows_removed} rows with invalid values (negative prices or quantities)")
    
    return df


if __name__ == "__main__":
    # Define file paths
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"
    
    # Execute data cleaning pipeline
    print("\n=== Starting Data Cleaning Pipeline ===\n")
    
    df_raw = load_data(raw_path)
    print(f"\nRaw data shape: {df_raw.shape}")
    
    df_clean = clean_column_names(df_raw)
    df_clean = strip_text_whitespace(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    
    # Export cleaned data
    df_clean.to_csv(cleaned_path, index=False)
    print(f"\nCleaned data shape: {df_clean.shape}")
    print(f"Saved cleaned data to {cleaned_path}")
    
    print("\n=== Cleaning Complete ===")
    print("\nFirst few rows of cleaned data:")
    print(df_clean.head())
    
    print("\nData types:")
    print(df_clean.dtypes)
