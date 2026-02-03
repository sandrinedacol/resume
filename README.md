# Resume

The `index.html` file is live at [https://sandrinedacol.github.io/resume/](https://sandrinedacol.github.io/resume/) (via GitHub Pages).

## Setup

Install dependencies and the Playwright browser:

```bash
uv sync
uv run playwright install chromium
```

## Updating the Resume

1. Update `data.json`.

2. Run the script to regenerate a fully static `index.html`:
    ```bash
    uv run main.py
    ```

1. Wait ~1 minute for the process to complete.