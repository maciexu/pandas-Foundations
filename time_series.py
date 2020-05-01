"""
df1 = pd.read_csv(filename)

df2 = pd.read_csv(filename, parse_dates=['Date'])

df3 = pd.read_csv(filename, index_col='Date', parse_dates=True)
"""
"""
Creating and using a DatetimeIndex

The pandas Index is a powerful way to handle time series data, so it is valuable to know how to build one yourself. 
Pandas provides the pd.to_datetime() function for just this task. 
For example, if passed the list of strings ['2015-01-01 091234','2015-01-01 091234'] and a format specification variable, 
such as format='%Y-%m-%d %H%M%S, pandas will parse the string into the proper datetime elements and build the datetime objects.
"""
# Prepare a format string: time_format
time_format = '%Y-%m-%d %H:%M'

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(date_list, format=time_format)  

# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(temperature_list, index=my_datetimes)

# Partial string indexing and slicing
# Extract the hour from 9pm to 10pm on '2010-10-11': ts1
ts1 = ts0.loc['2010-10-11 21:00:00':'2010-10-11 22:00:00']

# Extract '2010-07-04' from ts0: ts2
ts2 = ts0.loc['2010-07-04']

# Extract data from '2010-12-15' to '2010-12-31': ts3
ts3 = ts0.loc['2010-12-15':'2010-12-31']

"""
Reindexing the Index

Reindexing is useful in preparation for adding or otherwise combining two time series data sets. 
To reindex the data, we provide a new index and ask pandas to try and match the old data to the new index. 
If data is unavailable for one of the new index dates or times, you must tell pandas how to fill it in. 
Otherwise, pandas will fill with NaN by default.

In this exercise, two time series data sets containing daily data have been pre-loaded for you, each indexed by dates. 
The first, ts1, includes weekends, but the second, ts2, does not. The goal is to combine the two data sets in a sensible way. 
Your job is to reindex the second data set so that it has weekends as well, and then add it to the first. 
"""

# Reindex without fill method: ts3
# Create a new time series ts3 by reindexing ts2 with the index of ts1. 
# To do this, call .reindex() on ts2 and pass in the index of ts1 (ts1.index).
ts3 = ts2.reindex(ts1.index)

# Reindex with fill method, using forward fill: ts4
# Create another new time series, ts4, by calling the same .reindex() as above, but also specifying a fill method, 
# using the keyword argument method="ffill" to forward-fill values.
ts4 = ts2.reindex(ts1.index, method = 'ffill')

# Combine ts1 + ts2: sum12
sum12 = ts1 + ts2

# Combine ts1 + ts3: sum13
sum13 = ts1 + ts3

# Combine ts1 + ts4: sum14
sum14 = ts1 + ts4


"""
Resampling and frequency

Pandas provides methods for resampling time series data. 
When downsampling or upsampling, the syntax is similar, but the methods called are different. 
Both use the concept of 'method chaining' - df.method1().method2().method3() - 
to direct the output from one method call to the input of the next, and so on, 
as a sequence of operations, one feeding into the next.

For example, if you have hourly data, and just need daily data, pandas will not guess how to throw out the 23 of 24 points. 
You must specify this in the method. One approach, for instance, could be to take the mean, as in df.resample('D').mean().
"""
# Downsample to 6 hour data and aggregate by mean: df1
df1 = df.loc[:, 'Temperature'].resample('6h').mean()

# Downsample to daily data and count the number of data points: df2
df2 = df.loc[:, 'Temperature'].resample('D').count()

# Extract temperature data for August: august
august = df.loc['2010-08', 'Temperature']

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()

# Extract temperature data for February: february
february = df.loc['2010-02', 'Temperature']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()


"""
Rolling mean and frequency

Rolling means (or moving averages) are generally used to smooth out short-term fluctuations in time series data and highlight long-term trends. 
You can read more about them here: https://en.wikipedia.org/wiki/Moving_average

To use the .rolling() method, you must always use method chaining, 
first calling .rolling() and then chaining an aggregation method after it. 
For example, with a Series hourly_data, hourly_data.rolling(window=24).mean() would compute new values for each hourly point, 
based on a 24-hour window stretching out behind each point. 
The frequency of the output data is the same: it is still hourly. Such an operation is useful for smoothing time series data.
"""
# Extract data from 2010-Aug-01 to 2010-Aug-15: unsmoothed
unsmoothed = df['Temperature']['2010-08-01':'2010-08-15']

# Apply a rolling mean with a 24 hour window: smoothed
smoothed = unsmoothed.rolling(window=24).mean()

# Create a new DataFrame with columns smoothed and unsmoothed: august
august = pd.DataFrame({'smoothed':smoothed, 'unsmoothed':unsmoothed})

# Plot both smoothed and unsmoothed data using august.plot().
august.plot()
plt.show()

# Extract the August 2010 data: august
august = df['Temperature']['2010-08']

# Resample to daily data, aggregating by max: daily_highs
daily_highs = august.resample('D').max()

# Use a rolling 7-day window with method chaining to smooth the daily high temperatures in August
daily_highs_smoothed = daily_highs.rolling(window=7).mean()
print(daily_highs_smoothed)


# Method chaining and filtering
# Strip extra whitespace from the column names: df.columns
df.columns = df.columns.str.strip()

# Extract data for which the destination airport is Dallas: dallas
dallas = df['Destination Airport'].str.contains('DAL')

# Compute the total number of Dallas departures each day: daily_departures
daily_departures = dallas.resample('D').sum()

# Generate the summary statistics for daily Dallas departures: stats
stats = daily_departures.describe()

# Reset the index of ts2 to ts1, and then use linear interpolation to fill in the NaNs: ts2_interp
# To reindex ts2 using the index of ts1, use the .reindex() method with ts1.index as the argument. 
# After this, you can chain the .interpolate() method with the keyword argument how='linear'.
ts2_interp = ts2.reindex(ts1.index).interpolate(how='linear')

# Compute the absolute difference of ts1 and ts2_interp: differences 
differences = np.abs(ts1- ts2_interp)

# Generate and print summary statistics of the differences
print(differences.describe())


"""
Time zones and conversion
Time zone handling with pandas typically assumes that you are handling the Index of the Series. 
In this exercise, you will learn how to handle timezones that are associated with datetimes in the column data, 
and not just the Index.

You will work with the flight departure dataset again, and this time you will select Los Angeles ('LAX') as the destination airport.

Here we will use a mask to ensure that we only compute on data we actually want. 
To learn more about Boolean masks, click here!
https://docs.scipy.org/doc/numpy/reference/maskedarray.generic.html
"""
# Build a Boolean mask to filter for the 'LAX' departure flights: mask
mask = df['Destination Airport'] == 'LAX'

# Use the mask to subset the data: la
la = df[mask]

# Combine two columns of data to create a datetime series: times_tz_none 
times_tz_none = pd.to_datetime( la['Date (MM/DD/YYYY)'] + ' ' + la['Wheels-off Time'])

# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')

# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')


# Plotting time series, datetime indexing
# Convert the 'Date' column into a collection of datetime objects: df.Date
df.Date = pd.to_datetime(df.Date)

# Set the index to be the converted 'Date' column
df.set_index('Date', inplace=True)

# Re-plot the DataFrame to see that the axis is now datetime aware!
df.plot()
plt.show()

"""
Plotting date ranges, partial indexing
how to extract one month of temperature data using 'May 2010' as a key into df.Temperature[], 
and call head() to inspect the result: 
df.Temperature['May 2010'].head()
"""
# Plot the summer data
df.Temperature['Jun 2010':'Aug 2010'].plot()
plt.show()
plt.clf()

# Plot the one week data
df.Temperature['2010-06-10':'2010-06-17'].plot()
plt.show()
plt.clf()

