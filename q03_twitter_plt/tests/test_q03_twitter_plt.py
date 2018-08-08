from unittest import TestCase
from ..build import q03_twitter_plt, q02_tweet_info
from inspect import getfullargspec
import pandas as pd

twitter_data=pd.read_csv('data.csv')      
tweet_len, tweet_fav, tweet_retweet = q02_tweet_info(twitter_data) 


q03_twitter_plt(tweet_len, tweet_fav, tweet_retweet)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q03_twitter_plt).args
        self.assertEqual(len(arg), 3, "Expected argument(s) %d, Given %d" % (3, len(arg)))

