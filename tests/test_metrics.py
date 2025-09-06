import pandas as pd
import pytest
from metrics.disparate_impact import compute_disparate_impact
from metrics.demographic_parity import compute_demographic_parity
from metrics.equal_opportunity import compute_equal_opportunity

# Sample dataset
data = {
    'gender': ['M', 'F', 'M', 'F'],
    'label': [1, 1, 0, 0],
    'prediction': [1, 0, 0, 1]
}
df = pd.DataFrame(data)

def test_disparate_impact():
    di = compute_disparate_impact(df, 'gender', 'label', 'prediction')
    assert di >= 0  # Basic sanity check

def test_demographic_parity():
    dp = compute_demographic_parity(df, 'gender', 'label', 'prediction')
    assert dp >= 0

def test_equal_opportunity():
    eo = compute_equal_opportunity(df, 'gender', 'label', 'prediction')
    assert eo >= 0

