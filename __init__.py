"""
Ce module fait référence à l'ensemble des fonctions de la pipeline data. Il contient les fonctions d'ingestion, d'exploration, de visualisation et d'ingénierie des features.
"""

# ─────────────────────────────────────────────
# Importations des modules de la pipeline data  
# ─────────────────────────────────────────────
from .ingestion import *
from .exploratory import *
from .visualization import *
from .features_engineering import *
from .transformation import *
from .storing import *

# ─────────────────────────────────────────────
# Version du package
# ─────────────────────────────────────────────
__version__ = "0.1.0"

# ─────────────────────────────────────────────
# Message de bienvenue
# ─────────────────────────────────────────────
def welcome_message():
    print("Bienvenue dans le package de pipeline data !")
    print("Utilisez les fonctions d'ingestion, d'exploration, de visualisation et d'ingénierie des features pour analyser vos données.")

# ─────────────────────────────────────────────
# Appel du message de bienvenue lors de l'importation du package
# ───────────────────────────────────────────── 
welcome_message()

# ─────────────────────────────────────────────
# Fonction d'exécution de la pipeline complète
# ─────────────────────────────────────────────
def run_pipeline(file_path, target_col):
    """
    Exécute la pipeline complète de l'ingestion à l'analyse des features.
    """
    # Ingestion
    df = load_data_csv(file_path)
    
    # Exploration
    data_stats(df)
    check_missing_values(df)
    check_outliers(df)
    
    # Visualisation
    plot_distributions(df)
    plot_correlation_matrix(df)
    
    # Ingénierie des features
    feature_correlation(df, target_col)
    
    print("Pipeline complète exécutée avec succès !")
