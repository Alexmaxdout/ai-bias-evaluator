def compute_equal_opportunity(df, protected_column, label_column, prediction_column):
    """
    Measures difference in true positive rates between groups.
    """
    vals = df[protected_column].unique()
    if len(vals) < 2:
        raise ValueError("Protected column must have at least 2 groups")
    privileged, unprivileged = vals[0], vals[1]

    def tpr(sub_df):
        tp = ((sub_df[label_column] == 1) & (sub_df[prediction_column] == 1)).sum()
        pos = (sub_df[label_column] == 1).sum()
        return tp / pos if pos > 0 else 0

    return abs(tpr(df[df[protected_column] == privileged]) - tpr(df[df[protected_column] == unprivileged]))
