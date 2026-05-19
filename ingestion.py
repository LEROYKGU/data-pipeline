""" 
Ce module est dédié à l'ingestion de données. Il contient les fonctions pour charger les données à partir de différentes sources (CSV, Excel, SQL, etc.) et les préparer pour l'exploration et l'analyse.
"""

# ─────────────────────────────────────────────
# Importations des bibliothèques    
# ─────────────────────────────────────────────
import pandas as pd
import numpy as np
import requests
import sqlalchemy
import os

# ─────────────────────────────────────────────
# Fonction de chargement des données à partir d'un fichier CSV
# ─────────────────────────────────────────────
def load_data_csv(file_path):
    """
    Charge les données à partir d'un fichier CSV et retourne un DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return df
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None

# ─────────────────────────────────────────────
# Fonction de chargement des données à partir d'un fichier Excel
# ─────────────────────────────────────────────
def load_data_excel(file_path, sheet_name=0):
    """
    Charge les données à partir d'un fichier Excel et retourne un DataFrame.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"Data loaded successfully from {file_path} (sheet: {sheet_name})")
        return df
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None

# ─────────────────────────────────────────────
# Fonction de chargement des données à partir d'une base de données SQL 
# ─────────────────────────────────────────────
def load_data_sql(connection_string, query):
    """
    Charge les données à partir d'une base de données SQL et retourne un DataFrame.
    """
    try:
        df = pd.read_sql(query, connection_string)
        print(f"Data loaded successfully from SQL database")
        return df
    except Exception as e:
        print(f"Error loading data from SQL database: {e}")
        return None

# ─────────────────────────────────────────────
# Fonction de chargement des données à partir d'une API
# ─────────────────────────────────────────────
def load_data_api(api_url, params=None):
    """
    Charge les données à partir d'une API et retourne un DataFrame.
    """
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        df = pd.DataFrame(data)
        print(f"Data loaded successfully from API: {api_url}")
        return df
    except Exception as e:
        print(f"Error loading data from API: {e}")
        return None

# ─────────────────────────────────────────────
# Fonction de préparation des données (nettoyage)       
# ─────────────────────────────────────────────
def prepare_data(df):   
    """
    Prépare les données pour l'exploration et l'analyse, en effectuant des opérations de nettoyage et de transformation.
    """
    # Convert column names to lowercase
    df.columns = df.columns.str.lower()
    
    # Handle missing values (e.g., fill with median)
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col].fillna(df[col].median(), inplace=True)

    # Handle missing values for categorical columns (e.g., fill with mode)
    for col in df.select_dtypes(include=['object']).columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

    # Handle duplicates
    df.drop_duplicates(inplace=True)

    # Convert data types if necessary (e.g., convert date columns to datetime)
    for col in df.columns:
        if 'date' in col:
            df[col] = pd.to_datetime(df[col], errors='coerce')  

    # Handles outliers (using IQR method)
   columns = df.select_dtypes(include=[np.number]).columns
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
        df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])

    print("Data preparation completed.")
    return df
