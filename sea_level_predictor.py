import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')#, index_col='Year', parse_dates=True)

    # Create scatter plot
    plt.figure(figsize=(10, 4))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='red', label='Data')

    # Define the range of years for plotting the lines
    years_full = pd.Series(range(df['Year'].min(), 2051))
    years_recent = pd.Series(range(2000, 2051))

    # Create first line of best fit
    slope_all, intercept_all, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    sea_level_pred_all = intercept_all + slope_all * years_full
    plt.plot(years_full, sea_level_pred_all, color='black', label='Best fit line (1880-2050)')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value, p_value, std_err = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    sea_level_pred_2000 = intercept_2000 + slope_2000 * years_full
    plt.plot(years_full, sea_level_pred_2000, color='green', label='Best fit line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
