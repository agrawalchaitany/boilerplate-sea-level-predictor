import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    
    plt.scatter(x=df["Year"], y=df['CSIRO Adjusted Sea Level'], color="blue", label="Data")


    # Create first line of best fit
    slope , intercept,_,_,_=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2051) 
    sea_levels_extended=slope*(years_extended) + intercept
    
    plt.plot(years_extended, sea_levels_extended,label=f"best fit {df['Year']} - 2051", color="red")


    # Create second line of best fit
    df_recent=df.loc[df['Year'] >= 2000]
    slope_recent , intercept_recent,_,_,_=linregress(df_recent['Year'],df_recent['CSIRO Adjusted Sea Level'])
    years_recent= np.arange(2000,2051)
    sea_levels_recent=slope_recent*(years_recent) + intercept_recent
    plt.plot(years_recent, sea_levels_recent, label="best fit 2000 - 2050", color="green")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    plt.grid(True)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()