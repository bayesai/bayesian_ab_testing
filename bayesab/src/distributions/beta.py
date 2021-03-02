from scipy.stats import beta


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