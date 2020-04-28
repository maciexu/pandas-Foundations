"""
Bachelor's degrees awarded to women

In this exercise, you will investigate statistics of the percentage of Bachelor's degrees awarded to women from 1970 to 2011. 
Data is recorded every year for 17 different fields. This data set was obtained from the Digest of Education Statistics.
https://nces.ed.gov/programs/digest/2013menu_tables.asp

Your job is to compute the minimum and maximum values of the 'Engineering' column and generate a line plot of 
the mean value of all 17 academic fields per year. 
To perform this step, you'll use the .mean() method with the keyword argument axis='columns'. 
This computes the mean across all columns per row.
"""
# Print the minimum value of the Engineering column
print(df.Engineering.min())

# Print the maximum value of the Engineering column
print(df.Engineering.max())

# Construct the mean percentage per year: mean
mean = df.mean(axis='columns')

# Plot the average percentage per year
mean.plot()


"""
Median vs mean

In many data sets, there can be large differences in the mean and median value due to the presence of outliers.

In this exercise, you'll investigate the mean, median, and max fare prices paid by passengers on the Titanic and generate a box plot of the fare prices. 
This data set was obtained from Vanderbilt University.
http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.html
"""
# Print summary statistics of the fare column with .describe()
print(df.fare.describe())

# Generate a box plot of the fare column
df.fare.plot(kind='box')

# Show the plot
plt.show()



"""
Quantiles

In this exercise, you'll investigate the probabilities of life expectancy in countries around the world. 
This dataset contains life expectancy for persons born each year from 1800 to 2015. 
Since country names change or results are not reported, not every country has values. 
This dataset was obtained from Gapminder.

First, you will determine the number of countries reported in 2015. 
There are a total of 260 unique countries in the entire dataset. 
Then, you will compute the 5th and 95th percentiles of life expectancy over the entire dataset. 
Finally, you will make a box plot of life expectancy every 50 years from 1800 to 2000. 
Notice the large change in the distributions over this period.
"""
# Print the number of countries reported in 2015
print(df['2015'].count())

# Print the 5th and 95th percentiles
print(df.quantile([0.05, 0.95]))

# Generate a box plot
years = ['1800','1850','1900','1950','2000']
df[years].plot(kind='box')
plt.show()


"""
Standard deviation of temperature

Let's use the mean and standard deviation to explore differences in temperature distributions in Pittsburgh in 2013. 
The data has been obtained from Weather Underground.
https://www.wunderground.com/history
"""
# Print the mean of the January and March data
print(january.mean(), march.mean())

# Print the standard deviation of the January and March data
print(january.std(), march.std())



#Filtering and counting
df[df['origin'] == 'US']
df[df['origin'] == 'Asia'].count()


"""
Separate and summarize

Let's use population filtering to determine how the automobiles in the US differ from the global average and standard deviation. 
How does the distribution of fuel efficiency (MPG) for the US differ from the global average and standard deviation?

In this exercise, you'll compute the means and standard deviations of all columns in the full automobile dataset. 
Next, you'll compute the same quantities for just the US population and subtract the global values from the US values.
"""
# Compute the global mean and global standard deviation: global_mean, global_std
global_mean = df.mean()
global_std = df.std()

# Filter the US population from the origin column: us
us = df[df['origin']=='US']

# Compute the US mean and US standard deviation: us_mean, us_std
us_mean = us.mean()
us_std = us.std()

# Print the differences
print(us_mean - global_mean)
print(us_std - global_std)


"""
Separate and plot

Population filtering can be used alongside plotting to quickly determine differences in distributions between the sub-populations. 
You'll work with the Titanic dataset.

There were three passenger classes on the Titanic, and passengers in each class paid a different fare price. 
In this exercise, you'll investigate the differences in these fare prices.

Your job is to use Boolean filtering and generate box plots of the fare prices for each of the three passenger classes. 
The fare prices are contained in the 'fare' column and passenger class information is contained in the 'pclass' column.
"""
# Display the box plots on 3 separate rows and 1 column
fig, axes = plt.subplots(nrows=3, ncols=1)

# Generate a box plot of the fare prices for the First passenger class
titanic.loc[titanic['pclass'] == 1].plot(ax=axes[0], y='fare', kind='box')

# Generate a box plot of the fare prices for the Second passenger class
titanic.loc[titanic['pclass'] == 2].plot(ax=axes[1], y='fare', kind='box')

# Generate a box plot of the fare prices for the Third passenger class
titanic.loc[titanic['pclass'] == 3].plot(ax=axes[2], y='fare', kind='box')

# Display the plot
plt.show()

