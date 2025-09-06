import pandas as pd
from metrics.disparate_impact import compute_disparate_impact
from metrics.demographic_parity import compute_demographic_parity
from metrics.equal_opportunity import compute_equal_opportunity

def main():
    print("=== AI Bias Evaluator ===")
    dataset_path = input("Enter dataset path (CSV): ")
    df = pd.read_csv(dataset_path)

    # Example: assume dataset has 'gender', 'label', 'prediction'
    protected_column = 'gender'
    label_column = 'label'
    prediction_column = 'prediction'

    di = compute_disparate_impact(df, protected_column, label_column, prediction_column)
    dp = compute_demographic_parity(df, protected_column, label_column, prediction_column)
    eo = compute_equal_opportunity(df, protected_column, label_column, prediction_column)

    print(f"Disparate Impact: {di:.2f}")
    print(f"Demographic Parity: {dp:.2f}")
    print(f"Equal Opportunity Difference: {eo:.2f}")

if __name__ == "__main__":
    main()

