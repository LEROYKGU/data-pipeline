"""
Ce module est dédié à au choix des features et à l'ingénierie de celles-ci. Il contient les fonctions pour sélectionner les features les plus pertinentes, créer de nouvelles features à partir des données existantes, et préparer les données pour la modélisation.
"""

# ─────────────────────────────────────────────
# Importations des bibliothèques
# ─────────────────────────────────────────────
import pandas as pd
import numpy as np

# ─────────────────────────────────────────────
# Fonction de corrélation des features
# ─────────────────────────────────────────────
def feature_correlation(df, target_col):
    """
    Affiche la corrélation entre les features numériques et la variable cible.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    correlations = df[numeric_cols].corr()[target_col].sort_values(ascending=False)
    print(f"\n▸ Correlation with target variable '{target_col}':")
    print(correlations)

    return "Correlation analysis done!"

# ─────────────────────────────────────────────
# Fonction d'analyse de l'importance des features    
# ─────────────────────────────────────────────
def feature_importance(model, feature_names):
    """
    Affiche l'importance des features à partir d'un modèle entraîné.
    """
    importance = model.feature_importances_
    feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importance})
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
    
    print("\n▸ Feature importance:")
    print(feature_importance_df)

    return "Feature importance analysis done!"

# ─────────────────────────────────────────────
# Fonction d'analyse de la multicolinéarité
# ─────────────────────────────────────────────
def check_multicollinearity(df, threshold=0.8):
    """
    Affiche les paires de features qui ont une corrélation supérieure au seuil spécifié.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr().abs()
    
    print(f"\n▸ Pairs of features with correlation above {threshold}:")
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if corr_matrix.iloc[i, j] > threshold:
                print(f"  {corr_matrix.columns[i]} and {corr_matrix.columns[j]}: {corr_matrix.iloc[i, j]:.2f}")

    return "Multicollinearity check done!"

# ─────────────────────────────────────────────
# Fonction d'analyse des interactions entre les features
# ─────────────────────────────────────────────
def check_feature_interactions(df, target_col):
    """
    Affiche les interactions potentielles entre les features et la variable cible.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        interaction = df[col] * df[target_col]
        correlation = interaction.corr(df[target_col])
        print(f"  Interaction between {col} and {target_col}: Correlation = {correlation:.2f}")

    return "Feature interactions analysis done!"

# ─────────────────────────────────────────────
# Fonction d'analyse en composantes principales (PCA)
# ─────────────────────────────────────────────
def perform_pca(df, n_components=2):
    """
    Effectue une analyse en composantes principales (PCA) sur les features numériques.
    """
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[numeric_cols])
    
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(scaled_data)
    
    print(f"\n▸ PCA explained variance ratio: {pca.explained_variance_ratio_}")
    
    return pca_result


# ─────────────────────────────────────────────
# Fonction de création de nouvelles features à partir des interactions
# ─────────────────────────────────────────────
def create_interaction_features(df, feature_pairs):
    """
    Crée de nouvelles features à partir des interactions entre les paires de features spécifiées.
    """
    for feature1, feature2 in feature_pairs:
        new_feature_name = f"{feature1}_x_{feature2}"
        df[new_feature_name] = df[feature1] * df[feature2]
        print(f"  Created interaction feature: {new_feature_name}")

    return df

# ─────────────────────────────────────────────
# Fonction de sélection des features basée sur l'importance
# ─────────────────────────────────────────────
def select_features_by_importance(model, feature_names, threshold=0.01):
    """
    Sélectionne les features dont l'importance est supérieure au seuil spécifié.
    """
    importance = model.feature_importances_
    selected_features = [feature for feature, imp in zip(feature_names, importance) if imp > threshold]
    
    print(f"\n▸ Selected features based on importance (threshold={threshold}):")
    print(selected_features)

    return selected_features

# ─────────────────────────────────────────────
# Fonction de choix des features basée sur la corrélation
# ─────────────────────────────────────────────
def select_features_by_correlation(df, target_col, threshold=0.1):
    """
    Sélectionne les features dont la corrélation avec la variable cible est supérieure au seuil spécifié.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    selected_features = [col for col in numeric_cols if abs(df[col].corr(df[target_col])) > threshold]
    
    print(f"\n▸ Selected features based on correlation with target (threshold={threshold}):")
    print(selected_features)

    return selected_features

# ─────────────────────────────────────────────
# Fonction de choix des features basée sur la multicolinéarité  
# ─────────────────────────────────────────────
def select_features_by_multicollinearity(df, threshold=0.8):
    """
    Sélectionne les features en éliminant celles qui ont une corrélation supérieure au seuil spécifié.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr().abs()
    upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    
    to_drop = [column for column in upper_triangle.columns if any(upper_triangle[column] > threshold)]
    
    print(f"\n▸ Selected features after removing multicollinearity (threshold={threshold}):")
    selected_features = [col for col in numeric_cols if col not in to_drop]
    print(selected_features)

    return selected_features

# ─────────────────────────────────────────────
# Fonction de features synthesis 
# ─────────────────────────────────────────────
def feature_synthesis(df, feature_groups):
    """
    Crée de nouvelles features en combinant les features existantes selon les groupes spécifiés.
    """
    for group_name, features in feature_groups.items():
        df[group_name] = df[features].sum(axis=1)
        print(f"  Created synthesized feature: {group_name} from {features}")

    return df
