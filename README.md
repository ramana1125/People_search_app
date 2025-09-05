People Search App
Project Overview 🔍
The People Search App is a web-based tool that leverages a Retrieval-Augmented Generation (RAG) pipeline to perform intelligent, natural language-based searches for user profiles. It goes beyond keyword matching by using a Vector Database to find profiles semantically similar to a user's query and a Large Language Model (LLM) to generate detailed insights, compatibility percentages, and actionable feedback for each result.

The application allows users to find people based on shared interests, location, and values, making it ideal for connecting with like-minded individuals.

Key Features ✨
Natural Language Search: Find profiles using descriptive, human-like queries (e.g., "Find people in NYC interested in AI and tennis").

Intelligent Matching: The RAG pipeline ensures results are highly relevant and context-aware.

Compatibility Scoring: Each result includes a compatibility percentage and detailed insights explaining the match.

Scalable Architecture: The project is built with a modular structure, making it easy to add new features or integrate different models.

Project Structure 📁
PEOPLE-SEARCH-APP/
├── app/
│   ├── ui/
│   │   ├── streamlit.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── db_handler.py
│   ├── llm_handler.py
│   ├── main.py
│   └── rag_pipeline.py
├── data/
│   └── sample_profiles.json
├── .env
├── requirements.txt
└── README.md
app/: Contains the core logic of the application.

ui/: Holds the user interface code. streamlit.py is the main script for the web app.

db_handler.py: Handles interactions with the vector database.

llm_handler.py: Manages all calls to the Google Gemini LLM.

rag_pipeline.py: Orchestrates the retrieval and generation steps.

main.py: A command-line interface (CLI) for running searches without the web UI.

data/: Stores the raw user profile data in a JSON file.

.env: Used to store your Google API key securely.

requirements.txt: Lists all necessary Python dependencies.

Setup Instructions ⚙️
Follow these steps to set up and run the project locally.

1. Clone the repository
First, clone the project from your version control system or download the source code.

Bash

git clone <your_repo_url>
cd people-search-app
2. Create and activate a virtual environment
It is highly recommended to use a virtual environment to manage project dependencies.

Bash

# For Windows
python -m venv .venv
.venv\Scripts\activate

# For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
Install all required libraries using the requirements.txt file.

Bash

pip install -r requirements.txt
4. Configure your API key
The project uses the Google Gemini API. You need to obtain an API key from Google AI Studio.

Go to Google AI Studio.

Create a new API key.

In your project's root directory, create a file named .env.

Add your API key to this file in the following format:

Code snippet

GOOGLE_API_KEY="YOUR_API_KEY_HERE"
5. Add an __init__.py file (Important!)
If your ui folder does not contain an __init__.py file, you must create one to ensure Python recognizes it as a package.

touch app/ui/__init__.py
How to Run the App ▶️
You can run the application using either the Streamlit web interface or the command-line interface.

Run the Web App
Navigate to the project's root directory and run the following command.

Bash

python -m streamlit run app/ui/streamlit.py
This will launch the app in your browser, where you can enter natural language queries and see the results.
