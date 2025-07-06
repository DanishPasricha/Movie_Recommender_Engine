# 🎬 Movie Recommender Agent

A simple, production-ready movie recommender agent using OpenAI, Tavily for real-time search, and Judgeval for tracing and evaluation.

---

## 🚀 Features

- **Conversational movie recommendations** using OpenAI GPT-4o
- **Real-time web search** with Tavily for up-to-date movie data
- **Judgeval integration** for tracing, monitoring, and evaluating agent responses
- **Faithfulness scoring** to ensure recommendations are grounded in retrieved context

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd movie_recommender_agent
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the project root and add your API keys:

```
OPENAI_API_KEY=your-openai-key
TAVILY_API_KEY=your-tavily-key
JUDGMENT_API_KEY=your-judgment-key
JUDGMENT_ORG_ID=your-judgment-org-id
```

---

## 💡 Usage

### Run the Agent

```bash
source venv/bin/activate  # If not already active
python agent.py
```

- The agent will prompt you for your favorite genre, actor, and a recent movie you liked.
- It will recommend 5 movies based on your preferences and real-time search.
- **Judgeval tracing**: After each run, you'll see a "View Trace" link in the output. Click it to view the trace and evaluation on the Judgeval platform.

---

### Run Automated Evaluation Tests

```bash
python test_agent.py
```

- This runs a faithfulness evaluation using Judgeval, comparing the agent's output to a mock retrieval context.
- Results and detailed scoring will be printed, and you can view them on the Judgeval dashboard.

---

## 🧑‍💻 How Judgeval Tracing & Evaluation Works

- **Tracing**: Every agent run is traced and can be inspected on the Judgeval platform for debugging and monitoring.
- **Evaluation**: The agent's recommendations are scored for faithfulness to the search results (retrieval context) using Judgeval's `FaithfulnessScorer`.
- **Dashboard**: Use the "View Trace" and "View Results" links in your terminal output to inspect traces and evaluation results.

---

## 📚 References

- [Judgeval Documentation](https://docs.judgmentlabs.ai/documentation)
- [Judgeval Example Agents](https://github.com/JudgmentLabs/judgment-cookbook)


