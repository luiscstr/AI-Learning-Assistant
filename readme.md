# 🎓 Advanced AI Learning Assistant - MCP Server

> A sophisticated educational AI system built with the Model Context Protocol (MCP) and OpenAI's Agent SDK, showcasing enterprise-grade AI engineering and pedagogical capabilities.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)](https://openai.com/)
[![MCP](https://img.shields.io/badge/MCP-Protocol-orange.svg)](https://modelcontextprotocol.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Overview

This project demonstrates **production-ready AI engineering** through a comprehensive educational assistant that showcases:

- ✅ **Custom MCP Server Implementation** - Built following protocol specifications
- ✅ **Advanced Prompting Techniques** - Socratic method, structured outputs, JSON mode
- ✅ **Pedagogical AI** - Knowledge gap assessment, adaptive learning paths
- ✅ **Real-world Integration** - News aggregation, code review, research analysis
- ✅ **Production Architecture** - Proper error handling, timeout management, process orchestration

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

You'll see:
```
✅ Timeout environment variables configured (300s backup)
🚀 Starting Advanced AI Tutor...
✅ Successfully Connected!

📚 Found 9 Advanced Tools:
   1. socratic_dialogue
   2. generate_learning_path
   3. map_concept_prerequisites
   ...

💬 Type your question or 'exit' to quit
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
├── fix_timeout.py          # Timeout configuration module
├── test_newsapi.py         # NewsAPI connection test utility
│
├── .env                    # Environment variables (create this)
├── .env.example           # Template for environment variables
├── .gitignore             # Git ignore patterns
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License
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

## 📊 Skills Demonstrated

### For Technical Recruiters

**AI/ML Engineering:**
- Large Language Model integration
- Advanced prompt engineering
- Structured output generation (JSON mode)
- Multi-turn conversation management

**Software Architecture:**
- Client-server design patterns
- Protocol implementation (MCP)
- Asynchronous programming
- Process management and IPC

**Code Quality:**
- Type hints and comprehensive documentation
- Error handling and logging
- Configuration management
- Modular, testable design

**Domain Expertise:**
- Educational technology
- Cognitive science principles
- Academic content analysis
- News aggregation and curation

## 🐛 Troubleshooting

### "Connection closed" Error

**Solution:** Run `python mcp_server.py` standalone to see the actual error.

Common causes:
- Missing imports (`requests`, `datetime`)
- Syntax errors in tool functions
- Missing OpenAI API key

### Timeout Errors

**Solution:** Timeouts are already set to 300 seconds (5 minutes). If still timing out:
1. Check your internet connection
2. Verify OpenAI API status
3. Try a simpler query first

### NewsAPI Issues

**Solution:** Run `python test_newsapi.py` to diagnose.

Common issues:
- Missing or invalid API key
- Rate limit exceeded (100/day on free tier)
- Account restricted to localhost (normal for free tier)

### Import Errors

**Solution:**
```bash
pip install --upgrade -r requirements.txt
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
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas of Interest

- Additional educational tools
- Performance optimizations
- UI/UX improvements
- Documentation enhancements
- Test coverage
- New integrations (Slack, Discord, etc.)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**[Your Name]**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- Portfolio: [yourwebsite.com](https://yourwebsite.com)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Built with [OpenAI Agent SDK](https://github.com/openai/openai-agents-sdk)
- Implements [Model Context Protocol](https://modelcontextprotocol.io/)
- Powered by [OpenAI GPT-4o-mini](https://openai.com/)
- News data from [NewsAPI](https://newsapi.org/)

## 💼 Why This Project Stands Out

### Technical Complexity

- ✅ Custom protocol implementation (MCP)
- ✅ Advanced prompting patterns
- ✅ Multi-tool orchestration
- ✅ Async process management
- ✅ Production-ready error handling
- ✅ Educational domain expertise

### Real-World Application

This isn't a tutorial project - it's a **professional portfolio piece** that:
- Solves actual educational challenges
- Demonstrates enterprise architecture
- Shows production thinking
- Exhibits best practices
- Proves domain expertise

### Metrics

- **9 sophisticated tools** with unique capabilities
- **300-second timeout** handling for complex operations
- **JSON-structured outputs** for reliable parsing
- **Multi-source news aggregation** with deduplication
- **Comprehensive error handling** with graceful degradation

---

**⭐ If this project helped you or inspired your work, please star it on GitHub!**

---

### 📈 Project Stats

![Lines of Code](https://img.shields.io/badge/lines%20of%20code-2000%2B-blue)
![Tools](https://img.shields.io/badge/tools-9-green)
![Response Time](https://img.shields.io/badge/avg%20response-3--10s-yellow)

### 🎓 Perfect For

- AI/ML Engineer positions
- Full-stack Developer roles
- EdTech companies
- AI Research positions
- Technical Lead positions

**Questions?** Open an issue or reach out directly!
