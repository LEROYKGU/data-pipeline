"""
Ce module fait partie de la pipeline data. Elle contient les fonctions d'exploration de données.
"""

# ─────────────────────────────────────────────
# Importations des bibliothèques
# ─────────────────────────────────────────────
import pandas as pd
import numpy as np

# ─────────────────────────────────────────────
# Fonction de statistiques de données
# ─────────────────────────────────────────────
def data_stats(df):
    """
    Affiche les informations de base sur le dataset, y compris la forme, les types de données et les statistiques descriptives.
    """
    # Basic shape
    print(f"\n▸ Shape: {df.shape[0]} rows × {df.shape[1]} columns")

    # Column names
    print("\n▸ Columns:")
    print(df.columns.tolist())

    # Data types
    print("\n▸ Data types:")
    print(df.dtypes)

    # First 5 rows
    print("\n▸ First 5 rows:")
    print(df.head())

    # Summary statistics (numeric columns)
    print("\n▸ Summary statistics (numeric columns):")
    print(df.describe())


    return "Exploration done!"


# ─────────────────────────────────────────────
# Fonction de vérification des valeurs manquantes
# ─────────────────────────────────────────────
def check_missing_values(df):
    """
    Affiche les valeurs manquantes par colonne.
    """

    # Missing values
    print("\n▸ Missing values per column (top 20):")
    missing = df.isnull().sum().sort_values(ascending=False)
    print(missing[missing > 0].head(20))

    # Missing percentage
    print("\n▸ Missing value percentage (columns > 5% missing):")
    missing_pct = (df.isnull().sum() / len(df) * 100).sort_values(ascending=False)
    print(missing_pct[missing_pct > 5].head(20).round(2))

    return "Exploration done!"

# ─────────────────────────────────────────────
# Fonction de vérifications de duplaications
# ─────────────────────────────────────────────
def check_duplicates(df):
    """
    Vérifie les doublons dans le dataset.
    """
    duplicates = df.duplicated().sum()
    print(f"\n▸ Number of duplicate rows: {duplicates}")

    return "Duplication check done!"

# ─────────────────────────────────────────────
# Fonction d'exploration des valeurs uniques
# ────────────────────────────────────────────
def unique_values(df, key_cols):
    """
    Affiche le nombre de valeurs uniques pour les colonnes clés.
    """
    print("\n▸ Unique value counts for key categorical columns:")
    for col in key_cols:
        if col in df.columns:
            print(f"  {col}: {df[col].nunique()} unique values")

    return "Unique values exploration done!"

# ─────────────────────────────────────────────
# Fonction d'exploration de la distribution des données
# ─────────────────────────────────────────────
def distribution(df, column):
    """
    Affiche la distribution d'une colonne spécifique.
    """
    print(f"\n▸ Distribution of {column}:")
    print(df[column].value_counts(dropna=False))

    return "Distribution exploration done!"

# ─────────────────────────────────────────────
# Fonction d'exploration des outliers
# ─────────────────────────────────────────────
def check_outliers(df):
    """
    Affiche les statistiques descriptives pour identifier les outliers.
    """
    print("\n▸ Outliers detection (using IQR method):")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        print(f" {col}: Q1={Q1}, Q3={Q3}, IQR={IQR}, lower_bound={lower_bound}, upper_bound={upper_bound}")
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        print(f"  {col}: {len(outliers)} outliers")
        print(f"  {col}: {len(outliers)/len(df)*100:.2f}% d'outliers")

    return "Outliers check done!"
    