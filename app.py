from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)
UPSTREAM = "https://mcp.lastintel.io"

def call_mcp(name, arguments):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": name, "arguments": arguments}
    }
    r = requests.post(
        UPSTREAM,
        json=payload,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "MCP-Protocol-Version": "2025-06-18",
            "User-Agent": "WarzoneAtlas/2.0"
        },
        timeout=15
    )
    r.raise_for_status()
    return r.json()

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/search")
def search():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify({"items": []})
    try:
        data = call_mcp("search_commanders_and_alliances", {"query": q, "limit": 20})
        return jsonify(data.get("result", {}).get("structuredContent", {"items": []}))
    except Exception as e:
        return jsonify({"error": "Upstream request failed", "details": str(e)}), 502

@app.get("/api/warzones")
def warzones():
    try:
        data = call_mcp("list_warzones", {"limit": 100})
        return jsonify(data.get("result", {}).get("structuredContent", {"items": []}))
    except Exception as e:
        return jsonify({"error": "Upstream request failed", "details": str(e)}), 502

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "10000")))
