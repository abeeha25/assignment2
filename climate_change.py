# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_world_bank_data(filename: str) -> (pd.DataFrame, pd.DataFrame):
    """
    Reads World Bank data from a file and returns two dataframes.

    Args:
        filename: The path to the World Bank data file.

    Returns:
        df_countries: A DataFrame containing country names.
        df_years: A DataFrame containing indicator values over years.
    """

    # Read the Excel spreadsheet
    df = pd.read_excel(filename)

    # Extract and format country data
    df_countries = pd.DataFrame(df.iloc[3:, 0], columns=["Country Name"])
    df_countries = df_countries.reset_index(drop=True)

    # Extract and format indicator data
    df_years = pd.DataFrame(df.iloc[3:, 1:])
    df_years.reset_index(drop=True, inplace=True)
    df_years.columns = df.iloc[2, 1:]

    return df_countries, df_years


def analyze_summary_statistics(df_years: pd.DataFrame) -> None:
    """
    Analyzes and visualizes summary statistics.

    Args:
        df_years: A DataFrame containing indicator values over years.
    """

    # Print descriptive statistics
    print(df_years.describe(include="all"))

    # Visualize summary statistics with a bar chart
    fig, ax = plt.subplots(figsize=(20, 20))
    df_years.describe().plot(kind="bar", ax=ax)
    ax.set_title("Summary Statistics for Each Indicator")
    ax.set_xlabel("Indicators")
    ax.set_ylabel("Values")
    plt.tight_layout()
    plt.show()


def analyze_correlation(df_years: pd.DataFrame) -> None:
    """
    Analyzes and visualizes correlation between numeric indicators.

    Args:
        df_years: A DataFrame containing indicator values over years.
    """

    # Select only numeric columns for correlation analysis
    numeric_columns = df_years.select_dtypes(include=['number'])

    # Calculate the correlation matrix
    correlation_matrix = numeric_columns.corr()

    # Print the correlation matrix
    print(correlation_matrix)

    # Visualize correlation with a heatmap
    plt.figure(figsize=(25, 25))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation between Numeric Indicators")
    plt.show()


def visualize_time_series(df_years: pd.DataFrame) -> None:
    """
    Visualizes time series data.

    Args:
        df_years: A DataFrame containing indicator values over years.
    """

    # Plot time series data
    df_years.plot(figsize=(20, 20))
    plt.title("Change in the Indicators over Time")
    plt.xlabel("Years")
    plt.ylabel("Values")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # dataset file path
    data_file_path = "API_CLIMATE_CHANGE_WB.xls"
    
    # Read data from the World Bank file
    df_countries, df_years = read_world_bank_data(data_file_path)

    # Analyze and visualize summary statistics
    analyze_summary_statistics(df_years)

    # Analyze and visualize correlation between indicators
    analyze_correlation(df_years)

    # Visualize time series data
    visualize_time_series(df_years)
