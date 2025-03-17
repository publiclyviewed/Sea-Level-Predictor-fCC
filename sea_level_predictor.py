import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Data")

    # Create first line of best fit
    slope1, intercept1, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred1 = pd.Series(range(1880, 2051))
    y_pred1 = slope1 * x_pred1 + intercept1
    plt.plot(x_pred1, y_pred1, color="red", label="Best fit line 1880-2050")

    # Create second line of best fit for data from 2000 onwards
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, r_value, p_value, std_err = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = slope2 * x_pred2 + intercept2
    plt.plot(x_pred2, y_pred2, color="green", label="Best fit line 2000-2050")

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()

    # Save plot and return data for testing
    plt.savefig("sea_level_plot.png")
    return plt.gca()
