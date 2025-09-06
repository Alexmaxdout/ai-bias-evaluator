import streamlit as st
import pandas as pd
from metrics.disparate_impact import compute_disparate_impact

st.title("⚖️ AI Bias Evaluator Dashboard")

uploaded_file = st.file_uploader("Upload CSV dataset", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset preview:")
    st.dataframe(df.head())

    protected_column = st.text_input("Protected column (e.g., gender)")
    label_column = st.text_input("Label column (e.g., outcome)")
    prediction_column = st.text_input("Prediction column (e.g., model_pred)")

    if st.button("Evaluate Bias") and protected_column and label_column and prediction_column:
        di = compute_disparate_impact(df, protected_column, label_column, prediction_column)
        st.metric("Disparate Impact", f"{di:.2f}")

