# Resume

`index.html` is deployed at [https://sandrinedacol.github.io/resume/](https://sandrinedacol.github.io/resume/) (via GitHub Pages).

## Setup

Install dependencies and the Playwright browser:

```bash
uv sync
uv run playwright install chromium
```

## Update

1. Update `data.json`.

1. Run the script to regenerate a fully static `index.html`:
    ```bash
    uv run main.py
    ```