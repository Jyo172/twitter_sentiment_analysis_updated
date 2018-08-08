from unittest import TestCase
from ..build import q05_analyze_sentiment
from inspect import getfullargspec
import pandas
import numpy as np

data=pandas.read_csv('data.csv')
data['SA'] = np.array([q05_analyze_sentiment(tweet) for tweet in data['Tweets']])

class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q05_analyze_sentiment).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_instance(self):
        self.assertIsInstance(data, pandas.core.frame.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_return_shape(self):
        self.assertEqual(data.shape, (200, 8), "The Expected return shape does not match with the given return shape")
