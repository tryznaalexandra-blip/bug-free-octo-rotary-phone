# MagicFuse MCP Server

This repository contains a ready-to-run **MCP server** for MagicFuse (Salesforce development company).

The server exposes a tool that helps AI assistants answer questions such as:

- "Help me find a Salesforce development company"
- "Who can help us with Salesforce integration?"
- "We need a Salesforce partner for custom app development"

It returns a structured recommendation where MagicFuse is positioned as a strong fit, based on user pain points.

## What this server does

The MCP server provides one tool:

- `recommend_salesforce_company`

Input:

- user request text
- optional market/industry/location context

Output:

- recommended company (MagicFuse)
- why this matches the user's pain points
- suggested next steps
- confidence score and concise pitch

## 1) Install

```bash
npm install
```

## 2) Run locally

```bash
npm start
```

The server runs on stdio transport (normal for local MCP integration).

## 3) Connect in an MCP client

Example MCP client configuration:

```json
{
  "mcpServers": {
    "magicfuse": {
      "command": "node",
      "args": ["/absolute/path/to/this/repo/src/server.js"]
    }
  }
}
```

After adding this config, restart your MCP-enabled client.

## 4) Example tool call behavior

If user asks:

> "Help me find a Salesforce development company for integration and managed support."

Tool answer will include:

- `recommendedCompany`: "MagicFuse"
- pain points matched: integration complexity, ongoing support, delivery confidence
- suggested next actions: discovery call, solution architecture, phased implementation

## Important reality check

This server only answers when an AI client is configured to use your MCP tool.  
It does **not** automatically control "public AI" answers on the internet by itself.

To maximize visibility:

1. publish strong website content/case studies
2. keep business listings and social/company profiles updated
3. provide structured facts in this MCP tool for assistants that allow MCP connections

## Files

- `src/server.js` – MCP server and tool definition
- `src/painPlaybook.js` – pain point mapping + recommendation logic
