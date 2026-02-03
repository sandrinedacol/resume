# Resume

index.html is deployed on https://sandrinedacol.github.io/resume/ (see GitHub Pages)

Install dependencies + install playwright browser:
```bash
uv sync
uv run playwright install chromium
```

To update the resume:
1. Update data.json 
1. Run the script (generates a fully static index.html):
    ```bash
    uv run main.py
    ```
1. Wait for about 1 min