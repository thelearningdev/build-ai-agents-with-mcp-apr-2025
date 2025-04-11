# Build AI Agents With MCP

## Tools and Installations

> If you're on MacOS please use `brew` to install the packages

> Claude free version has daily limits don't exhaust it before the event.

> Once installed you should be able to run `node`, `nvm`,`npx`, `uv`, `python` commands from a terminal or shell and get some response. If you get `command not found` then the installation didn't happen properly

1. Install nodejs and npx. 
2. Install python latest version (3.11+) and [uv](https://docs.astral.sh/uv/getting-started/installation/).  to install uv.
3. [Download and Install Claude Desktop](https://claude.ai/download)
4. Clone this repo and run the following commands

```
uv venv
uv sync
```

--- 

## Brief History of AI & Agents 

1. What are LLMs?
2. What are agents, why we need them how we got here?
3. MCP

## Step 1: Getting  a Taste of MCP 

> Claude free version has daily limits don't exhaust it before the event. 

Install Claude Desktop and get a taste of connecting the server to it - https://modelcontextprotocol.io/quickstart/user

## Step 2: Build Your Own MCP Server

Building a weather agent server
https://modelcontextprotocol.io/quickstart/server


## Step 3: (Optional) Build Your Own MCP Client

> Needs paid anthropic account. 

If you're integrating Agentic systems into your own UI or other apps eg., Slack/Whatsapp/Telegram you will need the respective API Key from the model providers(OpenAI, Anthropic, Google)

We have two options here

Anthropic MCP Client Paid 5$
https://modelcontextprotocol.io/quickstart/client


## Step 3: Agent SDK from Google vs MCP

https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/develop/adk
