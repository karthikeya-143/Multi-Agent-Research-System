# Multi-Agent-Research-System

A simple multi-agent research system for orchestrating research tasks using modular agents, pipelines, and tools.

## Setup

```bash
conda create -n langagent python=3.11 -y
conda activate langagent
pip install -r requirements.txt
```

Create a `.env` file and add your API keys, for example:

```env
TAVILY_API_KEY=your_tavily_api_key
GOOGLE_API_KEY=your_google_api_key
```

## Working Flow

This project follows a step-by-step research pipeline:

1. User provides a topic.
2. The search agent uses the web search tool to gather recent and relevant information.
3. The reader agent picks the most relevant URL from the search results and scrapes its content for deeper context.
4. The writer chain transforms the gathered research into a structured report with:
   - Introduction
   - Key Findings
   - Conclusion
   - Sources
5. The critic chain reviews the generated report, scores it, and gives improvement feedback.
6. The pipeline returns the final research output along with the critic feedback.

## How the Project Is Organized

- `app.py` - Streamlit-based user interface for interacting with the system.
- `main.py` - Entry point that runs the research pipeline for a default topic.
- `src/agents/agents.py` - Defines the search agent, reader agent, writer chain, and critic chain.
- `src/pipelines/pipeline.py` - Orchestrates the full research workflow.
- `src/tools/tools.py` - Contains the web search and URL scraping tools.

## Run the Project

Run the Streamlit app:

```bash
streamlit run app.py
```

Or run the pipeline from the command line:

```bash
python main.py
```

## Author

Built with ❤️ by Karthikeya