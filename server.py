# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def get_latest_messages_from_slack():
    """
    Returns message from slack
    """
    return ["No new messages"]


if __name__ == "__main__":
    print ("running mcp demo server")
    mcp.run()