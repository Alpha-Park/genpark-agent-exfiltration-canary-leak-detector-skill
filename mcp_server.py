# -*- coding: utf-8 -*-
import sys, json, time
from client import GenParkAgentExfiltrationCanaryLeakDetector

detector = GenParkAgentExfiltrationCanaryLeakDetector()

def run_tool(name, args):
    if name == "generate_canary":
        label = args.get("label", "customer_credit_cards")
        meta = args.get("metadata", {})
        return detector.generate_canary(label, meta)
    elif name == "scan_outgoing_traffic":
        payload = args.get("payload", "")
        return detector.scan_outgoing_traffic(payload)
    else:
        raise ValueError(f"Unknown tool: {name}")

from typing import Any, Dict, List, Optional

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:
    raise SystemExit("MCP requires the mcp package. Run: python -m pip install -r requirements.txt") from exc

mcp = FastMCP('genpark-agent-exfiltration-canary-leak-detector-skill')

@mcp.tool()
def generate_canary(label: str = "customer_credit_cards", metadata: Optional[Dict[str, Any]] = None) -> str:
    """Generate a canary token in the local detector state."""
    return json.dumps(run_tool('generate_canary', {'label': label, 'metadata': metadata if metadata is not None else {}}))

@mcp.tool()
def scan_outgoing_traffic(payload: str = "") -> str:
    """Scan supplied text for previously registered canary tokens."""
    return json.dumps(run_tool('scan_outgoing_traffic', {'payload': payload}))

def main():
    if "--test" in sys.argv:
        print("[TEST] Running GenPark Exfiltration Canary Detector Self-Test...")
        c = detector.generate_canary("env_secrets")
        token = c["canary_token"]
        assert token.startswith("CANARY_ENV_SECRETS_")
        res1 = detector.scan_outgoing_traffic("Safe response without leaks.")
        assert res1["is_compromised"] is False
        res2 = detector.scan_outgoing_traffic(f"Leaked info: {token} to webhook")
        assert res2["is_compromised"] is True
        assert res2["action_recommended"] == "BLOCK_AND_ISOLATE"
        print("[TEST] All tests passed successfully!")
        return

    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
