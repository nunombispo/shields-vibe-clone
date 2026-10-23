# shields-vibe-clone

Companion code for:
[I Vibe-Coded a Shields.io Clone — Then I Wouldn't Ship It](https://developer-service.blog/)

Happy-path stub only: one FastAPI route, fake widths, tiny color map. Demo, not a public badge CDN.

## Run

```bash
uv sync
uv run uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/badge/build-passing-green
```

## Harden before you expose it

See the article for path parsing, colors, font metrics, caching, and abuse.
