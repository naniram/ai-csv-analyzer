import streamlit as st
import pandas as pd
import tempfile

from data_utils import dataset_overview, numeric_stats, categorical_stats, correlation_summary
from ai_utils import create_documents, create_vector_db, setup_qa_chain

# Page Config
st.set_page_config(page_title="📊 AI CSV Insight Explorer", layout="centered")

st.title("📊 AI CSV Insight Explorer")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        csv_path = tmp_file.name

    df = pd.read_csv(csv_path)
    st.success(f"✅ CSV Loaded: {df.shape[0]} rows × {df.shape[1]} columns")

    # Show top 5 rows
    st.subheader("🔍 Top 5 Rows of the Dataset")
    st.dataframe(df.head())

    # Generate insights
    with st.spinner("Generating insights..."):
        insights = []
        insights.append(dataset_overview(df))
        insights.extend(numeric_stats(df))
        insights.extend(categorical_stats(df))
        corr_summary = correlation_summary(df)
        if corr_summary:
            insights.append(corr_summary)

        full_summary_text = "\n\n".join(insights)
        insights.append(f"Full Dataset Summary:\n\n{full_summary_text}")

        documents = create_documents(insights)
        db = create_vector_db(documents, "deepseek-r1:1.5b")
        qa_chain = setup_qa_chain(db, "deepseek-r1:1.5b")

    # Show insights in expander
    with st.expander("📖 Insights Summary"):
        for text in insights:
            st.text(text)

    st.success("✅ AI Assistant Ready — Ask your questions!")

    # Query input
    query = st.text_input("💬 Ask a question about your dataset:")

    if query:
        if query.lower() in ["all insights", "summary", "show summary", "dataset overview"]:
            st.markdown(f"**📝 Full Dataset Summary:**\n\n```text\n{full_summary_text}\n```")
        else:
            with st.spinner("Thinking..."):
                answer = qa_chain.run(query)
            st.markdown(f"**🤖 Assistant:**\n\n{answer}")

else:
    st.info("👆 Upload a CSV file to start.")

