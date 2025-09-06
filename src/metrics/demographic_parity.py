def compute_demographic_parity(df, protected_column, label_column, prediction_column):
    """
    Returns the difference in positive prediction rates between groups.
    """
    vals = df[protected_column].unique()
    if len(vals) < 2:
        raise ValueError("Protected column must have at least 2 groups")
    privileged, unprivileged = vals[0], vals[1]

    p_priv = df[df[protected_column] == privileged][prediction_column].mean()
    p_unpriv = df[df[protected_column] == unprivileged][prediction_column].mean()

    return abs(p_priv - p_unpriv)

