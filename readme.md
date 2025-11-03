# 🎓 Advanced AI Learning Assistant - MCP Server

> A sophisticated educational AI system built with the Model Context Protocol (MCP) and OpenAI's Agent SDK

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)](https://openai.com/)
[![MCP](https://img.shields.io/badge/MCP-Protocol-orange.svg)](https://modelcontextprotocol.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Key Features

### 1. 🧠 **Socratic Dialogue Engine**
Guides students through discovery learning using probing questions instead of direct answers.

### 2. 🗺️ **Intelligent Learning Path Generator**
Creates personalized, week-by-week curricula with:
- Hands-on projects at each milestone
- Industry-relevant resources
- Built-in assessments
- Realistic timeframes

### 3. 🔗 **Concept Prerequisite Mapper**
Generates knowledge dependency graphs showing what concepts are needed before others.

### 4. 📊 **Knowledge Gap Analyzer**
Analyzes student explanations to provide:
- Specific gap identification
- Misconception correction
- Personalized remediation strategies

### 5. 🔍 **Professional Code Reviewer**
Enterprise-grade analysis covering:
- Bug detection and edge cases
- Style and readability (PEP 8)
- Performance optimizations
- Security vulnerabilities
- Best practices and design patterns

### 6. 🎯 **Adaptive Practice Problem Generator**
Creates varied problems with:
- Multiple difficulty levels
- Hints and solutions
- Common mistakes to avoid
- Follow-up challenges

### 7. 📚 **Research Paper Analyzer**
Multi-level summaries including:
- ELI5 explanations
- Technical breakdowns
- Critical analysis
- Practical implications

### 8. 📅 **Smart Study Scheduler**
Optimizes learning with:
- Spaced repetition
- Active recall techniques
- Realistic time allocation
- Progress checkpoints

### 9. 📰 **News Newsletter Generator**
Aggregates and curates recent news with:
- Article summaries
- Trend analysis
- Multiple output styles
- Original source links

## 🏗️ Architecture

```
┌──────────────┐         MCP over STDIO        ┌───────────────┐
│              │◄─────────────────────────────►│               │
│   agent.py   │                                │ mcp_server.py │
│   (Client)   │   Tool Calls & JSON Results   │   (Server)    │
│              │◄───────────────────────────────┤               │
└──────────────┘                                └───────┬───────┘
                                                        │
     Agent SDK                                          │
     - Tool Discovery                           OpenAI API
     - Context Management                       - GPT-4o-mini
     - Timeout Management                       - Structured Output
     - Conversation Flow                        - JSON Mode
```

## 📋 Prerequisites

- Python 3.10 or higher
- OpenAI API key
- (Optional) NewsAPI key for newsletter feature

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/advanced-ai-learning-assistant.git
cd advanced-ai-learning-assistant
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
# Required
OPENAI_API_KEY=sk-your-openai-key-here

# Optional (for news newsletter feature)
NEWSAPI_KEY=your-newsapi-key-here
```

**Get API Keys:**
- OpenAI: https://platform.openai.com/api-keys
- NewsAPI: https://newsapi.org/register (free tier: 100 requests/day)

## 💻 Usage

### Start the Assistant

```bash
python agent.py
```

### Example Interactions

**1. Create a Learning Path:**
```
💬 You: Create a 12-week learning path for machine learning

🤖 Assistant: [Comprehensive JSON with weekly curriculum, projects, resources]
```

**2. Map Prerequisites:**
```
💬 You: What prerequisites do I need for understanding transformers?

🤖 Assistant: [Dependency graph showing required concepts]
```

**3. Review Code:**
```
💬 You: Review this Python code:
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

🤖 Assistant: [Detailed analysis with performance issues, suggestions, examples]
```

**4. Generate Newsletter:**
```
💬 You: Create a newsletter with top 10 AI news from this week

🤖 Assistant: [Curated newsletter with summaries and links]
```

**5. Assess Knowledge:**
```
💬 You: Assess my understanding of neural networks: [your explanation]

🤖 Assistant: [Personalized feedback with gaps and remediation]
```

### Special Commands

- `help` - Show examples and available tools
- `clear` - Reset conversation context
- `exit` / `quit` / `bye` - Exit the program

## 📁 Project Structure

```
advanced-ai-learning-assistant/
│
├── agent.py                 # Main agent client with chat interface
├── mcp_server.py           # MCP server with 9 advanced tools
├── .env                    # Environment variables (create this)
├── .env.example           # Template for environment variables
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## 🔧 Configuration

### Adjust Timeouts

In `agent.py`:
```python
mcp_server = MCPServerStdio(
    name="Advanced AI Tutor",
    params={...},
    timeout=300,  # Server process timeout
    client_session_timeout_seconds=300  # Session timeout
)
```

### Change Model

In `mcp_server.py`:
```python
MODEL_NAME = "gpt-4o"        # Best quality
MODEL_NAME = "gpt-4o-mini"   # Fast & economical (default)
MODEL_NAME = "gpt-4-turbo"   # High quality
```

### Customize Tool Behavior

Edit functions in `mcp_server.py`:
- Modify prompts in each `*_fn()` function
- Adjust parameters (difficulty levels, timeframes, etc.)
- Add new tools following the existing pattern

## 🧪 Testing

### Test NewsAPI Connection

```bash
python test_newsapi.py
```

### Test MCP Server Standalone

```bash
python mcp_server.py
```

### Run Agent in Debug Mode

```bash
# Windows
set DEBUG=true
python agent.py

# Mac/Linux
DEBUG=true python agent.py
```

## 🎯 Future Enhancements

- [ ] Vector database integration for RAG
- [ ] Multi-agent collaboration
- [ ] Web interface (Gradio/Streamlit)
- [ ] File upload support (PDFs, code files)
- [ ] Conversation history persistence
- [ ] Analytics dashboard
- [ ] Multi-language support
- [ ] LMS platform integration

## 📚 Resources & References

- [Model Context Protocol Docs](https://modelcontextprotocol.io/)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-sdk)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)


