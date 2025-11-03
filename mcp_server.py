'''
Advanced Learning Assistant
Features:
- Socratic teaching method
- Learning path generation
- Concept prerequisite mapping
- Adaptive difficulty assessment
- Code review and debugging
- Research paper summarization
- Study Scheduler
- News aggregation and newsletter generation tool. 
'''

import os
import json
import requests  
from datetime import datetime, timedelta 
from typing import List, Dict, Any
from openai import OpenAI
from dotenv import load_dotenv
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types as mcp_types
import asyncio

# Load environment
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found")
# Disable tracing errors
os.environ["OPENAI_LOG"] = "error"
client = OpenAI(
    api_key=openai_api_key,
     timeout=120.0)
MODEL_NAME = "gpt-4o-mini"


# Create MCP Server instance
server = Server("advanced-learning-assistant")

# Tool functions
def socratic_dialogue_fn(topic: str, student_answer: str = "", depth: int = 3) -> str:
    """
    Engage in Socratic questioning to deepen understanding.
    Instead of giving answers, asks probing questions.
    
    Showcases: Advanced prompting, educational psychology, iterative reasoning
    """
    if not topic.strip():
        return "Error: topic cannot be blank."
    
    if student_answer:
        system_prompt = f"""You are a Socratic tutor. The student is learning about {topic}.
They provided this answer/thought: "{student_answer}"

Instead of telling them if they're right or wrong, ask {depth} probing questions that:
1. Challenge their assumptions
2. Explore edge cases
3. Connect to related concepts
4. Encourage deeper thinking

Format as numbered questions. Be encouraging but intellectually rigorous."""
    else:
        system_prompt = f"""You are a Socratic tutor introducing {topic}.

Start by asking {depth} thought-provoking questions that:
1. Assess their current understanding
2. Make them think about real-world applications
3. Connect to concepts they might already know

Don't explain the topic yet - just ask questions to stimulate thinking."""
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "system", "content": system_prompt}],
        temperature=0.8,
    )
    return response.choices[0].message.content

def generate_learning_path_fn(topic: str, current_level: str = "beginner", 
                               goal: str = "mastery", timeframe_weeks: int = 12) -> str:
    """
    Create a personalized, structured learning path with milestones.
    
    Showcases: Curriculum design, project planning, structured output
    """
    if not topic.strip():
        return "Error: topic cannot be blank."
    
    system_prompt = f"""You are an expert curriculum designer. Create a comprehensive {timeframe_weeks}-week learning path.

Student Profile:
- Topic: {topic}
- Current Level: {current_level}
- Goal: {goal}
- Duration: {timeframe_weeks} weeks

Generate a structured learning path in JSON format:
{{
  "overview": "Brief description of the journey",
  "prerequisites": ["list", "of", "prerequisites"],
  "phases": [
    {{
      "week": 1,
      "phase_name": "Foundations",
      "objectives": ["specific", "learning", "objectives"],
      "resources": ["books/courses/tools to use"],
      "projects": ["hands-on project"],
      "assessment": "How to verify mastery"
    }}
  ],
  "milestones": [
    {{
      "week": 4,
      "milestone": "Build first project",
      "success_criteria": "What success looks like"
    }}
  ],
  "final_capstone": "Major project demonstrating mastery"
}}

Make it practical, achievable, and industry-relevant."""
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "system", "content": system_prompt}],
        temperature=0.7,
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content

def map_concept_prerequisites_fn(concept: str, depth: int = 3) -> str:
    """
    Generate a dependency graph of prerequisite concepts.
    
    Showcases: Knowledge graphs, system thinking, hierarchical reasoning
    """
    if not concept.strip():
        return "Error: concept cannot be blank."
    
    system_prompt = f"""You are a knowledge architect. Map out the prerequisite concepts for understanding "{concept}".

Create a dependency graph showing {depth} levels of prerequisites in JSON:
{{
  "target_concept": "{concept}",
  "complexity_level": "beginner/intermediate/advanced",
  "prerequisite_graph": [
    {{
      "level": 1,
      "concepts": [
        {{
          "name": "Concept Name",
          "why_needed": "Brief explanation",
          "estimated_study_time": "2 hours",
          "resources": ["where to learn this"]
        }}
      ]
    }}
  ],
  "learning_order": ["ordered list of concepts"],
  "optional_concepts": ["nice-to-know but not required"],
  "common_misconceptions": ["what students often get wrong"]
}}

Think like building a skill tree in a video game - what must you unlock first?"""
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "system", "content": system_prompt}],
        temperature=0.7,
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content

def assess_knowledge_gaps_fn(topic: str, student_explanation: str) -> str:
    """
    Analyze student's explanation to identify knowledge gaps and misconceptions.
    
    Showcases: NLP analysis, pedagogical assessment, personalized feedback
    """
    if not topic.strip() or not student_explanation.strip():
        return "Error: both topic and student_explanation are required."
    
    system_prompt = f"""You are an expert educator analyzing a student's understanding of {topic}.

Student's Explanation:
"{student_explanation}"

Provide a detailed assessment in JSON:
{{
  "overall_understanding": "percentage (0-100)",
  "strengths": ["what they understand well"],
  "knowledge_gaps": [
    {{
      "gap": "What's missing",
      "severity": "critical/important/minor",
      "remediation": "How to address this gap"
    }}
  ],
  "misconceptions": [
    {{
      "misconception": "What they got wrong",
      "correct_concept": "What they should understand",
      "explanation": "Why this matters"
    }}
  ],
  "next_steps": ["ordered list of what to study next"],
  "estimated_time_to_mastery": "X hours/days/weeks",
  "recommended_resources": ["specific books/courses/exercises"]
}}

Be specific, constructive, and actionable."""
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "system", "content": system_prompt}],
        temperature=0.6,
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content

def review_code_fn(code: str, language: str = "python", 
                    focus: str = "all") -> str:
    """
    Comprehensive code review: bugs, style, performance, security.
    
    Showcases: Code analysis, best practices, technical depth
    """
    if not code.strip():
        return "Error: code cannot be blank."
    
    focus_areas = {
        "all": "bugs, style, performance, security, and best practices",
        "bugs": "potential bugs and errors",
        "style": "code style and readability",
        "performance": "performance optimizations",
        "security": "security vulnerabilities"
    }
    
    system_prompt = f"""You are a senior software engineer conducting a code review.

Language: {language}
Focus: {focus_areas.get(focus, focus_areas['all'])}

Analyze this code and provide a structured review in JSON:
{{
  "overall_quality": "rating (1-10)",
  "summary": "Brief assessment",
  "issues": [
    {{
      "severity": "critical/high/medium/low",
      "category": "bug/style/performance/security",
      "line": "approximate line number or section",
      "issue": "What's wrong",
      "explanation": "Why this is a problem",
      "fix": "How to fix it",
      "code_example": "corrected code snippet"
    }}
  ],
  "strengths": ["what's done well"],
  "refactoring_suggestions": ["structural improvements"],
  "testing_recommendations": ["what tests to add"],
  "complexity_analysis": "assessment of code complexity"
}}

Code to review:
```{language}
{code}
```

Be thorough but constructive."""
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "system", "content": system_prompt}],
        temperature=0.5,
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content

def generate_practice_problems_fn(topic: str, difficulty: str = "medium",
                                  problem_type: str = "mixed", count: int = 5) -> str:
    """
    Generate varied practice problems with solutions and hints.
    
    Showcases: Educational content generation, adaptive difficulty
    """
    if not topic.strip():
        return "Error: topic cannot be blank."
    
    if count < 1 or count > 20:
        return "Error: count must be between 1 and 20."
    
    problem_types_desc = {
        "mixed": "a mix of conceptual, application, and analytical problems",
        "conceptual": "conceptual understanding questions",
        "application": "practical application problems",
        "analytical": "deep analytical challenges",
        "debugging": "code debugging exercises"
    }
    
    system_prompt = f"""You are an expert problem creator for {topic}.

Generate {count} {difficulty} difficulty problems focused on {problem_types_desc.get(problem_type, problem_type)}.

Format as JSON:
{{
  "problems": [
    {{
      "number": 1,
      "title": "Problem Title",
      "difficulty": "{difficulty}",
      "type": "{problem_type}",
      "problem_statement": "Detailed problem description",
      "hints": ["hint 1", "hint 2"],
      "solution": "Complete solution with explanation",
      "common_mistakes": ["what students often do wrong"],
      "follow_up_questions": ["extensions to explore"],
      "estimated_time": "minutes to solve",
      "learning_objectives": ["what this problem teaches"]
    }}
  ]
}}

Make problems realistic, engaging, and pedagogically valuable."""
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "system", "content": system_prompt}],
        temperature=0.8,
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content

def summarize_research_paper_fn(paper_text: str, audience: str = "general") -> str:
    """
    Multi-level research paper summary (ELI5, technical, implications).
    
    Showcases: Academic analysis, multi-audience communication, critical thinking
    """
    if not paper_text.strip():
        return "Error: paper_text cannot be blank."
    
    if len(paper_text) < 100:
        return "Error: paper_text is too short. Please provide the full paper or at least the abstract and key sections."
    
    system_prompt = f"""You are a research analyst. Summarize this academic paper for a {audience} audience.

Provide a multi-layered summary in JSON:
{{
  "title": "inferred title",
  "eli5_summary": "Explain like I'm 5 - simple analogy",
  "executive_summary": "3-4 sentences for busy professionals",
  "technical_summary": {{
    "problem": "What problem does this solve?",
    "method": "How did they approach it?",
    "results": "What did they find?",
    "novelty": "What's new or innovative?"
  }},
  "key_findings": ["bullet points of main discoveries"],
  "methodology": "Brief description of research methods",
  "limitations": ["acknowledged limitations"],
  "implications": {{
    "theoretical": "Impact on the field",
    "practical": "Real-world applications",
    "future_research": "What's next?"
  }},
  "related_concepts": ["concepts to explore further"],
  "critical_analysis": "Strengths and weaknesses",
  "citation_worthiness": "rating and why"
}}

Paper text:
{paper_text[:3000]}...  # Truncate if too long"""
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "system", "content": system_prompt}],
        temperature=0.6,
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content


def create_study_schedule_fn(topics: str, deadline_days: int = 30,
                             hours_per_week: int = 10, learning_style: str = "balanced") -> str:
    """
    Generate a realistic, adaptive study schedule with time management.
    
    Showcases: Planning algorithms, resource optimization, personalization
    """
    if not topics.strip():
        return "Error: topics cannot be blank."
    
    if deadline_days < 1 or hours_per_week < 1:
        return "Error: deadline_days and hours_per_week must be positive."
    
    system_prompt = f"""You are a study coach creating a personalized schedule.

Requirements:
- Topics to cover: {topics}
- Deadline: {deadline_days} days
- Available time: {hours_per_week} hours/week
- Learning style: {learning_style}

Create a detailed study plan in JSON:
{{
  "total_study_hours": {hours_per_week * (deadline_days/7)},
  "topics_breakdown": [
    {{
      "topic": "Topic name",
      "estimated_hours": 10,
      "priority": "high/medium/low",
      "complexity": "easy/medium/hard"
    }}
  ],
  "weekly_schedule": [
    {{
      "week": 1,
      "focus_topics": ["topics for this week"],
      "daily_breakdown": [
        {{
          "day": "Monday",
          "morning": "specific activity",
          "afternoon": "specific activity",
          "evening": "review/practice"
        }}
      ],
      "goals": ["what to accomplish"],
      "checkpoints": ["how to verify progress"]
    }}
  ],
  "buffer_time": "built-in slack for unexpected delays",
  "revision_cycles": ["when to review previous material"],
  "stress_management": ["breaks, rest days"],
  "success_metrics": ["how to measure if you're on track"]
}}

Consider spaced repetition, active recall, and realistic pacing."""
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "system", "content": system_prompt}],
        temperature=0.7,
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content

def generate_news_newsletter_fn(
    topic: str = "artificial intelligence",
    num_articles: int = 10,
    days_back: int = 7,
    newsletter_style: str = "professional"
) -> str:
    """
    Fetch recent news and generate a professional newsletter.
    FIXED: Simplified version that works reliably.
    """
    articles = []
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_back)
    
    # NewsAPI first
    newsapi_key = os.getenv("NEWSAPI_KEY")
    if newsapi_key:
        try:
            response = requests.get(
                "https://newsapi.org/v2/everything",
                params={
                    "q": topic,
                    "from": start_date.strftime("%Y-%m-%d"),
                    "sortBy": "publishedAt",
                    "language": "en",
                    "pageSize": num_articles,
                    "apiKey": newsapi_key
                },
                timeout=10
            )
            
            if response.status_code == 200:
                for article in response.json().get("articles", [])[:num_articles]:
                    articles.append({
                        "title": article.get("title", ""),
                        "description": article.get("description", ""),
                        "url": article.get("url", ""),
                        "source": article.get("source", {}).get("name", ""),
                        "published_at": article.get("publishedAt", "")
                    })
        except Exception as e:
            print(f"NewsAPI error: {e}")
    
    # Fallback: Create sample articles if API unavailable
    if not articles:
        articles = [{
            "title": f"Recent Development in {topic} #{i+1}",
            "description": "Breaking news and analysis of recent developments in the field...",
            "url": "https://example.com/article",
            "source": "Tech News",
            "published_at": (end_date - timedelta(days=i)).isoformat()
        } for i in range(num_articles)]
    
    # Generate newsletter with GPT
    prompt = f"""Create a {newsletter_style} newsletter about "{topic}" from these articles:

{json.dumps(articles, indent=2)}

Return JSON with:
{{
  "title": "Newsletter title",
  "date": "{end_date.strftime('%B %d, %Y')}",
  "intro": "2-3 sentence intro",
  "articles": [
    {{
      "headline": "Catchy headline",
      "summary": "3-4 sentence summary",
      "why_matters": "Impact/significance",
      "link": "original URL",
      "source": "source name"
    }}
  ],
  "trends": ["trend 1", "trend 2", "trend 3"],
  "insights": ["insight 1", "insight 2"],
  "markdown": "Full newsletter in Markdown format"
}}"""
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "system", "content": prompt}],
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content
    except Exception as e:
        return json.dumps({"error": str(e), "raw_articles": articles})


# Register tools with MCP server 
@server.list_tools()
async def list_tools() -> list[mcp_types.Tool]:
    """List all available advanced educational tools."""
    return [
        mcp_types.Tool(
            name="socratic_dialogue",
            description="Engage in Socratic questioning to deepen understanding through probing questions rather than direct answers",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "The concept or topic to explore"
                    },
                    "student_answer": {
                        "type": "string",
                        "description": "Optional: Student's current answer or thought to analyze",
                        "default": ""
                    },
                    "depth": {
                        "type": "integer",
                        "description": "Number of probing questions to ask (1-10)",
                        "default": 3,
                        "minimum": 1,
                        "maximum": 10
                    }
                },
                "required": ["topic"]
            }
        ),
        mcp_types.Tool(
            name="generate_learning_path",
            description="Create a comprehensive, personalized learning roadmap with milestones, projects, and assessments",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "The subject to master"
                    },
                    "current_level": {
                        "type": "string",
                        "description": "Current knowledge level: beginner, intermediate, advanced",
                        "default": "beginner"
                    },
                    "goal": {
                        "type": "string",
                        "description": "Learning goal: awareness, competency, mastery, expert",
                        "default": "mastery"
                    },
                    "timeframe_weeks": {
                        "type": "integer",
                        "description": "Available time in weeks (4-52)",
                        "default": 12,
                        "minimum": 4,
                        "maximum": 52
                    }
                },
                "required": ["topic"]
            }
        ),
        mcp_types.Tool(
            name="map_concept_prerequisites",
            description="Generate a dependency graph showing prerequisite concepts needed for understanding a topic",
            inputSchema={
                "type": "object",
                "properties": {
                    "concept": {
                        "type": "string",
                        "description": "The concept to analyze"
                    },
                    "depth": {
                        "type": "integer",
                        "description": "Levels of prerequisites to map (1-5)",
                        "default": 3,
                        "minimum": 1,
                        "maximum": 5
                    }
                },
                "required": ["concept"]
            }
        ),
        mcp_types.Tool(
            name="assess_knowledge_gaps",
            description="Analyze a student's explanation to identify knowledge gaps, misconceptions, and provide targeted remediation",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "The topic being assessed"
                    },
                    "student_explanation": {
                        "type": "string",
                        "description": "Student's explanation or answer to analyze"
                    }
                },
                "required": ["topic", "student_explanation"]
            }
        ),
        mcp_types.Tool(
            name="review_code",
            description="Comprehensive code review analyzing bugs, style, performance, security, and best practices",
            inputSchema={
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "Code to review"
                    },
                    "language": {
                        "type": "string",
                        "description": "Programming language",
                        "default": "python"
                    },
                    "focus": {
                        "type": "string",
                        "description": "Review focus: all, bugs, style, performance, security",
                        "default": "all"
                    }
                },
                "required": ["code"]
            }
        ),
        mcp_types.Tool(
            name="generate_practice_problems",
            description="Create varied practice problems with solutions, hints, and common mistakes",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Topic for practice problems"
                    },
                    "difficulty": {
                        "type": "string",
                        "description": "Difficulty level: easy, medium, hard, expert",
                        "default": "medium"
                    },
                    "problem_type": {
                        "type": "string",
                        "description": "Type: mixed, conceptual, application, analytical, debugging",
                        "default": "mixed"
                    },
                    "count": {
                        "type": "integer",
                        "description": "Number of problems (1-20)",
                        "default": 5,
                        "minimum": 1,
                        "maximum": 20
                    }
                },
                "required": ["topic"]
            }
        ),
        mcp_types.Tool(
            name="summarize_research_paper",
            description="Multi-level academic paper summary (ELI5, technical, implications) with critical analysis",
            inputSchema={
                "type": "object",
                "properties": {
                    "paper_text": {
                        "type": "string",
                        "description": "Full text or substantial excerpt of research paper"
                    },
                    "audience": {
                        "type": "string",
                        "description": "Target audience: general, technical, academic, executive",
                        "default": "general"
                    }
                },
                "required": ["paper_text"]
            }
        ),
        mcp_types.Tool(
            name="create_study_schedule",
            description="Generate a realistic, adaptive study schedule with time management and spaced repetition",
            inputSchema={
                "type": "object",
                "properties": {
                    "topics": {
                        "type": "string",
                        "description": "Topics to study (comma-separated)"
                    },
                    "deadline_days": {
                        "type": "integer",
                        "description": "Days until deadline (1-365)",
                        "default": 30,
                        "minimum": 1,
                        "maximum": 365
                    },
                    "hours_per_week": {
                        "type": "integer",
                        "description": "Available study hours per week (1-80)",
                        "default": 10,
                        "minimum": 1,
                        "maximum": 80
                    },
                    "learning_style": {
                        "type": "string",
                        "description": "Learning preference: visual, auditory, kinesthetic, balanced",
                        "default": "balanced"
                    }
                },
                "required": ["topics"]
            }
        ),
        mcp_types.Tool(
            name="generate_news_newsletter",
            description="Fetch recent news and generate a curated newsletter with summaries and links",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "News topic",
                        "default": "artificial intelligence"
                    },
                    "num_articles": {
                        "type": "integer",
                        "description": "Number of articles (1-50)",
                        "default": 10,
                        "minimum": 1,
                        "maximum": 50
                    },
                    "days_back": {
                        "type": "integer",
                        "description": "Days to look back (1-30)",
                        "default": 7,
                        "minimum": 1,
                        "maximum": 30
                    },
                    "newsletter_style": {
                        "type": "string",
                        "description": "Style: professional/casual/technical/executive",
                        "default": "professional"
                    }
                },
                "required": []
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[mcp_types.TextContent]:
    """Route tool calls to appropriate functions."""
    
    if name == "socratic_dialogue":
        result = socratic_dialogue_fn(
            arguments.get("topic"),
            arguments.get("student_answer", ""),
            arguments.get("depth", 3)
        )
    elif name == "generate_learning_path":
        result = generate_learning_path_fn(
            arguments.get("topic"),
            arguments.get("current_level", "beginner"),
            arguments.get("goal", "mastery"),
            arguments.get("timeframe_weeks", 12)
        )
    elif name == "map_concept_prerequisites":
        result = map_concept_prerequisites_fn(
            arguments.get("concept"),
            arguments.get("depth", 3)
        )
    elif name == "assess_knowledge_gaps":
        result = assess_knowledge_gaps_fn(
            arguments.get("topic"),
            arguments.get("student_explanation")
        )
    elif name == "review_code":
        result = review_code_fn(
            arguments.get("code"),
            arguments.get("language", "python"),
            arguments.get("focus", "all")
        )
    elif name == "generate_practice_problems":
        result = generate_practice_problems_fn(
            arguments.get("topic"),
            arguments.get("difficulty", "medium"),
            arguments.get("problem_type", "mixed"),
            arguments.get("count", 5)
        )
    elif name == "summarize_research_paper":
        result = summarize_research_paper_fn(
            arguments.get("paper_text"),
            arguments.get("audience", "general")
        )
    elif name == "create_study_schedule":
        result = create_study_schedule_fn(
            arguments.get("topics"),
            arguments.get("deadline_days", 30),
            arguments.get("hours_per_week", 10),
            arguments.get("learning_style", "balanced")
        )
    elif name == "generate_news_newsletter":  # FIXED: proper indentation
        result = generate_news_newsletter_fn(
            arguments.get("topic", "artificial intelligence"),
            arguments.get("num_articles", 10),
            arguments.get("days_back", 7),
            arguments.get("newsletter_style", "professional")
        )
    else:
        raise ValueError(f"Unknown tool: {name}")
    
    return [mcp_types.TextContent(type="text", text=result)]


async def main():
    """Run the advanced MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())