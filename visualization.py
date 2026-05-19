"""
Ce module est dédié à la visualisation des données. Il contient les fonctions pour créer des graphiques et des visualisations afin de mieux comprendre les données, identifier les tendances, les distributions et les relations entre les variables.
"""

# ─────────────────────────────────────────────
# Importations des bibliothèques    
# ─────────────────────────────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ─────────────────────────────────────────────
# Fonction de visualisation de la distribution des variables numériques 
# ─────────────────────────────────────────────
def plot_numeric_distribution(df):
    """
    Affiche la distribution d'une variable numérique à l'aide d'un histogramme et d'un graphique de densité.
    """
    columns = df.select_dtypes(include=[np.number]).columns
    for column in columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], kde=True, bins=30, bounds=(df[column].min(), df[column].max()), color='skyblue')
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

# ─────────────────────────────────────────────
# Fonction de visualisation de la relation entre deux variables numériques
# ─────────────────────────────────────────────
def plot_numeric_relationship(df, column1, column2):
    """
    Affiche la relation entre deux variables numériques à l'aide d'un nuage de points et d'une ligne de tendance.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[column1], y=df[column2])
    sns.regplot(x=df[column1], y=df[column2], scatter=False, color='red')
    plt.title(f"Relationship between {column1} and {column2}")
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.show()

# ─────────────────────────────────────────────
# Fonction de visualisation de la relation entre une variable numérique et une variable catégorielle
# ─────────────────────────────────────────────
def plot_numeric_categorical_relationship(df, numeric_col, categorical_col):
    """
    Affiche la relation entre une variable numérique et une variable catégorielle à l'aide d'un boxplot.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[categorical_col], y=df[numeric_col])
    plt.title(f"Relationship between {numeric_col} and {categorical_col}")
    plt.xlabel(categorical_col)
    plt.ylabel(numeric_col)
    plt.show()

# ─────────────────────────────────────────────
# Fonction de visualisation de la relation entre deux variables catégorielles
# ─────────────────────────────────────────────
def plot_categorical_relationship(df, column1, column2):
    """
    Affiche la relation entre deux variables catégorielles à l'aide d'un graphique en barres empilées.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(x=df[column1], hue=df[column2])
    plt.title(f"Relationship between {column1} and {column2}")
    plt.xlabel(column1)
    plt.ylabel("Count")
    plt.legend(title=column2)
    plt.show()

# ─────────────────────────────────────────────
# Fonction de visualisation de la matrice de corrélation
# ─────────────────────────────────────────────
def plot_correlation_matrix(df):
    """
    Affiche la matrice de corrélation pour les variables numériques du dataset.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()

    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Correlation Matrix")
    plt.show()

# ─────────────────────────────────────────────
# Fonction de visualisation avec Pie Chart
# ─────────────────────────────────────────────
def plot_pie_chart(df, column):
    """
    Affiche la répartition d'une variable catégorielle à l'aide d'un graphique en secteurs (pie chart).
    """
    plt.figure(figsize=(8, 8))
    df[column].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
    plt.title(f"Distribution of {column}")
    plt.ylabel('')
    plt.show()

# ─────────────────────────────────────────────
# Fonction de visualisation avec Bar Chart
# ─────────────────────────────────────────────
def plot_bar_chart(df, column):
    """
    Affiche la répartition d'une variable catégorielle à l'aide d'un graphique en barres.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(x=df[column], palette='pastel')
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

# ─────────────────────────────────────────────
# Fonction de visualisation avec Box Plot
# ─────────────────────────────────────────────
def plot_box_plot(df, column):
    """
    Affiche la distribution d'une variable numérique à l'aide d'un box plot.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(y=df[column], color='lightblue')
    plt.title(f"Box Plot of {column}")
    plt.ylabel(column)
    plt.show()

# ─────────────────────────────────────────────
# Fonction de visualisation avec Violin Plot
# ─────────────────────────────────────────────
def plot_violin_plot(df, column):
    """
    Affiche la distribution d'une variable numérique à l'aide d'un violin plot.
    """
    plt.figure(figsize=(10, 6))
    sns.violinplot(y=df[column], color='lightgreen')
    plt.title(f"Violin Plot of {column}")
    plt.ylabel(column)
    plt.show()

# ─────────────────────────────────────────────
# Fonction de visualisation avec Pair Plot
# ─────────────────────────────────────────────
def plot_pair_plot(df):
    """
    Affiche les relations entre toutes les variables numériques du dataset à l'aide d'un pair plot.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    sns.pairplot(df[numeric_cols], diag_kind='kde', corner=True)
    plt.suptitle("Pair Plot of Numerical Variables", y=1.02)
    plt.show()

# ─────────────────────────────────────────────
# Fonction de visualisation avec Count Plot
# ─────────────────────────────────────────────
def plot_count_plot(df, column):
    """
    Affiche la répartition d'une variable catégorielle à l'aide d'un count plot.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(x=df[column], palette='pastel')
    plt.title(f"Count Plot of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

# ─────────────────────────────────────────────
# Fonction de visualisation avec waterfall chart
# ─────────────────────────────────────────────
def plot_waterfall_chart(df, column, value_column):
    """
    Affiche la contribution de chaque catégorie d'une variable catégorielle à une variable numérique à l'aide d'un waterfall chart.
    """
    df_sorted = df.groupby(column)[value_column].sum().sort_values(ascending=False).reset_index()
    df_sorted['cumulative'] = df_sorted[value_column].cumsum()
    df_sorted['previous_cumulative'] = df_sorted['cumulative'] - df_sorted[value_column]

    plt.figure(figsize=(12, 6))
    plt.bar(df_sorted[column], df_sorted[value_column], bottom=df_sorted['previous_cumulative'], color='lightcoral')
    plt.title(f"Waterfall Chart of {value_column} by {column}")
    plt.xlabel(column)
    plt.ylabel(value_column)
    plt.xticks(rotation=45)
    plt.show()

# ─────────────────────────────────────────────
# Fonction de visualisation avec Treemap
# ─────────────────────────────────────────────
def plot_treemap(df, column, value_column):
    """
    Affiche la répartition d'une variable catégorielle à l'aide d'un treemap.
    """
    import squarify  # Assurez-vous d'avoir installé la bibliothèque squarify

    df_sorted = df.groupby(column)[value_column].sum().sort_values(ascending=False).reset_index()
    
    plt.figure(figsize=(12, 6))
    squarify.plot(sizes=df_sorted[value_column], label=df_sorted[column], alpha=0.8)
    plt.title(f"Treemap of {value_column} by {column}")
    plt.axis('off')
    plt.show()

# ─────────────────────────────────────────────
# Fonction de visualisation avec Regplot
# ─────────────────────────────────────────────
def plot_regplot(df, column1, column2):
    """
    Affiche la relation entre deux variables numériques à l'aide d'un regplot.
    """
    plt.figure(figsize=(10, 6))
    sns.regplot(x=df[column1], y=df[column2], scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
    plt.title(f"Regplot of {column1} vs {column2}")
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.show()
