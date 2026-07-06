import pandas as pd
df=pd.read_csv("tested.csv")

#  How many missing values are there in each column?
print(df.isnull().sum())

# Which column has the most missing values?
print(df.isnull().sum().idxmax())

# How many missing values are in Age?
print(df["Age"].isnull().sum())

# How many missing values are in Cabin?
print(df["Cabin"].isnull().sum())

# How many missing values are in Embarked?
print(df["Embarked"].isnull().sum())

# Fill missing Age values with the mean age.
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Verify that Age has no missing values after filling.
print(df["Age"].isnull().sum())
# Level 3
# What is the average age?
print(df["Age"].mean())

# What is the maximum age?
print(df["Age"].max())

# What is the minimum age?
print(df["Age"].min())

# What is the average fare?
print(df["Fare"].mean())

# What is the highest fare?
print(df["Fare"].max())

# What is the lowest fare?
print(df["Fare"].min())

# What is the total fare of all passengers?
print(df["Fare"].sum())

# How many passengers have non-null ages?
print(df["Age"].count())

# What is the standard deviation of Age?
print(df["Age"].std())

# What is the standard deviation of Fare?
print(df["Fare"].std())
# Level 4
# Show the 10 oldest passengers.
print(df.sort_values("Age", ascending=False).head(10))

# Show the 10 youngest passengers.
print(df.sort_values("Age").head(10))

# Show the 10 highest fares.
print(df.sort_values("Fare", ascending=False).head(10))

# Show the 10 lowest fares.
print(df.sort_values("Fare").head(10))

# Sort passengers by Age descending.
print(df.sort_values("Age", ascending=False))

# Sort passengers by Fare ascending.
print(df.sort_values("Fare"))
# Level 5
# Show all passengers older than 50.
print(df[df["Age"] > 50])

# Show all passengers younger than 18.
print(df[df["Age"] < 18])

# Show all female passengers.
print(df[df["Sex"] == "female"])

# Show all male passengers.
print(df[df["Sex"] == "male"])

# Show passengers who paid more than 100 fare.
print(df[df["Fare"] > 100])

# Show passengers from first class.
print(df[df["Pclass"] == 1])

# Show passengers who survived.
print(df[df["Survived"] == 1])

# Show passengers who did not survive.
print(df[df["Survived"] == 0])
# Level 6
# Find average age by gender.
print(df.groupby("Sex")["Age"].mean())

# Find average fare by gender.
print(df.groupby("Sex")["Fare"].mean())

# Count males and females.
print(df["Sex"].value_counts())

# Count passengers in each class.
print(df["Pclass"].value_counts())

# Find average fare in each passenger class.
print(df.groupby("Pclass")["Fare"].mean())

# Find average age in each passenger class.
print(df.groupby("Pclass")["Age"].mean())

# Find survival count by gender.
print(df.groupby("Sex")["Survived"].sum())

# Find survival count by passenger class.
print(df.groupby("Pclass")["Survived"].sum())

# Find average fare paid by survivors and non-survivors.
print(df.groupby("Survived")["Fare"].mean())
# Challenge Questions
# Who is the oldest passenger?
print(df.loc[df["Age"].idxmax()])

# Who paid the highest fare?
print(df.loc[df["Fare"].idxmax()])

# What percentage of passengers survived?
print(df["Survived"].mean() * 100)

# Which gender had a higher survival rate?
print(df.groupby("Sex")["Survived"].mean())

# Which passenger class had the highest average fare?
print(df.groupby("Pclass")["Fare"].mean())

# Which passenger class had the highest survival count?
print(df.groupby("Pclass")["Survived"].sum())

# How many children (Age < 18) survived?
print(df[(df["Age"] < 18) & (df["Survived"] == 1)].shape[0])

# How many women survived?
print(df[(df["Sex"] == "female") & (df["Survived"] == 1)].shape[0])

# How many men survived?
print(df[(df["Sex"] == "male") & (df["Survived"] == 1)].shape[0])

# Which age appears most frequently?
print(df["Age"].mode())
