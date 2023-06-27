import numpy as np

class Toolbox:
    def __init__(self, name=None):
        self.name = name

    def mean(self, data):
        '''
        Calculate mean of a data series
        '''
        self._mean = np.mean(data)

    def std(self, data):
        '''
        Calculate sample standard deviation of a data series
        '''
        self._std = np.std(data, ddof = 1)

    def median(self, data):
        '''
        Calculate median of a data series
        '''
        self._median = np.median(data)

    def quantile(self, data, n):
        '''
        Calculate quantile n of a data series,
        e.g. n = 4 calculates quartile, n = 5 calculates quintile etc.
        '''
        if not hasattr(self, "_quantile"):
            self._quantile = {}
        self._quantile[n] = np.quantile(data, q = 1 / n)

    def percentile(self, data, n):
        '''
        Calculate percentile of n percent of a data series,
        e.g. n = 25 calculates quartile, n = 75 calculates three quartiles etc.
        '''
        if not hasattr(self, "_percentile"):
            self._percentile = {}
        self._percentile[n] = np.percentile(data, q = n)

    def iqr(self, data):
        '''
        Calculates interquartile range of a data series
        (difference between percentile of 75 percent and percentile of 25 percent)
        '''
        try:
            self._iqr = self._percentile[75] - self._percentile[25]
        except(AttributeError, KeyError):
            self.percentile(data, n = 25)
            self.percentile(data, n = 75)
            self.iqr(data)
