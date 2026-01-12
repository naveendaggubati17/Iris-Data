# Basic Data Analysis and Visualization using Pandas and Matplotlib
This program shows how to load a CSV file with **Pandas**, perform basic data analysis, and create four separate visualizations using **Matplotlib** and **Seaborn** (each as its own image). It uses the classic Iris dataset with columns `sepal_length`, `sepal_width`, `petal_length`, `petal_width`, and `species`.

## What the script does

- Loads `iris.csv` into a Pandas DataFrame  
- Prints basic information and summary statistics  
- Calculates the average of selected columns  
- Creates 4 separate plots:
  - Bar chart of average measurements per species  
  - Scatter plot: sepal length vs sepal width  
  - Scatter plot: petal length vs petal width  
  - Heatmap of feature correlations  

***

## Code walkthrough

### 1. Imports and dataset

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("iris.csv")
```

- `pandas` is used for data loading and analysis.  
- `matplotlib.pyplot` is used for plotting.  
- `seaborn` is used to draw a nicer correlation heatmap.  
- `read_csv("iris.csv")` loads the Iris dataset from a CSV file in the same folder.

### 2. Basic data analysis

```python
print("Shape (rows, columns):", df.shape)
print(df.head())
print(df.info())
print(df.describe())
```

- `df.shape` prints how many rows and columns are in the dataset (150 × 5 for Iris).
- `df.head()` shows the first 5 rows to get a quick look at the data.  
- `df.info()` shows column types and non-null counts.  
- `df.describe()` gives summary statistics (mean, std, min, max, quartiles) for numeric columns.

### 3. Average of selected columns

```python
avg_sepal_length = df["sepal_length"].mean()
avg_petal_width = df["petal_width"].mean()
print(f"Average sepal_length: {avg_sepal_length:.2f}")
print(f"Average petal_width: {avg_petal_width:.2f}")
```

- Uses `mean()` to calculate the average of `sepal_length` and `petal_width`.  
- Formatted to two decimal places with f-strings.

### 4. Bar chart

```python
plt.figure(figsize=(8, 6))
species_means = df.groupby("species")[["sepal_length",
                                       "sepal_width",
                                       "petal_length",
                                       "petal_width"]].mean()
species_means.plot(kind="bar")
plt.title("Average Measurements by Species")
plt.ylabel("Length / Width (cm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

- `groupby("species").mean()` computes the average of each numeric feature per species.
- `plot(kind="bar")` draws a bar chart of these averages.  
- `plt.figure(...)` ensures this bar chart is on its own figure.  
- `plt.show()` displays the first image.

### 5. Sepal scatter plot

```python
plt.figure(figsize=(8, 6))
for species, group in df.groupby("species"):
    plt.scatter(group["sepal_length"],
                group["sepal_width"],
                label=species)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width")
plt.legend()
plt.tight_layout()
plt.show()
```

- Loops over each `species` and plots its points with `plt.scatter`.  
- X-axis: `sepal_length`, Y-axis: `sepal_width`.  
- `plt.legend()` labels the species clusters; `plt.show()` displays the second figure.

### 6. Petal scatter plot

```python
plt.figure(figsize=(8, 6))
for species, group in df.groupby("species"):
    plt.scatter(group["petal_length"],
                group["petal_width"],
                label=species)
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs Petal Width")
plt.legend()
plt.tight_layout()
plt.show()
```

- Similar to the sepal plot, but for petals: `petal_length` vs `petal_width`.  
- Clearly shows stronger separation between species compared to sepal features.

### 7. Correlation heatmap

```python
plt.figure(figsize=(8, 6))
numeric_df = df.drop(columns=["species"])
corr_matrix = numeric_df.corr()

sns.heatmap(corr_matrix,
            annot=True,
            cmap="coolwarm",
            fmt=".2f")
plt.title("Correlation Heatmap of Iris Features")
plt.tight_layout()
plt.show()
```

- Removes the non-numeric `species` column using `drop(columns=["species"])`.  
- `corr()` computes the correlation matrix between the four numeric features.
- `sns.heatmap` visualizes correlations with colors and numeric annotations.

### 8. Printed insights

```python
print("\n=== Insights and Observations ===")
print("1. Dataset has 150 rows and 5 columns (4 numeric features + species).")
print("2. Petal length and petal width are highly positively correlated, forming a near-linear relationship.")
print("3. Setosa shows smaller petal measurements and relatively larger sepal width than the other species.")
print("4. Separate figures make it easier to inspect each pattern individually.")
```

- Summarizes what the analysis and plots reveal:
  - Data size and structure.  
  - Strong correlation between petal length and width.  
  - Species differences visible in plots and bar chart.
  - Benefit of separate figures for clearer inspection.

***

### 9. Output

1. Dataset has 150 rows and 5 columns (4 numeric features + species).
2. Petal length and petal width are highly positively correlated, forming a near-linear relationship.
3. Setosa shows smaller petal measurements and relatively larger sepal width than the other species.
4. Separate figures make it easier to inspect each pattern (averages, sepal relations, petal relations, overall correlations) individually.

***

### 10. Image Outputs

1. Average Measurements by Species(Bar Chart):


   <img width="424" height="280" alt="image" src="https://github.com/user-attachments/assets/90670d06-18a0-4b8d-9143-835a70347cff" />


2. Sepal scatter plot:

   
   <img width="568" height="424" alt="image" src="https://github.com/user-attachments/assets/3cd24c37-1d44-4787-b2ad-e051cae6a115" />

   
3. Petal scatter plot:

   
   <img width="568" height="424" alt="image" src="https://github.com/user-attachments/assets/63442047-36eb-4307-a055-27dade7fe998" />


4. Correlation Heatmap:

   
   <img width="538" height="424" alt="image" src="https://github.com/user-attachments/assets/740a8d88-272b-47f8-892c-bd291ad508d7" />






