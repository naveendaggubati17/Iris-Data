# Program: Basic Data Analysis and Visualization using Pandas and Matplotlib
# Dataset: iris.csv (sepal_length, sepal_width, petal_length, petal_width, species)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/Sunil Daggubati/Downloads/iris.csv")  # Ensure iris.csv is in the same folder
print(df)

print("Shape (rows, columns):", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nInfo:")
print(df.info())
print("\nStatistical summary (numeric columns):")
print(df.describe())

# Average of selected columns
avg_sepal_length = df["sepal_length"].mean()
avg_petal_width = df["petal_width"].mean()
print(f"\nAverage sepal_length: {avg_sepal_length:.2f}")
print(f"Average petal_width: {avg_petal_width:.2f}")  # Features are in cm

plt.figure(figsize=(8, 6))
species_means = df.groupby("species")[["sepal_length", "sepal_width", "petal_length", "petal_width"]].mean()
species_means.plot(kind="bar")
plt.title("Average Measurements by Species")
plt.ylabel("Length / Width (cm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()  # First image (bar chart) 

plt.figure(figsize=(8, 6))
for species, group in df.groupby("species"): plt.scatter(group["sepal_length"], group["sepal_width"], label=species)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width")
plt.legend()
plt.tight_layout()
plt.show()  # Second image (scatter 1) 

plt.figure(figsize=(8, 6))
for species, group in df.groupby("species"): plt.scatter(group["petal_length"], group["petal_width"], label=species)
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs Petal Width")
plt.legend()
plt.tight_layout()
plt.show()  # Third image (scatter 2) 

plt.figure(figsize=(8, 6))
numeric_df = df.drop(columns=["species"])
corr_matrix = numeric_df.corr()  # correlation matrix for 4 numeric features

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Iris Features")
plt.tight_layout()
plt.show()  # Fourth image (heatmap)

print("1. Dataset has 150 rows and 5 columns (4 numeric features + species).")
print("2. Petal length and petal width are highly positively correlated, forming a near-linear relationship.") 
print("3. Setosa shows smaller petal measurements and relatively larger sepal width than the other species.")
print("4. Separate figures make it easier to inspect each pattern (averages, sepal relations, petal relations, overall correlations) individually.") 

