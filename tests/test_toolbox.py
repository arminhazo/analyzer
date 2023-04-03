import pytest
import analyzer.toolbox as toolbox

test_toolbox = toolbox.Toolbox('test')
test_data = [0, 1, 2, 3, 4, 4.2, 1.1, 3.2, 9.7, 5.5, 14.7, 15.8]

def test_mean():
    test_toolbox.mean(test_data)
    assert(test_toolbox.mean == pytest.approx(5.35))

def test_std():
    test_toolbox.std(test_data)
    assert(round(test_toolbox.std,4) == pytest.approx(5.2716))

def test_median():
    test_toolbox.median(test_data)
    assert(test_toolbox.median == pytest.approx(3.6))

def test_quantile_nothasattr():
    pass

def test_quantile_hasattr():
    pass

def test_percentile_nothasattr():
    pass

def test_percentile_hasattr():
    pass

def test_iqr_nothasattr():
    pass

def test_iqr_nothaskey():
    pass

def test_iqr_haskey():
    pass
