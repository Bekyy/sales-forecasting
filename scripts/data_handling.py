import pandas as pd
import numpy as np

def missing_values_table(df):
    # Total missing values
    mis_val = df.isnull().sum()

    # Percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)

    # dtype of missing values
    mis_val_dtype = df.dtypes

    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent, mis_val_dtype], axis=1)

    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
    columns={0: 'Missing Values', 1: '% of Total Values', 2: 'Dtype'})

    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)

    # Print some summary information
    print("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
          "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")

    # Return the dataframe with missing information
    return mis_val_table_ren_columns


def handling_missing_data(data):
    # Replace inf and -inf with NaN
    data.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Step 1: Calculate missing data and remove columns with more than 90% missing data
    missing_data = data.isnull().sum().sort_values(ascending=False)
    missing_percentage = (missing_data / len(data)) * 100
    datacleaned = data.drop(columns=missing_data[missing_percentage > 90].index)

    # Step 2: Impute missing values in numeric columns using 0 or the mean
    numeric_cols = datacleaned.select_dtypes(include=['float64', 'int64']).columns
    datacleaned[numeric_cols] = datacleaned[numeric_cols].fillna(0)

    # Step 3: Impute missing values in date columns using forward fill or backward fill
    date_cols = datacleaned.select_dtypes(include=['datetime64[ns]']).columns
    datacleaned[date_cols] = datacleaned[date_cols].fillna(method='ffill').fillna(method='bfill')

    # Step 4: Impute missing values in categorical columns using 'unknown'
    categorical_cols = datacleaned.select_dtypes(include=['object']).columns
    datacleaned[categorical_cols] = datacleaned[categorical_cols].fillna('unknown')

    return datacleaned


