import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")
    print(df)


    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    #plt.title('Scatter Plot')
    #plt.xlabel('Year')
    #plt.ylabel('CSIRO Adjusted Sea Level')
    plt.show()

    # Create first line of best fit
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Observed Data')
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    year_2050 = 2050
    predicted_sea_level_2050 = slope * year_2050 + intercept

    plt.plot([df['Year'].min(), year_2050], [intercept, predicted_sea_level_2050], color='red', label='Line of Best Fit')

    #plt.title('Sea Level Rise Prediction')
    #plt.xlabel('Year')
    #plt.ylabel('Sea Level Rise (mm)')
    plt.legend()
    plt.show()
    print(f"Predicted sea level rise in 2050: {predicted_sea_level_2050:.2f} mm")


    # Create second line of best fit
    mask=df['Year']>=2000
    year_between_2000and_above=df[mask]
    year_between_2000and_above
    plt.scatter(year_between_2000and_above['Year'],year_between_2000and_above['CSIRO Adjusted Sea Level'])
    slope, intercept, r_value, p_value, std_err = linregress(year_between_2000and_above['Year'], year_between_2000and_above['CSIRO Adjusted Sea Level'])


    year_2050 = 2050
    predicted_sea_level_2050 = slope * year_2050 + intercept


    plt.plot([year_between_2000and_above['Year'].min(), year_2050], [intercept, predicted_sea_level_2050], color='Green', label='Line of Best Fit')

    plt.title('Sea Level Rise Prediction')
    #plt.xlabel('Year')
    #plt.ylabel('Sea Level Rise (mm)')
    #plt.title("Scatter plot from the year 2000 to the most recent year in the dataset")
    plt.legend()
    plt.show()

    print(f"Predicted sea level rise in 2050: {predicted_sea_level_2050:.2f} mm")


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in sea Level")
     
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()