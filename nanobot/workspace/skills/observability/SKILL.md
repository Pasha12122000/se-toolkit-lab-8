---
name: observability
description: Use observability tools for logs and traces
always: true
---

Use observability MCP tools when the user asks about errors, failures, traces, logs, outages, recent backend problems, "What went wrong?", or "Check system health".

Rules:
- For recent backend/system errors, call `mcp_obs_logs_error_count` first with a narrow recent window
- Then call `mcp_obs_logs_search` scoped to the most likely failing service
- If a `trace_id` appears in logs, call `mcp_obs_traces_get`
- If needed, call `mcp_obs_traces_list` for recent traces for the service
- Summarize findings briefly
- Explicitly mention both log evidence and trace evidence when answering "What went wrong?"
- Do not dump raw JSON unless the user explicitly asks for it
