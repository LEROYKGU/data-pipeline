""" 
Ce module est dédié au stockage des données. Il contient les fonctions pour sauvegarder les données traitées dans différents formats (CSV, Excel, SQL, etc.) et les préparer pour une utilisation future.
"""

# ─────────────────────────────────────────────
# Importations des bibliothèques
# ─────────────────────────────────────────────
import pandas as pd
import numpy as np
import os

# ─────────────────────────────────────────────
# Fonction de sauvegarde des données dans un fichier CSV
# ─────────────────────────────────────────────
def save_data_csv(df, file_path):
    """
    Sauvegarde les données dans un fichier CSV.
    """
    try:
        df.to_csv(file_path, index=False)
        print(f"Data saved successfully to {file_path}")
    except Exception as e:
        print(f"Error saving data to {file_path}: {e}")

# ─────────────────────────────────────────────
# Fonction de sauvegarde des données dans un fichier Excel
# ─────────────────────────────────────────────
def save_data_excel(df, file_path, sheet_name='Sheet1'):
    """
    Sauvegarde les données dans un fichier Excel.
    """
    try:
        df.to_excel(file_path, sheet_name=sheet_name, index=False)
        print(f"Data saved successfully to {file_path} (sheet: {sheet_name})")
    except Exception as e:
        print(f"Error saving data to {file_path}: {e}")

# ─────────────────────────────────────────────
# Fonction de sauvegarde des données dans une base de données SQL
# ─────────────────────────────────────────────
def save_data_sql(df, connection_string, table_name):
    """
    Sauvegarde les données dans une base de données SQL.
    """
    try:
        from sqlalchemy import create_engine
        engine = create_engine(connection_string)
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Data saved successfully to SQL database (table: {table_name})")
    except Exception as e:
        print(f"Error saving data to SQL database: {e}")

# ─────────────────────────────────────────────
# Fonction de sauvegarde des données dans un format JSON
# ─────────────────────────────────────────────
def save_data_json(df, file_path):
    """
    Sauvegarde les données dans un fichier JSON.
    """
    try:
        df.to_json(file_path, orient='records', lines=True)
        print(f"Data saved successfully to {file_path}")
    except Exception as e:
        print(f"Error saving data to {file_path}: {e}")

# ─────────────────────────────────────────────
# Fonction de préparation des données pour une utilisation future
# ─────────────────────────────────────────────
def prepare_data_for_future_use(df, file_path):
    """
    Prépare les données pour une utilisation future en les sauvegardant dans un format compressé.
    """
    try:
        df.to_csv(file_path, index=False, compression='gzip')
        print(f"Data prepared and saved successfully to {file_path} (compressed)")
    except Exception as e:
        print(f"Error preparing data for future use: {e}")

# ─────────────────────────────────────────────
# Fonction de séparation et d'enregistrement des données en ensembles d'entraînement ,de test et de validation.
# ─────────────────────────────────────────────
def split_data(df, train_path, test_path, val_path, test_size=0.2, val_size=0.1, random_state=42):
    """
    Sépare les données en ensembles d'entraînement, de test et de validation, puis les sauvegarde dans des fichiers CSV.
    """
    from sklearn.model_selection import train_test_split
    
    # Séparation des données en ensembles d'entraînement et de test
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)
    
    # Séparation de l'ensemble de test en ensemble de validation
    val_df, test_df = train_test_split(test_df, test_size=val_size/(test_size + val_size), random_state=random_state)
    
    # Sauvegarde des ensembles d'entraînement, de test et de validation
    save_data_csv(train_df, train_path)
    save_data_csv(test_df, test_path)
    save_data_csv(val_df, val_path)

    return train_df, test_df, val_df
