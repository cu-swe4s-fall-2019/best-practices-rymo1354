import unittest
from get_column_stats import column_mean
from get_column_stats import column_stdev
import random
import os
import numpy as np


class TestMean(unittest.TestCase):

    def generate_file(self):
        self.number = 1000
        self.empty = []
        self.values = np.random.randint(0, 1000, size=self.number)
        self.test_file = 'data_file.txt'
        self.mean = np.mean(self.values)
        self.std = np.std(self.values)

    def setUp(self):
        self.generate_file()

    def test_mean(self):
        for i in range(1000):
            self.generate_file()
            self.assertEqual(column_mean(self.values), round(self.mean, 3))

    def test_std(self):
        for i in range(1000):
            self.generate_file()
            self.assertAlmostEqual(column_stdev(self.values, self.mean),
                                   self.std, 3)

    def test_mean_exception(self):
        self.assertRaises(ZeroDivisionError and
                          SystemExit, column_mean, self.empty)

    def test_std_exception(self):
        self.assertRaises(ZeroDivisionError and
                          SystemExit, column_stdev, self.empty, self.values)


if __name__ == '__main__':
    unittest.main()
