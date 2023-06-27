import pytest
import analyzer.toolbox as toolbox

test_toolbox = toolbox.Toolbox('test')
test_data = [0, 1, 2, 3, 4, 4.2, 1.1, 3.2, 9.7, 5.5, 14.7, 15.8]

def test_mean():
    test_toolbox.mean(test_data)
    assert(test_toolbox._mean == pytest.approx(5.35))

def test_std():
    test_toolbox.std(test_data)
    assert(round(test_toolbox._std,4) == pytest.approx(5.2716))

def test_median():
    test_toolbox.median(test_data)
    assert(test_toolbox._median == pytest.approx(3.6))

def test_quantile_nothasattr():
    if hasattr(test_toolbox, "_quantile"):
        del test_toolbox._quantile

    n = 4

    test_toolbox.quantile(test_data, n)
    assert(test_toolbox._quantile[n] == pytest.approx(1.775))
    del test_toolbox._quantile

    n = 5

    test_toolbox.quantile(test_data, n)
    assert(test_toolbox._quantile[n] == pytest.approx(1.28))


def test_quantile_hasattr():
    if not hasattr(test_toolbox, "_quantile"):
        test_toolbox._quantile = {}

    n = 5

    test_toolbox.quantile(test_data, n)
    assert (test_toolbox._quantile[n] == pytest.approx(1.28))

    n = 4

    test_toolbox.quantile(test_data, n)
    assert (test_toolbox._quantile[n] == pytest.approx(1.775))

def test_percentile_nothasattr():
    if hasattr(test_toolbox, "_percentile"):
        del test_toolbox._percentile

    n = 5

    test_toolbox.percentile(test_data, n)
    assert (test_toolbox._percentile[n] == pytest.approx(0.55))

    n = 4

    test_toolbox.percentile(test_data, n)
    assert (test_toolbox._percentile[n] == pytest.approx(0.44))

def test_percentile_hasattr():
    if not hasattr(test_toolbox, "_percentile"):
        test_toolbox._percentile = {}

    n = 5

    test_toolbox.percentile(test_data, n)
    assert (test_toolbox._percentile[n] == pytest.approx(0.55))

    n = 4

    test_toolbox.percentile(test_data, n)
    assert (test_toolbox._percentile[n] == pytest.approx(0.44))

def test_iqr_nothasattr_haskey():
    if hasattr(test_toolbox, "_iqr"):
        del test_toolbox._iqr

    test_toolbox.percentile(test_data, n=75)
    test_toolbox.percentile(test_data, n=25)

    test_toolbox.iqr(test_data)
    assert (test_toolbox._iqr == pytest.approx(4.775))

def test_iqr_nothaskey():
    if hasattr(test_toolbox, "_percentile"):
        del test_toolbox._percentile

    test_toolbox.iqr(test_data)
    assert (test_toolbox._iqr == pytest.approx(4.775))
