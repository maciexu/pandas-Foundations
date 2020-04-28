"""
pandas line plots

.plot() method will place the Index values on the x-axis by default. 
In this exercise, you'll practice making line plots with specific columns on the x and y axes.

You will work with a dataset consisting of monthly stock prices in 2015 for AAPL, GOOG, and IBM. 
The stock prices were obtained from Yahoo Finance. 
Your job is to plot the 'Month' column on the x-axis and the AAPL and IBM prices on the y-axis using a list of column names.

All necessary modules have been imported for you, and the DataFrame is available in the workspace as df. 
Explore it using methods such as .head(), .info(), and .describe() to see the column names.
"""
# Create a list of y-axis column names: y_columns
y_columns = ['AAPL', 'IBM']

# Generate a line plot
df.plot(x='Month', y=y_columns)

# Add the title
plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()


"""
pandas scatter plots

Pandas scatter plots are generated using the kind='scatter' keyword argument. 
Scatter plots require that the x and y columns be chosen by specifying the x and y parameters inside .plot(). 
Scatter plots also take an s keyword argument to provide the radius of each circle to plot in pixels.

In this exercise, you're going to plot fuel efficiency (miles-per-gallon) versus horse-power 
for 392 automobiles manufactured from 1970 to 1982 from the UCI Machine Learning Repository.
https://archive.ics.uci.edu/ml/datasets/Auto+MPG

The size of each circle is provided as a NumPy array called sizes. This array contains the normalized 'weight' of each automobile in the dataset.
# Generate a scatter plot
df.plot(kind='scatter', x='hp', y='mpg', s=sizes)

# Add the title
plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
plt.xlabel('Horse-power')

# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
plt.show()


"""
pandas box plots

While pandas can plot multiple columns of data in a single figure, making plots that share the same x and y axes, 
there are cases where two columns cannot be plotted together because their units do not match. 
The .plot() method can generate subplots for each column being plotted. Here, each plot will be scaled independently.

In this exercise your job is to generate box plots for fuel efficiency (mpg) and weight from the automobiles data set. 
To do this in a single figure, you'll specify subplots=True inside .plot() to generate two separate plots.
"""
# Make a list of the column names to be plotted: cols
cols = ['weight','mpg']

# Generate the box plots
df[cols].plot(kind='box', subplots=True)

# Display the plot
plt.show()


"""
pandas hist, pdf and cdf

Pandas relies on the .hist() method to not only generate histograms, 
but also plots of probability density functions (PDFs) and cumulative density functions (CDFs).

In this exercise, you will work with a dataset consisting of restaurant bills that includes the amount customers tipped.

The original dataset is provided by the Seaborn package.
https://github.com/mwaskom/seaborn-data/blob/master/tips.csv

Your job is to plot a PDF and CDF for the fraction column of the tips dataset. 
This column contains information about what fraction of the total bill is comprised of the tip.

Remember, when plotting the PDF, you need to specify normed=True in your call to .hist(), 
and when plotting the CDF, you need to specify cumulative=True in addition to normed=True.
"""
# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plot the PDF
df.fraction.plot(ax=axes[0], kind='hist', bins=30, normed=True, range=(0,.3))
plt.show()

# Plot the CDF
df.fraction.plot(ax=axes[1], kind='hist', bins=30, normed=True, cumulative=True, range=(0,.3))
plt.show()










