import pytest
from bayesab import distributions


@pytest.fixture
def beta():
    return distributions.Beta(1, 1)


def test_beta_pdf(beta):
    actual = beta.pdf(0.5)
    expected = 1
    assert actual == expected



