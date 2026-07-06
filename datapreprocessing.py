"""
===========================================================
OUTLIER DETECTION AND HANDLING USING PYTHON
Author : Prem Mishra
Description:
This script demonstrates different techniques used to
detect and handle outliers in a dataset.

Methods Covered:
1. Mean Comparison
2. Z-Score
3. IQR (Interquartile Range)
4. Box Plot
5. Scatter Plot
6. Winsorization
7. Isolation Forest

Libraries Used:
- NumPy
- Matplotlib
- SciPy
- Scikit-Learn
===========================================================
"""

# ==========================
# Import Required Libraries
# ==========================

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats.mstats import winsorize
from sklearn.ensemble import IsolationForest


# ============================================================
# STEP 1 : Create Dataset
# ============================================================

# Dataset without any outlier
regular_data = np.array([10, 20, 30, 40, 50])

# Dataset containing an extreme value (500)
outlier_data = np.array([10, 20, 30, 40, 500])


# ============================================================
# STEP 2 : Compare Mean
# ============================================================

# Mean is very sensitive to outliers.
# Observe how a single extreme value changes the average.

print("=" * 50)
print("MEAN COMPARISON")
print("=" * 50)

print("Regular Data :", regular_data)
print("Mean :", regular_data.mean())

print()

print("Data With Outlier :", outlier_data)
print("Mean :", outlier_data.mean())


# ============================================================
# STEP 3 : Detect Outlier using Z-Score
# ============================================================

"""
Z-Score tells how many standard deviations a value is
away from the mean.

Formula:
    Z = (Value - Mean) / Standard Deviation

Rule:
|Z| > 3  → Outlier
"""

print("\n" + "=" * 50)
print("Z-SCORE METHOD")
print("=" * 50)

z_scores = np.abs(stats.zscore(outlier_data))

print("Z Scores")
print(z_scores)

detected = outlier_data[z_scores > 3]

print("Detected Outliers")
print(detected)

# Note:
# In very small datasets, Z-score may fail because
# the outlier itself increases the mean and standard deviation.


# ============================================================
# STEP 4 : Detect Outlier using IQR
# ============================================================

"""
IQR = Q3 - Q1

Lower Limit = Q1 - 1.5 * IQR
Upper Limit = Q3 + 1.5 * IQR

Any value outside these limits is considered an outlier.
"""

print("\n" + "=" * 50)
print("IQR METHOD")
print("=" * 50)

Q1 = np.percentile(outlier_data, 25)
Q3 = np.percentile(outlier_data, 75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("Q1 :", Q1)
print("Q3 :", Q3)
print("IQR :", IQR)

print("Lower Limit :", lower_limit)
print("Upper Limit :", upper_limit)

iqr_outliers = outlier_data[
    (outlier_data < lower_limit) |
    (outlier_data > upper_limit)
]

print("Detected Outliers")
print(iqr_outliers)


# ============================================================
# STEP 5 : Visualize using Box Plot
# ============================================================

"""
A Box Plot displays

Minimum
Q1
Median
Q3
Maximum

Outliers appear as separate points outside the whiskers.
"""

plt.figure(figsize=(6, 4))

plt.boxplot(outlier_data)

plt.title("Box Plot")
plt.ylabel("Values")

plt.show()


# ============================================================
# STEP 6 : Visualize using Scatter Plot
# ============================================================

"""
Scatter Plot displays every data point.

Outliers are easy to identify because they are
far away from the majority of points.
"""

plt.figure(figsize=(6, 4))

plt.scatter(range(len(outlier_data)), outlier_data)

plt.title("Scatter Plot")
plt.xlabel("Index")
plt.ylabel("Value")

plt.grid(True)

plt.show()


# ============================================================
# STEP 7 : Winsorization
# ============================================================

"""
Winsorization reduces the effect of outliers.

Instead of removing an outlier,
it replaces it with a less extreme value.

Original:
10 20 30 40 500

Example after Winsorization:
20 20 30 40 40
"""

print("\n" + "=" * 50)
print("WINSORIZATION")
print("=" * 50)

winsorized_data = winsorize(outlier_data, limits=[0.2, 0.2])

print("Original Data")
print(outlier_data)

print("Winsorized Data")
print(winsorized_data)


# ============================================================
# STEP 8 : Isolation Forest
# ============================================================

"""
Isolation Forest is a Machine Learning algorithm.

Instead of using statistics,
it isolates observations.

Output:
1  -> Normal Observation
-1 -> Outlier
"""

print("\n" + "=" * 50)
print("ISOLATION FOREST")
print("=" * 50)

model = IsolationForest(
    contamination=0.2,
    random_state=42
)

prediction = model.fit_predict(outlier_data.reshape(-1, 1))

print("Predictions")
print(prediction)

print()

for value, result in zip(outlier_data, prediction):

    if result == -1:
        print(f"{value} --> Outlier")

    else:
        print(f"{value} --> Normal")


# ============================================================
# END OF PROGRAM
# ============================================================

print("\n" + "=" * 50)
print("Summary")
print("=" * 50)

print("✔ Mean is affected by outliers.")
print("✔ Z-Score works well for normally distributed data.")
print("✔ IQR works well for skewed datasets.")
print("✔ Box Plot visually detects outliers.")
print("✔ Scatter Plot shows isolated points.")
print("✔ Winsorization reduces the impact of outliers.")
print("✔ Isolation Forest detects outliers using Machine Learning.")
