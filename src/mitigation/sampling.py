def balance_sampling(df, protected_column, label_column):
    """
    Resamples dataset to have equal representation of protected groups.
    """
    groups = df.groupby([protected_column, label_column])
    min_count = groups.size().min()
    return groups.sample(n=min_count, replace=False).reset_index(drop=True)

