# import pandas as pd
# df=pd.read_csv("tested.csv")
# print(df.head())   #it will print the first 5 rows of the dataset
# print(df.info())   #it will print the information about the dataset
# print(df.tail())   #it will print the last 5 rows of the dataset
# print(df.shape)   #it will print the shape of the dataset
# print(df.columns) # it will print the columns of the dataset
# print(df.head(50))
# print(len(df)) # it will print the number of rows in the dataset
# print("Number of records:", len(df))

# print("Number of elements:", df.size)

# print("Column names:")
# print(df.columns)

# print("Column types:")
# print(df.dtypes)

# print(df.describe()) # it will print the statistical summary of the dataset

# print(df["Age"].describe()) # it will print the summary of the Age column
# print(df.std(numeric_only=True)) # it will print the standard deviation of the numeric columns in the dataset
# print(df.head(50).mean(numeric_only=True)) # it will print the mean of the numeric columns in the first 50 rows of the dataset
# print(df.sort_values("Age")) # it will print the dataset sorted by the Age column in ascending order
# print(df.head().sort_values("Age")) # it will print the first 5 rows of the dataset sorted by the Age column in ascending order
# print(df.sort_values("Age", ascending=False)) # it will print the dataset sorted by the Age column in descending order
# df.sort_values("Fare", ascending=False) # it will print the dataset sorted by the Fare column in descending order
# print(df.sort_values("Age", ascending=False).head(10)) # it will print the first 10 rows of the dataset sorted by the Age column in descending order
# print(df.head(10).sort_values("Age", ascending=False)) # it will print the first 10 rows of the dataset sorted by the Age column in descending order
# print(df.isnull().sum()) # it will print the number of missing values in each column of the dataset
# print(df.isnull().any()) # it will print whether there are any missing values in each column of the dataset
# df.dropna() # it will drop the rows with missing values from the dataset
# print(df["Age"] = df["Age"].fillna(df["Age"].mean()) ) # it will fill the missing values in the Age column with the mean of the Age column

#  aggregation value
# aggregation=summarize mnay values into one value
# df["Age"].mean() # it will print the mean of the Age column
# df["Age"].max() # it will print the maximum value of the Age column
# df["Age"].min() # it will print the minimum value of the Age column
# print(df.groupby("Sex")["Age"].mean()) # it will print the mean of the Age column for each group
# print(df.groupby("Pclass")["Fare"].mean()) # it will print the mean of the Fare column for each group


#questions to solve
# How many rows are in the dataset?
# How many columns are in the dataset?
# What are the column names?
# What is the data type of each column?
# How many elements are there in total?
# Display the first 10 rows.
# Display the last 15 rows.
# Show summary statistics for all numeric columns.
# Show summary statistics only for the Age column.
# Show summary statistics only for the Fare column.

# Level 2: Missing Values
# How many missing values are there in each column?
# Which column has the most missing values?
# How many missing values are in Age?
# How many missing values are in Cabin?
# How many missing values are in Embarked?
# Fill missing Age values with the mean age.
# Verify that Age has no missing values after filling.

# Level 3: Aggregation Functions
# What is the average age?
# What is the maximum age?
# What is the minimum age?
# What is the average fare?
# What is the highest fare?
# What is the lowest fare?
# What is the total fare of all passengers?
# How many passengers have non-null ages?
# What is the standard deviation of Age?
# What is the standard deviation of Fare?

# Level 4: Sorting
# Show the 10 oldest passengers.
# Show the 10 youngest passengers.
# Show the 10 highest fares.
# Show the 10 lowest fares.
# Sort passengers by Age descending.
# Sort passengers by Fare ascending.
# Level 5: Filtering
# Show all passengers older than 50.
# Show all passengers younger than 18.
# Show all female passengers.
# Show all male passengers.
# Show passengers who paid more than 100 fare.
# Show passengers from first class (Pclass = 1).
# Show passengers who survived.
# Show passengers who did not survive.

# Level 6: GroupBy
# Find average age by gender.
# Find average fare by gender.
# Count males and females.
# Count passengers in each class.
# Find average fare in each passenger class.
# Find average age in each passenger class.
# Find survival count by gender.
# Find survival count by passenger class.
# Find average fare paid by survivors and non-survivors.

# Challenge Questions
# Who is the oldest passenger?
# Who paid the highest fare?
# What percentage of passengers survived?
# Which gender had a higher survival rate?
# Which passenger class had the highest average fare?
# Which passenger class had the highest survival count?
# How many children (Age < 18) survived?
# How many women survived?
# How many men survived?
# Which age appears most frequently?
