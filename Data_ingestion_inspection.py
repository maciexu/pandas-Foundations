"""
Plotting series using pandas

Data visualization is often a very effective first step in gaining a rough understanding of a data set to be analyzed. 
Pandas provides data visualization by both depending upon and interoperating with the matplotlib library. 
You will now explore some of the basic plotting mechanics with pandas as well as related matplotlib options. 
We have pre-loaded a pandas DataFrame df which contains the data you need. 
Your job is to use the DataFrame method df.plot() to visualize the data, 
and then explore the optional matplotlib input parameters that this .plot() method accepts.

The pandas .plot() method makes calls to matplotlib to construct the plots. 
This means that you can use the skills you've learned in previous visualization courses to customize the plot. 
In this exercise, you'll add a custom title and axis labels to the figure.

Before plotting, inspect the DataFrame in the IPython Shell using df.head(). 
Also, use type(df) and note that it is a single column DataFrame.
"""
# Create a plot with color='red'
df.plot(color='r')

# Add a title
plt.title('Temperature in Austin')

# Specify the x-axis label
plt.xlabel('Hours since midnight August 1, 2010')

# Specify the y-axis label
plt.ylabel('Temperature (degrees F)')

# Display the plot
plt.show()

"""
Plotting DataFrames

Comparing data from several columns can be very illuminating. Pandas makes doing so easy with multi-column DataFrames. 
By default, calling df.plot() will cause pandas to over-plot all column data, with each column as a single line. 
In this exercise, we have pre-loaded three columns of data from a weather data set - temperature, dew point, and pressure - 
but the problem is that pressure has different units of measure. 
The pressure data, measured in Atmospheres, has a different vertical scaling than that of the other two data columns, 
which are both measured in degrees Fahrenheit.

Your job is to plot all columns as a multi-line plot, to see the nature of vertical scaling problem. 
Then, use a list of column names passed into the DataFrame df[column_list] to limit plotting to just one column, 
and then just 2 columns of data. When you are finished, you will have created 4 plots. 
You can cycle through them by clicking on the 'Previous Plot' and 'Next Plot' buttons.
"""

# Plot all columns (default)
df.plot()
plt.show()

# Plot all columns as subplots
df.plot(subplots=True)
plt.show()

# Plot just the Dew Point data
column_list1 = ['Dew Point (deg F)']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature (deg F)','Dew Point (deg F)']
df[column_list2].plot()
plt.show()

