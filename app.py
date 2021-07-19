import pandas as pd

df = pd.read_csv('data.csv')


#to_string() to print the entire DataFrame
print(df.to_string())

# for getting a quick overview of the DataFrame, is the head() method.
print(df.head(10))

#tail() method for viewing the last rows of the DataFrame
print(df.tail(10))

#info() gives you more information about the data set.
print(df.info())

# dropna() method returns a new DataFrame, and will not change the original.
new_df = df.dropna()
print(new_df.to_string())

# dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame.
df.dropna(inplace=True)
print(df.to_string())


# The fillna() method allows us to replace empty cells with a value:
df.fillna(5000,inplace=True)
print(df.to_string())

# df = pd.read_csv('data1.csv')

# Mean = the average value (the sum of all values divided by number of values).
x = df["Calories"].mean()
df["Calories"].fillna(x,inplace=True)
print(df.to_string())

# Median = the value in the middle, after you have sorted all values ascending.
x = df["Calories"].median()
df["Calories"].fillna(x,inplace=True)
print(df.to_string())


# Mode = the value that appears most frequently.
x = df["Calories"].mode()[0]
df['Calories'].fillna(x, inplace=True)
print(df.to_string())

# Convert into a Correct Format
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())

# Remove rows with a NULL value in the "Date" column:
df['Date'] = pd.to_datetime(df['Date'])

df.dropna(subset=['Date'], inplace = True)
print(df.to_string())



#Pandas use the loc attribute to return one or more specified row(s)
df.loc[7,'Duration'] = 53
print(df.to_string())

# If the value is higher than 120, set it to 120:
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df.to_string())


# Removing rows
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

print(df.to_string())

# Returns True for every row that is a duplicate, othwerwise False
print(df.duplicated())


# remove duplicates
df.drop_duplicates(inplace = True)
print(df.to_string())


