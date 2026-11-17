# genpark-agent-exfiltration-canary-leak-detector-skill

[![Organization](https://img.shields.io/badge/AlphaPark-OpenSource-blue.svg)](https://github.com/Alpha-Park)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard-orange.svg)](https://modelcontextprotocol.io)
[![MCP SDK](https://img.shields.io/badge/MCP_SDK-required-blue.svg)](requirements.txt)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](#)
[![Security Rating](https://img.shields.io/badge/Security-Production_Hardened-success.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Production-hardened Agentic Cybersecurity & Red-Teaming skill with a Python standard-library core and an MCP server powered by the official `mcp` SDK. Provides real-time injection fuzzing, exfiltration canary detection, least-privilege tool sandboxing, and cryptographic audit proofs via the Model Context Protocol (MCP).

---

## MCP runtime requirements

Use Python 3.10 or newer. The core `client.py` uses only the standard library; `mcp_server.py` requires the official `mcp` SDK (`mcp>=1.0.0,<2`). From this repository's checkout, create an isolated environment and install its requirements:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

On Windows, use `.venv\Scripts\python.exe` instead. You may use an existing Python environment with the requirements installed. Configure your MCP client with that interpreter's absolute path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; the GitHub repository URL is not a remote MCP endpoint.

Example client configuration (replace the placeholder paths):

```json
{
  "mcpServers": {
    "genpark-agent-exfiltration-canary-leak-detector-skill": {
      "command": "/absolute/path/to/genpark-agent-exfiltration-canary-leak-detector-skill/.venv/bin/python",
      "args": [
        "/absolute/path/to/genpark-agent-exfiltration-canary-leak-detector-skill/mcp_server.py"
      ]
    }
  }
}
```

## Architecture & Data Flow

```mermaid
flowchart TD
    Payload[Untrusted Prompt / RAG Context / Agent Action] --> Inspector[Telemetry Ingestion]
    Inspector --> Core["GenParkAgentExfiltrationCanaryLeakDetector"]
    Core --> Detection[Cryptographic / Heuristic Analysis Engine]
    Detection --> Mitigation[Least-Privilege & Boundary Enforcement]
    Mitigation --> MCPOutput[MCP Result / Quarantine Signal / Merkle Seal]
```

---

## Quickstart & Usage

### 1. Direct Python Client Execution
```bash
python example_usage.py
```

### 2. Standalone MCP Server Launch
Run the local STDIO MCP server using the environment prepared above:
```bash
.venv/bin/python mcp_server.py
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
