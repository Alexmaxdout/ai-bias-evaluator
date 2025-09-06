import pandas as pd
from mitigation.reweighting import reweight
from mitigation.sampling import balance_sampling

# Sample dataset
data = {
    'gender': ['M', 'F', 'M', 'F'],
    'label': [1, 1, 0, 0],
    'prediction': [1, 0, 0, 1]
}
df = pd.DataFrame(data)

def test_reweight():
    df_weighted = reweight(df, 'gender', 'label')
    assert 'weight' in df_weighted.columns
    assert all(df_weighted['weight'] > 0)

def test_balance_sampling():
    df_sampled = balance_sampling(df, 'gender', 'label')
    # After balancing, each group-label combo should have equal counts
    counts = df_sampled.groupby(['gender', 'label']).size()
    assert counts.nunique() == 1

