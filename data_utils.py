import pandas as pd

def dataset_overview(df):
    total_rows, total_cols = df.shape
    summary = f"Dataset Overview:\n- Total Rows: {total_rows}\n- Total Columns: {total_cols}\n\n"
    summary += "Columns and Data Types:\n"
    summary += "\n".join([f"- {col}: {dtype}" for col, dtype in df.dtypes.items()]) + "\n\n"

    missing_summary = "Missing Values Per Column:\n"
    for col in df.columns:
        missing_count = df[col].isnull().sum()
        missing_pct = (missing_count / total_rows) * 100
        missing_summary += f"- {col}: {missing_count} ({missing_pct:.2f}%)\n"

    return summary + missing_summary

def numeric_stats(df):
    insight_texts = []
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        series = df[col]
        count = series.count()
        min_val, max_val = series.min(), series.max()
        mean_val = series.mean()
        median_val = series.median()
        std_val = series.std()

        summary = f"Numeric Column: {col}\n"
        summary += f"- Count: {count}\n- Min: {min_val}\n- Max: {max_val}\n"
        summary += f"- Mean: {mean_val:.2f}\n- Median: {median_val}\n- Std Dev: {std_val:.2f}\n"
        insight_texts.append(summary)

    return insight_texts

def categorical_stats(df):
    insight_texts = []
    categorical_cols = df.select_dtypes(include='object').columns
    for col in categorical_cols:
        series = df[col]
        unique_vals = series.nunique()
        mode = series.mode().iloc[0] if not series.mode().empty else "N/A"
        value_counts = series.value_counts().head(5)

        summary = f"Categorical Column: {col}\n"
        summary += f"- Unique Categories: {unique_vals}\n- Mode: {mode}\n- Top 5 Values:\n"
        for val, count in value_counts.items():
            pct = (count / len(series)) * 100
            summary += f"  - {val}: {count} ({pct:.2f}%)\n"

        insight_texts.append(summary)
    return insight_texts

def correlation_summary(df):
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 1:
        corr = df[numeric_cols].corr()
        corr_values = corr.where(~(corr == 1)).stack()
        if not corr_values.empty:
            max_pair = corr_values.idxmax()
            min_pair = corr_values.idxmin()

            summary = "Correlation Summary:\n"
            summary += f"- Most Positively Correlated Pair: {max_pair} ({corr_values[max_pair]:.2f})\n"
            summary += f"- Most Negatively Correlated Pair: {min_pair} ({corr_values[min_pair]:.2f})\n"
            return summary
    return ""
