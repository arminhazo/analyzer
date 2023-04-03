import numpy as np

class Toolbox:
    def __init__(self, name=None):
        self.name = name

    def mean(self, data):
        '''
        Calculate mean of a data series
        '''
        self.mean = np.mean(data)

    def std(self, data):
        '''
        Calculate sample standard deviation of a data series
        '''
        self.std = np.std(data, ddof = 1)

    def median(self, data):
        '''
        Calculate median of a data series
        '''
        self.median = np.median(data)

    def quantile(self, data, n):
        '''
        Calculate quantile n of a data series,
        e.g. n = 4 calculates quartile, n = 5 calculates quintile etc.
        '''
        if not hasattr(self, "quantile"):
            self.quantile = {}
        self.quantile[n] = np.quantile(data, q = 100 / n)

    def percentile(self, data, n):
        '''
        Calculate percentile of n percent of a data series,
        e.g. n = 25 calculates quartile, n = 75 calculates three quartiles etc.
        '''
        if not hasattr(self, "percentile"):
            self.percentile = {}
        self.percentile[n] = np.percentile(data, q = n)

    def iqr(self, data):
        '''
        Calculates interquartile range of a data series
        (difference between percentile of 75 percent and percentile of 25 percent)
        '''
        try:
            self.iqr = self.percentile[75] - self.percentile[25]
        except(AttributeError, KeyError):
            self.percentile(self, data, n = 25)
            self.percentile(self, data, n = 75)
            self.iqr(self, data)
