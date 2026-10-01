# Warzone Atlas V2

A free, read-only Last War: Survival intelligence dashboard.

## Data source
This version is wired for LastIntel's public read-only API/MCP. It does not ask for game credentials.

## Run
1. Install Python 3.10+.
2. `pip install -r requirements.txt`
3. `python app.py`
4. Open http://127.0.0.1:8000

The server proxies search requests so the browser does not need to know the upstream endpoint.

## Notes
- The LastIntel public service currently documents anonymous read access.
- Keep requests cached and respect upstream limits.
- Do not add credential capture, reverse engineering, or automated game access.

## Phone-only deployment

You do not need a PC. Put this folder in a GitHub repository from your phone, then connect the repository to Render and choose the Free web service plan. Render supports Flask deployment from Git repositories and provides a public HTTPS URL.

Render settings if entered manually:
- Runtime: Python 3
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
