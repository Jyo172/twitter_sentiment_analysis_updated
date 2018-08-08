
from unittest import TestCase
from ..build import q04_sources_piechart
from inspect import getfullargspec
import pandas

data=pandas.read_csv('data.csv')
q04_sources_piechart(data)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q04_sources_piechart).args
        self.assertEqual(len(arg),1 , "Expected argument(s) %d, Given %d" % (1, len(arg)))

