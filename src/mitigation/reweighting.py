def reweight(df, protected_column, label_column):
    """
    Adds a 'weight' column to reduce bias: simple example using inverse frequency.
    """
    total = len(df)
    counts = df.groupby([protected_column, label_column]).size()
    df = df.copy()
    df['weight'] = df.apply(lambda row: total / counts[row[protected_column], row[label_column]], axis=1)
    return df

