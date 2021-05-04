from scipy.stats import beta
import pandas as pd


class Beta:
    """
    Todo documentation

    """
    def __init__(self, a0, b0):
        self.a = a0
        self.b = b0

    def pdf(self, x):
        return beta.pdf(x, self.a, self.b)

    def gen_sample(self,size):
        return beta(self.a, self.b, size=size)

    def posterior_update(self, df:pd.Series):
        c = df.sum()
        n = len(df)

        self.a = self.a + c
        self.b = self.b + n - c

