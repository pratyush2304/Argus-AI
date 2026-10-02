# Groq chatbot — premium UI

Streamlit + Groq chatbot with a Linear/Raycast-style interface: spatial dark background, glass sidebar,
tonal message cards, floating command-bar input, designed empty and error states.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your GROQ_API_KEY
```

```bash
streamlit run app.py   # web UI
python cli.py          # terminal UI
```

## Files

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit UI (feed, sidebar, empty/error states) |
| `styles.py` | Design tokens, Lucide icons, all CSS, HTML snippets |
| `.streamlit/config.toml` | Native dark theme matching the tokens |
| `DESIGN.md` | Token palette, Tailwind equivalents, animation guidance |
| `bot_core.py`, `cli.py`, `config.py` | Unchanged |

Do not commit `.env`.
