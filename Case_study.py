# what if there's no header???->header=None
# Import pandas
import pandas as pd

# Read in the data file: df
df = pd.read_csv(data_file)

# Print the output of df.head()
print(df.head())

# Read in the data file with header=None: df_headers
df_headers = pd.read_csv(data_file, header=None)

# Print the output of df_headers.head()
print(df_headers.head())


# Re-assigning column names
# Split on the comma to create a list: column_labels_list
column_labels_list = column_labels.split(',')

# Assign the new column labels to the DataFrame: df.columns
df.columns = column_labels_list

# Remove the appropriate columns: df_dropped
df_dropped = df.drop(list_to_drop, axis='columns')

# Print the output of df_dropped.head()
print(df_dropped.head())

"""
Cleaning and tidying datetime data

In order to use the full power of pandas time series, you must construct a DatetimeIndex. 
To do so, it is necessary to clean and transform the date and time columns.

The DataFrame df_dropped you created in the last exercise is provided for you and pandas has been imported as pd.

Your job is to clean up the date and Time columns and combine them into a datetime collection to be used as the Index.
"""
# Convert the date column to string: df_dropped['date']
df_dropped['date'] = df_dropped['date'].astype(str)

# Pad leading zeros to the Time column: df_dropped['Time']
df_dropped['Time'] = df_dropped['Time'].apply(lambda x:'{:0>4}'.format(x))

# Concatenate the new date and Time columns: date_string
date_string = df_dropped['date'] + df_dropped['Time']

# Convert the date_string Series to datetime: date_times
date_times = pd.to_datetime(date_string, format='%Y%m%d%H%M')

# Set the index to be the new date_times container: df_clean
df_clean = df_dropped.set_index(date_times)

# Print the output of df_clean.head()
print(df_clean.head())


"""
Cleaning the numeric columns

The numeric columns contain missing values labeled as 'M'. 
In this exercise, your job is to transform these columns such that they contain only numeric values and interpret missing data as NaN.

The pandas function pd.to_numeric() is ideal for this purpose: It converts a Series of values to floating-point values. 
Furthermore, by specifying the keyword argument errors='coerce', you can force strings like 'M' to be interpreted as NaN.
"""
# Print the dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc['2011-06-20 08:00:00':'2011-06-20 09:00:00', 'dry_bulb_faren'])

# Convert the dry_bulb_faren column to numeric values: df_clean['dry_bulb_faren']
df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], errors='coerce')

# Print the transformed dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc['2011-06-20 08:00:00':'2011-06-20 09:00:00', 'dry_bulb_faren'])

# Convert the wind_speed and dew_point_faren columns to numeric values
df_clean['wind_speed'] = pd.to_numeric(df_clean['wind_speed'] , errors='coerce')
df_clean['dew_point_faren'] = pd.to_numeric(df_clean['dew_point_faren'], errors='coerce')


# EDA
# Print the median of the dry_bulb_faren column
print(df_clean['dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the time range '2011-Apr':'2011-Jun'
print(df_clean.loc['2011-Apr':'2011-Jun', 'dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the month of January
print(df_clean.loc['2011-Jan', 'dry_bulb_faren'].median())


"""
Signal variance

You're now ready to compare the 2011 weather data with the 30-year normals reported in 2010. 
You can ask questions such as, on average, how much hotter was every day in 2011 than expected from the 30-year average?

The DataFrames df_clean and df_climate from previous exercises are available in the workspace.

Your job is to first resample df_clean and df_climate by day and aggregate the mean temperatures. 
You will then extract the temperature related columns from each - 'dry_bulb_faren' in df_clean, 
and 'Temperature' in df_climate - as NumPy arrays and compute the difference.

Notice that the indexes of df_clean and df_climate are not aligned - df_clean has dates in 2011, 
while df_climate has dates in 2010. This is why you extract the temperature columns as NumPy arrays. 
An alternative approach is to use the pandas .reset_index() method to make sure the Series align properly. 
You will practice this approach as well.
"""
# Downsample df_clean by day and aggregate by mean: daily_mean_2011
daily_mean_2011 = df_clean.resample('D').mean()

# Extract the dry_bulb_faren column from daily_mean_2011 using .values: daily_temp_2011
# Extract the 'dry_bulb_faren' column from daily_mean_2011 as a NumPy array using .values. 
# Store the result as daily_temp_2011. Note: .values is an attribute, not a method, so you don't have to use ().
daily_temp_2011 = daily_mean_2011['dry_bulb_faren'].values

# Downsample df_climate by day and aggregate by mean: daily_climate
daily_climate = df_climate.resample('D').mean()

# Extract the Temperature column from daily_climate using .reset_index(): daily_temp_climate
# Be sure you call reset_index() on daily_climate and then access the 'Temperature' column using bracket indexing.
daily_temp_climate = daily_climate.reset_index()['Temperature']

# Compute the difference between the two arrays and print the mean difference
difference = daily_temp_2011 - daily_temp_climate
print(difference.mean())



"""
Sunny or cloudy
On average, how much hotter is it when the sun is shining? 
In this exercise, you will compare temperatures on sunny days against temperatures on overcast days.

Your job is to use Boolean selection to filter for sunny and overcast days, 
and then compute the difference of the mean daily maximum temperatures between each type of day.

The DataFrame df_clean from previous exercises has been provided for you. 
The column 'sky_condition' provides information about whether the day was sunny ('CLR') or overcast ('OVC').
"""

# Using df_clean, when is sky_condition 'CLR'?
is_sky_clear = df_clean['sky_condition']=='CLR'

# Filter df_clean using is_sky_clear
sunny = df_clean.loc[is_sky_clear]

# Resample sunny by day then calculate the max
sunny_daily_max = sunny.resample('D').max()

# See the result
sunny_daily_max.head()


# Using df_clean, when does sky_condition contain 'OVC'?
is_sky_overcast = df_clean['sky_condition'].str.contains('OVC')

# Filter df_clean using is_sky_overcast
overcast = df_clean.loc[is_sky_overcast]

# Resample overcast by day then calculate the max
overcast_daily_max = overcast.resample('D').max()

# See the result
overcast_daily_max.head()


# From previous steps
is_sky_clear = df_clean['sky_condition']=='CLR'
sunny = df_clean.loc[is_sky_clear]
sunny_daily_max = sunny.resample('D').max()
is_sky_overcast = df_clean['sky_condition'].str.contains('OVC')
overcast = df_clean.loc[is_sky_overcast]
overcast_daily_max = overcast.resample('D').max()

# Calculate the mean of sunny_daily_max
sunny_daily_max_mean = sunny_daily_max.mean()

# Calculate the mean of overcast_daily_max
overcast_daily_max_mean = overcast_daily_max.mean()

# Print the difference (sunny minus overcast)
print(sunny_daily_max_mean-overcast_daily_max_mean)


"""
Weekly average temperature and visibility

Is there a correlation between temperature and visibility? Let's find out.

In this exercise, your job is to plot the weekly average temperature and visibility as subplots. 
To do this, you need to first select the appropriate columns and then resample by week, aggregating the mean.

In addition to creating the subplots, you will compute the Pearson correlation coefficient using .corr(). 
The Pearson correlation coefficient, known also as Pearson's r, ranges from -1 (indicating total negative linear correlation) 
to 1 (indicating total positive linear correlation). 
A value close to 1 here would indicate that there is a strong correlation between temperature and visibility.
"""

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Select the visibility and dry_bulb_faren columns and resample them: weekly_mean
# Remember that to select multiple columns with the indexing operator, you need to pass a list (e.g. df_clean[['item 1', 'item 2']]
weekly_mean = df_clean[['visibility','dry_bulb_faren']].resample('W').mean()

# Print the output of weekly_mean.corr()
print(weekly_mean.corr())

# Plot weekly_mean with subplots=True
weekly_mean.plot(subplots=True)
plt.show()


# Daily hours of clear sky
# Using df_clean, when is sky_condition 'CLR'?
is_sky_clear = df_clean['sky_condition']=='CLR'

# Resample is_sky_clear by day
resampled = is_sky_clear.resample('D').sum()

# See the result
print(resampled)

# From previous step
is_sky_clear = df_clean['sky_condition'] == 'CLR'
resampled = is_sky_clear.resample('D')

# Calculate the number of sunny hours per day
sunny_hours = resampled.sum()

# Calculate the number of measured hours per day
total_hours = resampled.count()

# Calculate the fraction of hours per day that were sunny
sunny_fraction = sunny_hours / total_hours


# From previous steps
is_sky_clear = df_clean['sky_condition'] == 'CLR'
resampled = is_sky_clear.resample('D')
sunny_hours = resampled.sum()
total_hours = resampled.count()
sunny_fraction = sunny_hours / total_hours

# Make a box plot of sunny_fraction
sunny_fraction.plot(kind='box')
plt.show()


"""
Heat or humidity

Dew point is a measure of relative humidity based on pressure and temperature. 
A dew point above 65 is considered uncomfortable while a temperature above 90 is also considered uncomfortable.

In this exercise, you will explore the maximum temperature and dew point of each month. 
The columns of interest are 'dew_point_faren' and 'dry_bulb_faren'. 
After resampling them appropriately to get the maximum temperature and dew point in each month, 
generate a histogram of these values as subplots.
"""

# Resample dew_point_faren and dry_bulb_faren by Month, aggregating the maximum values: monthly_max
monthly_max = df_clean[['dew_point_faren', 'dry_bulb_faren']].resample('M').max()

# Generate a histogram with bins=8, alpha=0.5, subplots=True
monthly_max.plot(kind='hist', bins=8, alpha=0.5, subplots=True)

# Show the plot
plt.show()


"""
Probability of high temperatures

We already know that 2011 was hotter than the climate normals for the previous thirty years. 
In this final exercise, you will compare the maximum temperature in August 2011 against that of the August 2010 climate normals. 
More specifically, you will use a CDF plot to determine the probability of the 2011 daily maximum temperature in August 
being above the 2010 climate normal value. T
o do this, you will leverage the data manipulation, filtering, resampling, and visualization skills you have acquired throughout this course.

The two DataFrames df_clean and df_climate are available in the workspace. 
Your job is to select the maximum temperature in August in df_climate, and then maximum daily temperatures in August 2011. 
You will then filter to keep only the days in August 2011 that were above the August 2010 maximum, 
and use this to construct a CDF plot.

Once you've generated the CDF, notice how it shows that there was a 
50% probability of the 2011 daily maximum temperature in August being 5 degrees above the 2010 climate normal value!
"""

# Extract the maximum temperature in August 2010 from df_climate: august_max
# You can select the rows corresponding to August 2010 in multiple ways. For example, df_climate.loc['2011-Feb'] selects all rows corresponding to February 2011, while df_climate.loc['2009-09', 'Pressure'] selects the rows corresponding to September 2009 from the 'Pressure' column.
august_max = df_climate.loc['2010-Aug','Temperature'].max()
print(august_max)

# Resample August 2011 temps in df_clean by day & aggregate the max value: august_2011
august_2011 = df_clean.loc['2011-Aug','dry_bulb_faren'].resample('D').max()

# Filter for days in august_2011 where the value exceeds august_max: august_2011_high
august_2011_high = august_2011.loc[august_2011 > august_max]

# Construct a CDF of august_2011_high
august_2011_high.plot(kind='hist', normed=True, cumulative=True, bins=25)

# Display the plot
plt.show()


