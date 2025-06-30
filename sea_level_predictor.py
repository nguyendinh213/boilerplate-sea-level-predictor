import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Original Data", alpha=0.7)

    # First line of best fit (entire dataset)
    res1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred1 = pd.Series(range(1880, 2051))
    y_pred1 = res1.slope * x_pred1 + res1.intercept
    plt.plot(x_pred1, y_pred1, 'r', label="Fit: 1880–2050")

    # Second line of best fit (from year 2000)
    df_recent = df[df["Year"] >= 2000]
    res2 = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = res2.slope * x_pred2 + res2.intercept
    plt.plot(x_pred2, y_pred2, 'g', label="Fit: 2000–2050")

    # Formatting the plot
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid(True)

    # Save plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()
