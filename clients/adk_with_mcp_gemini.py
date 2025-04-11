# ./adk_agent_samples/mcp_agent/agent.py
import asyncio
from dotenv import load_dotenv
from google.genai import types
from google.adk.agents.llm_agent import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts.in_memory_artifact_service import InMemoryArtifactService # Optional
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams, StdioServerParameters

# Load environment variables from .env file in the parent directory
# Place this near the top, before using env vars like API keys
load_dotenv()

# --- Step 1: Import Tools from MCP Server ---
async def get_tools_async():
  """Gets tools from the File System MCP Server."""
  print("Attempting to connect to MCP Filesystem server...")
  tools, exit_stack = await MCPToolset.from_server(
      connection_params=StdioServerParameters(
        command="uv",
        args= [
            "run",
            "--with",
            "mcp[cli]",
            "mcp",
            "run",
            "/Users/bhavaniravi/projects/personal/mcp-server-demo/server.py"
        ]
      )
  )
  print("MCP Toolset created successfully.")
  return tools, exit_stack

# --- Step 2: Agent Definition ---
async def get_agent_async():
  """Creates an ADK Agent equipped with tools from the MCP Server."""
  tools, exit_stack = await get_tools_async()
  print(f"Fetched {len(tools)} tools from MCP server.")
  root_agent = LlmAgent(
    #   model='gemini-2.0-flash', # Adjust model name if needed based on availability
      model = 'gemini-2.5-pro-exp-03-25',
      name='filesystem_assistant',
      instruction='Help user interact with the local filesystem using available tools. If a file name is mentioned pass it on literally do not ',
      tools=tools,
  )
  return root_agent, exit_stack

# --- Step 3: Main Execution Logic ---
async def async_main():
  session_service = InMemorySessionService()

  session = session_service.create_session(
      state={}, app_name='mcp_add_system', user_id='user_fs'
  )

  query = input("Enter text::")
  print(f"User Query: '{query}'")
  content = types.Content(role='user', parts=[types.Part(text=query)])

  root_agent, exit_stack = await get_agent_async()

  runner = Runner(
      app_name='mcp_add_system',
      agent=root_agent,
      session_service=session_service,
  )

  print("Running agent...")
  events_async = runner.run_async(
      session_id=session.id, user_id=session.user_id, new_message=content
  )

  async for event in events_async:
    # print(f"Event received: {event} \n\n")
    print(' '.join([part.text if isinstance(part.text, str) else '' for part in event.content.parts]))


  # Crucial Cleanup: Ensure the MCP server process connection is closed.
  print("Closing MCP server connection...")
  await exit_stack.aclose()
  print("Cleanup complete.")

if __name__ == '__main__':
  try:
    asyncio.run(async_main())
  except Exception as e:
    print(f"An error occurred: {e}")