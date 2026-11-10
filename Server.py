from mcp.server import MCPServer

# Initialize MCP server
mcp = MCPServer("MyFirstServer")

# Register a tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def addTwoNumber(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def powerOfNumber(a: int, b: int) -> int:
    """Power of numbers."""
    return a ** b


if __name__ == "__main__":
    mcp.run(transport="stdio")