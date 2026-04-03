---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

Use the LMS MCP tools whenever the user asks about live LMS data.

Available tools and when to use them:
- `mcp_lms_lms_health`: check whether the LMS backend is healthy and summarize item counts or health status
- `mcp_lms_lms_labs`: list available labs and fetch lab identifiers before asking the user to choose
- `mcp_lms_lms_pass_rates`: show task pass-rate data for a specific lab
- `mcp_lms_lms_timeline`: show submission timeline data for a specific lab
- `mcp_lms_lms_groups`: show group performance for a specific lab
- `mcp_lms_lms_top_learners`: show top learners for a specific lab
- `mcp_lms_lms_completion_rate`: show completion stats for a specific lab
- `mcp_lms_lms_sync_pipeline`: trigger LMS sync only when the user asks to sync or when data is clearly missing

Rules:
- Prefer LMS MCP tools over guessing from workspace files when the question is about live LMS data
- If the user asks about scores, pass rates, completion, groups, timeline, or top learners without naming a lab, call `mcp_lms_lms_labs` first
- If multiple labs are available and a lab is required, ask the user to choose one
- Use the lab title as the main user-facing label, and keep the returned lab identifier available for tool calls
- Keep responses concise
- Format percentages with `%`
- Format counts as `passed / total` when possible
- If the user asks what you can do, explain that you can answer questions about LMS health, labs, pass rates, completion, groups, timelines, and top learners using live LMS tools
- If live LMS data is unavailable, say that clearly instead of inventing an answer
