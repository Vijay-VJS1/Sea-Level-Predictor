import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
pd.set_option("display.precision", 16)
def draw_plot():
    # Read data from file
    df1=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df1['Year'],df1['CSIRO Adjusted Sea Level'],color="green")

    # Create first line of best fit
    line1=linregress(df1["Year"],df1['CSIRO Adjusted Sea Level'])
    slope1=line1.slope
    y_int1=line1.intercept
    x1 = np.arange(1880,2051)
    y1 = x1*slope1 + y_int1

    plt.plot(x1,y1,color="red")

    # Create second line of best fit
    df2=df1[df1['Year']>=2000]
    full_df2 = pd.concat([df2,pd.DataFrame({"Year":[2050]})],ignore_index=True)
    line2=linregress(df2["Year"],df2['CSIRO Adjusted Sea Level'])
    slope2=line2.slope
    y_int2=line2.intercept
    x2 = np.arange(2000,2051)
    y2 = x2*slope2 + y_int2

    plt.plot(x2,y2,color="blue")

    # Add labels and title
    plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()