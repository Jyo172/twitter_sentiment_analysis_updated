## Reorganizing

This assignment is all about reorganizing the data in the form of time series which can give us meaningful visualizations.


## Write a function `q02_tweet_info` that :
- Loads previously saved csv file into a dataframe
- Converts features such as `Likes`, `len`, `RTs` into time series.


### Parameters:

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable  |pandas.DataFrame| compulsory    |               | Dataframe to be loaded        |

### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| variable1 | pandas.core.series.Series | Pandas Series contaning len of each tweet|
| variable2 | pandas.core.series.Series | Pandas Series contaning likes of each tweet|
| variable3 | pandas.core.series.Series | Pandas Series contaning retweets on each tweet|
