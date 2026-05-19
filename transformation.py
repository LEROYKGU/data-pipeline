"""
Ce module est dédié à la transformation des données. Il contient les fonctions pour nettoyer, transformer et préparer les données pour l'analyse et la modélisation.
"""

# ─────────────────────────────────────────────
# Importations des bibliothèques
# ─────────────────────────────────────────────
import pandas as pd
import numpy as np

# ─────────────────────────────────────────────
# Fonction de discretisation d'une variable continue
# ───────────────────────────────────────────── 
def discretize_variable(df, column, bins, labels):
    """
    Discretise une variable continue en catégories.
    """
    df[column + '_binned'] = pd.cut(df[column], bins=bins, labels=labels)
    return df

# ─────────────────────────────────────────────
# Fonction de normalisation d'une variable numérique avec Min-Max
# ───────────────────────────────────────────── 
def min_max_normalize(df, column):
    """
    Normalise une variable numérique en utilisant la méthode Min-Max.
    """
    scaler = MinMaxScaler()
    df[column + '_normalized'] = scaler.fit_transform(df[[column]])
    return df

# ─────────────────────────────────────────────
# Fonction de standardisation d'une variable numérique avec Z-score
# ─────────────────────────────────────────────
def z_score_standardize(df, column):
    """
    Standardise une variable numérique en utilisant la méthode Z-score.
    """
    scaler = StandardScaler()
    df[column + '_standardized'] = scaler.fit_transform(df[[column]])
    return df

# ─────────────────────────────────────────────
# Fonction de transformation logarithmique d'une variable numérique
# ─────────────────────────────────────────────
def log_transform(df, column):
    """
    Applique une transformation logarithmique à une variable numérique.
    """
    df[column + '_log'] = np.log(df[column] + 1)  # Ajout de 1 pour éviter log(0)
    return df

# ─────────────────────────────────────────────
# Fonction de transformation Box-Cox d'une variable numérique
# ─────────────────────────────────────────────
def boxcox_transform(df, column):
    """
    Applique une transformation Box-Cox à une variable numérique.
    """
    df[column + '_boxcox'], _ = boxcox(df[column] + 1)  # Ajout de 1 pour éviter les valeurs négatives
    return df

# ─────────────────────────────────────────────
# Fonction d'encoding d'une variable catégorielle avec One-Hot Encoding
# ─────────────────────────────────────────────
def one_hot_encode(df, column):
    """
    Applique un encodage One-Hot à une variable catégorielle.
    """
    dummies = pd.get_dummies(df[column], prefix=column)
    df = pd.concat([df, dummies], axis=1)
    return df

# ─────────────────────────────────────────────
# Fonction d'encoding d'une variable catégorielle avec Label Encoding
# ─────────────────────────────────────────────
def label_encode(df, column):
    """
    Applique un encodage Label à une variable catégorielle.
    """
    le = LabelEncoder()
    df[column + '_label'] = le.fit_transform(df[column])
    return df

# ─────────────────────────────────────────────
# Fonction de catégorisation d'une variable catégorielle en fonction de seuils
# ─────────────────────────────────────────────
def categorize_variable(df, column, thresholds, labels):
    """
    Catégorise une variable catégorielle en fonction de seuils définis.
    """
    df[column + '_categorized'] = pd.cut(df[column], bins=thresholds, labels=labels)
    return df
