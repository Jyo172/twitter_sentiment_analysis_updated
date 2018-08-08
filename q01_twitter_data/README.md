## Enabling connection to twitter

In this assignment we will be creating a Utility function to setup the Twitter's API with our access keys provided  and get the desired dataframe.

## Write a function `q01_twitter_data` that :
- Authenticates and access the keys of twitter application using tweepy.
- Calls previous function and extracts the tweets of `NarendraModi` using tweepy's `user_timeline` method.
- Creates a Dataframe consisting of the following information(as features) extracted from the tweets
  - Lenght of the tweets.
  - ID of the tweets.
  - Date the tweet has been posted.
  - Source of the tweets.
  - Likes per tweet recorded.
  - No. of retweets on a particular tweet recorded.


### Parameters:

This function takes no parameters.

### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| data | pandas.core.frame.DataFrame | dataframe containg the following information mentioned above |



`Note` :For future tasks, store the returned dataframe as a csv file