def compute_disparate_impact(df, protected_column, label_column, prediction_column):
    """
    Computes Disparate Impact = P(Y_hat=1 | unprivileged) / P(Y_hat=1 | privileged)
    Minimal example: privileged = first unique value, unprivileged = second
    """
    vals = df[protected_column].unique()
    if len(vals) < 2:
        raise ValueError("Protected column must have at least 2 groups")
    privileged, unprivileged = vals[0], vals[1]

    p_priv = df[df[protected_column] == privileged][prediction_column].mean()
    p_unpriv = df[df[protected_column] == unprivileged][prediction_column].mean()

    if p_priv == 0:
        return 0
    return p_unpriv / p_priv

