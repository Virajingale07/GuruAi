GuruAi ⚡
An Advanced Agentic Data Analysis & Intelligence Platform

GuruAi is a modular AI system designed to perform autonomous data analysis, visualization, and reporting. Built using a modern stack of Streamlit, LangGraph, and Groq, it allows users to interact with datasets using natural language to uncover deep insights and generate professional reports.

🏗️ Architecture & Stack
Frontend: Streamlit (Python-based UI with custom CSS themes).

Orchestration: LangGraph (Stateful agent workflows with tool-calling capabilities).

LLM Engine: Groq (Llama 3.3 70B for logic, 8B for speed).

Database: Supabase (Cloud storage for authentication and chat history).

Tools:

Python Engine: Sandboxed execution of Pandas and Matplotlib.

Tavily Search: Real-time web information retrieval.

Insights Module: Built-in anomaly detection and forecasting.

🚀 Key Features
Autonomous Analysis: Upload CSV, Excel, or JSON files and ask questions like "Identify revenue outliers".

Smart Visualization: Automatically generates and renders Matplotlib/Seaborn charts within the chat.

Professional Reporting: Compiles the entire session history and generated charts into a downloadable PDF.

Multi-User Security: Secure login system using bcrypt hashing and Supabase storage.

Resilient Intelligence: Automatic API key rotation and model fallback (70B to 8B) to handle rate limits.

🛠️ Installation & Setup
1. Clone the Repository
Bash

git clone https://github.com/virajingale07/guruai.git
cd guruai
2. Install Dependencies
Bash

pip install -r requirements.txt
3. Configure Secrets
Create a .streamlit/secrets.toml file with your credentials:

Ini, TOML

[secrets]
GROQ_API_KEYS = "gsk_key1, gsk_key2"
TAVILY_API_KEYS = "tvly-key1"
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-anon-key"

4. Database Setup
Execute the following SQL in your Supabase SQL Editor to create the required tables:

5. Run the Application
Bash

streamlit run nexus_core.py
📁 Project Structure
nexus_core.py: Main entry point and Streamlit UI logic.

nexus_brain.py: LangGraph agent definition and LLM orchestration.

nexus_engine.py: Python execution environment for data processing.

nexus_db.py: Supabase connection and history management.

nexus_security.py: User authentication and password hashing.

nexus_report.py: PDF generation logic.

themes.py: Custom CSS and professional UI styling
