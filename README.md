# CSV Insight AI 📊

An **end-to-end AI-powered CSV Data Insight Explorer** built with **Streamlit**, **LangChain**, **FAISS**, and a local **DeepSeek R1:1.5B** LLM.

Upload a CSV file, automatically generate data summaries, and interactively ask natural language questions about your data — all processed locally, with no cloud required.

---

## Features

- Upload any CSV file
- View the top 5 rows of your dataset
- Automatically generate insights:
  - Dataset overview
  - Descriptive stats for numeric columns
  - Top categories for categorical columns
  - Correlations between numeric columns
  - Missing value analysis
- Ask questions about your data using a local LLM
- Fully offline, private, and local processing
- Clean, simple Streamlit interface

---

## Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Ollama](https://ollama.ai/)
- [Pandas](https://pandas.pydata.org/)

---

## How to Run Locally

### Install Dependencies

```bash
pip install -r requirements.txt
````

### Start the Streamlit App

```bash
streamlit run app.py
```

---

## Project Structure

```
csv-insight-ai/
├── app.py
├── data_utils.py
├── ai_utils.py
├── requirements.txt
├── README.md
└── sample.csv
```

---

## License

MIT License. See `LICENSE` file for details.

---

## Credits

Built using open-source AI tools, powered by DeepSeek R1:1.5B via [Ollama](https://ollama.ai/).

---

## Star this repo ⭐ if you find it helpful!
