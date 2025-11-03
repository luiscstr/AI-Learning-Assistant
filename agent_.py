import os
import asyncio
from dotenv import load_dotenv
from agents.mcp import MCPServerStdio
from agents import Agent, Runner

# Load environment
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ.setdefault("MCP_REQUEST_TIMEOUT", "60")  # 60 seconds
# Connect to MCP server
mcp_server = MCPServerStdio(
    name="AI Tutor",
    params={
        "command": "python",
        "args": ["mcp_server_basic.py"],
    }
)

# Create agent
agent = Agent(
    name="Smart Assistant",
    instructions="""
    You are an AI expert teacher with access to four educational tools:

    1. **explain_concept** - Explain concepts at different difficulty levels
       - Levels: 1=child, 2=beginner, 3=student, 4=expert
    
    2. **summarize_text** - Summarize text with adjustable compression
       - Compression ratio: 0.1 (very short) to 0.8 (detailed)
    
    3. **generate_flashcards** - Create study flashcards
       - Can generate 1-20 flashcards on any topic
    
    4. **quiz_me** - Generate multiple-choice quizzes
       - Can create 1-15 questions at different difficulty levels

    When helping users:
    - Choose the most appropriate tool for their request
    - Use sensible defaults 
    - Present information clearly and encouragingly
    - Ask clarifying questions if needed

    Be helpful, patient, and educational!
    """,
    model="gpt-4o-mini",
    mcp_servers=[mcp_server]
)

async def test_connection():
    """Test MCP server connection."""
    print("🔍 Testing MCP connection...")
    try:
        await mcp_server.connect()
        tools = await mcp_server.list_tools()
        print(f" Connected! Found {len(tools)} tools:")
        for tool in tools:
            print(f"   • {tool.name}: {tool.description}")
        await mcp_server.cleanup()
        print()
        return True
    except Exception as e:
        print(f" Connection test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def chat_loop():
    """Main chat loop."""
    await mcp_server.connect()
     #Patching the MCP session timeout directly to increase the default of 5 secons, which is not enough
    if hasattr(mcp_server, '_session'):
        # Patch the send_request method to use longer timeout
        original_send_request = mcp_server._session.send_request
        
        async def patched_send_request(request, result_type, request_read_timeout_seconds=None, **kwargs):
            return await original_send_request(
                request, 
                result_type, 
                request_read_timeout_seconds=60.0,  # Force 60 second timeout
                **kwargs
            )
        
        mcp_server._session.send_request = patched_send_request

    result = None
    
    print(" AI Assistant Ready!")
    print("=" * 50)
    print("\nAvailable commands:")
    print("  • Ask me to explain any concept")
    print("  • Request summaries of text")
    print("  • Generate flashcards on topics")
    print("  • Quiz yourself on subjects")
    print("\nType 'exit' or 'quit' to end.\n")
    
    try:
        while True:
            user_input = input("\n You: ")
            
            if user_input.lower().strip() in {"exit", "quit", "bye"}:
                print("\n Thanks for learning with me! Goodbye!")
                break
            
            if not user_input.strip():
                continue

            # Maintain conversation context
            if result is not None:
                new_input = result.to_input_list() + [{"role": "user", "content": user_input}]
            else:
                new_input = [{"role": "user", "content": user_input}]

            print("\n Thinking...")
            
            try:
                # Run the agent
                result = await Runner.run(starting_agent=agent, input=new_input)
                
                print("\n Assistant:")
                print("-" * 50)
                print(result.final_output)
                
            except Exception as e:
                print(f"\n Error: {e}")
                import traceback
                traceback.print_exc()
    
    finally:
        # Clean up
        await mcp_server.cleanup()

async def main():
    """Main entry point."""
    # Testing connection
    if await test_connection():
        # Run chat loop
        await chat_loop()
    else:
        print("\n  Could not connect to MCP server.")
        print("Make sure mcp_server.py is in the same directory!")

if __name__ == "__main__":
    asyncio.run(main())