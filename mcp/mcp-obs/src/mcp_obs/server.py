from __future__ import annotations

import json
import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-obs")


def _victorialogs_url() -> str:
    return os.environ["NANOBOT_VICTORIALOGS_URL"].rstrip("/")


def _victoriatraces_url() -> str:
    return os.environ["NANOBOT_VICTORIATRACES_URL"].rstrip("/")


async def _get_json(url: str, params: dict[str, Any] | None = None) -> Any:
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def logs_search(query: str, limit: int = 20) -> str:
    data = await _get_json(
        f"{_victorialogs_url()}/select/logsql/query",
        params={"query": query, "limit": limit},
    )
    return json.dumps(data, ensure_ascii=False)


@mcp.tool()
async def logs_error_count(minutes: int = 10) -> str:
    query = f'_time:{minutes}m service.name:"Learning Management Service" severity:ERROR'
    data = await _get_json(
        f"{_victorialogs_url()}/select/logsql/query",
        params={"query": query, "limit": 100},
    )
    if isinstance(data, list):
        return json.dumps({"count": len(data), "entries": data}, ensure_ascii=False)
    return json.dumps(data, ensure_ascii=False)


@mcp.tool()
async def traces_list(service: str = "Learning Management Service", limit: int = 10) -> str:
    data = await _get_json(
        f"{_victoriatraces_url()}/select/jaeger/api/traces",
        params={"service": service, "limit": limit},
    )
    return json.dumps(data, ensure_ascii=False)


@mcp.tool()
async def traces_get(trace_id: str) -> str:
    data = await _get_json(f"{_victoriatraces_url()}/select/jaeger/api/traces/{trace_id}")
    return json.dumps(data, ensure_ascii=False)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
