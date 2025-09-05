# 👥 ProfileFinder 🔍

A smart **People Search Application** powered by **RAG (Retrieval-Augmented Generation)** 🧠 and **Google Gemini AI** ✨.
This tool allows you to search for profiles using **natural language queries** instead of plain keyword matching.

It combines:

* 📚 **Vector Search (ChromaDB + Sentence Transformers)** for semantic similarity
* 🤖 **LLM (Gemini API)** for compatibility scoring & insights
* 🖥️ **CLI Interface** to interact with results

---

## 🚀 Features

* 🔍 Semantic profile search with embeddings
* 🤝 Compatibility insights & percentage match
* 📊 Ranking of top results
* ⚡ Simple CLI interface

---

## 📂 Project Structure

```
.
├── app/
│   ├── db_handler.py     # Handles ChromaDB, embeddings & search
│   ├── llm_handler.py    # Generates insights using Gemini LLM
│   ├── rag_pipeline.py   # RAG pipeline to combine search + insights
│   └── main.py           # CLI entry point
├── data/
│   └── sample_profiles.json   # Sample profiles data
└── README.md
```

---

## 🛠️ Installation

1. **Clone repo**

   ```bash
   git clone https://github.com/your-username/people-search-app.git
   cd people-search-app
   ```

2. **Create virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Linux/Mac
   .venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root:

   ```ini
   GOOGLE_API_KEY=your_google_api_key_here
   ```

---

## ▶️ Usage

###  Run Commands

To launch the **Streamlit UI**:

```bash
python -m streamlit run app/ui/streamlit.py
```

Or to use the **CLI version** directly:

```bash
python -m app.main --query "AI enthusiast from New York" --top_k 3
```

✅ Example Output:

```
🔍 Running search...

📌 Top Results:

Result 1:
Name: Alice Johnson
Location: New York
Interests: AI, Data Science, Startups
Bio: Passionate about building AI tools for social good
Compatibility: 85%
Insights: Strong alignment with query in terms of AI and location.
```

---

## ⚙️ Tech Stack

* 🐍 Python 3.9+
* 💾 [ChromaDB](https://docs.trychroma.com/) (vector database)
* 🔤 [Sentence Transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`)
* 🤖 [Google Gemini API](https://ai.google.dev/)
* 🛠️ CLI (argparse)

---

## 🌟 Future Improvements

* 🌐 Web UI with Streamlit or FastAPI
* 🔒 Authentication & user management
* 📈 More advanced ranking (multi-criteria search)

---

## 📜 License

MIT License © 2025
