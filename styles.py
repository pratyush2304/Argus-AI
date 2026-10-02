"""Design system for the Streamlit chat UI: tokens, Lucide icons, CSS, HTML snippets."""
import streamlit as st

_ICONS = {
    "zap": '<path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/>',
    "message": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "alert": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
}


def icon(name: str, size: int = 16) -> str:
    """Inline Lucide icon, stroke-width 1.75."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" '
        f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_ICONS[name]}</svg>'
    )


CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

:root {
  --bg: #09090b;
  --surface: rgba(255,255,255,.03);
  --surface-hover: rgba(255,255,255,.06);
  --surface-user: rgba(99,102,241,.09);
  --border: rgba(255,255,255,.10);
  --border-subtle: rgba(255,255,255,.06);
  --text: #fafafa;
  --text-2: #d4d4d8;
  --text-muted: #a1a1aa;
  --accent: #818cf8;
  --accent-strong: #6366f1;
  --danger: #f87171;
  --success: #4ade80;
  --s1: 4px; --s2: 8px; --s3: 12px; --s4: 16px; --s6: 24px; --s8: 32px;
  --r-control: 8px; --r-card: 12px; --r-panel: 16px;
  --ease: cubic-bezier(.2,.8,.2,1);
  --shadow-card: 0 1px 0 rgba(255,255,255,.04) inset, 0 8px 24px -12px rgba(0,0,0,.6);
}

/* ---------- Atmosphere ---------- */
.stApp { background: var(--bg); color: var(--text); font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif; }
.stApp::before {            /* ambient glows + fine grid */
  content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 0;
  background:
    radial-gradient(900px 520px at 62% -8%, rgba(99,102,241,.17), transparent 60%),
    radial-gradient(700px 420px at 6% 108%, rgba(56,189,248,.07), transparent 60%),
    linear-gradient(rgba(255,255,255,.028) 1px, transparent 1px) 0 0 / 32px 32px,
    linear-gradient(90deg, rgba(255,255,255,.028) 1px, transparent 1px) 0 0 / 32px 32px;
}
.stApp::after {             /* micro-noise */
  content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 0; opacity: .05;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
}
[data-testid="stAppViewContainer"], [data-testid="stMain"] { background: transparent; position: relative; z-index: 1; }
[data-testid="stHeader"] { background: transparent; }
.block-container { max-width: 760px; padding-top: var(--s8); padding-bottom: 160px; }
.stApp p, .stApp li, .stApp label, .stApp textarea, .stApp button, .stApp h1, .stApp h2, .stApp h3 {
  font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;
}
.stMarkdown p { line-height: 1.65; color: var(--text-2); font-size: 15px; }

/* ---------- Sidebar (glass) ---------- */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, rgba(24,24,27,.72), rgba(9,9,11,.6));
  -webkit-backdrop-filter: blur(12px); backdrop-filter: blur(12px);
  border-right: 1px solid var(--border);
  box-shadow: 8px 0 32px -16px rgba(0,0,0,.7);
}
[data-testid="stSidebar"] > div:first-child { background: transparent; }
.brand { display: flex; align-items: center; gap: var(--s3); margin-bottom: var(--s6); }
.badge { display: inline-flex; align-items: center; justify-content: center; width: 32px; height: 32px; flex: none;
  border-radius: var(--r-control); color: var(--accent);
  background: linear-gradient(180deg, rgba(129,140,248,.22), rgba(99,102,241,.08));
  border: 1px solid rgba(129,140,248,.3); box-shadow: 0 0 16px -4px rgba(99,102,241,.5); }
.badge.lg { width: 48px; height: 48px; border-radius: var(--r-card); }
.brand-name { font-size: 15px; font-weight: 600; color: var(--text); line-height: 1.2; }
.brand-sub { font-size: 12px; color: var(--text-muted); }
.label { font-size: 12px; font-weight: 500; color: var(--text-muted); margin: var(--s4) 0 var(--s2); }
.chip { display: inline-flex; align-items: center; gap: var(--s2); padding: var(--s1) var(--s3);
  border: 1px solid var(--border); background: rgba(255,255,255,.04); border-radius: 999px;
  font: 500 12px ui-monospace, SFMono-Regular, Menlo, monospace; color: var(--text-2);
  transition: border-color .2s var(--ease), background .2s var(--ease); max-width: 100%; }
.chip:hover { border-color: rgba(255,255,255,.2); background: rgba(255,255,255,.07); }
.dot { width: 6px; height: 6px; border-radius: 50%; background: var(--success); box-shadow: 0 0 8px rgba(74,222,128,.7); flex: none; }
.side-foot { font-size: 12px; color: var(--text-muted); margin-top: var(--s6); }

/* ---------- Header ---------- */
.app-header { display: flex; align-items: center; justify-content: space-between; gap: var(--s4); margin-bottom: var(--s6);
  padding-bottom: var(--s4); border-bottom: 1px solid var(--border-subtle); }
.app-title { font-size: 18px; font-weight: 600; letter-spacing: -.01em; color: var(--text); line-height: 1.3; }
.app-sub { font-size: 13px; color: var(--text-muted); }

/* ---------- Buttons ---------- */
.stButton > button {
  background: var(--surface-hover); color: var(--text-2); border: 1px solid var(--border);
  border-radius: var(--r-control); padding: var(--s2) var(--s4); min-height: 40px;
  font-size: 14px; font-weight: 500;
  transition: background .2s var(--ease), border-color .2s var(--ease), transform .15s var(--ease), box-shadow .2s var(--ease), color .2s var(--ease);
}
.stButton > button:hover { background: rgba(255,255,255,.1); border-color: rgba(255,255,255,.22); color: var(--text);
  transform: translateY(-1px); box-shadow: 0 6px 16px -6px rgba(0,0,0,.6); }
.stButton > button:active { transform: translateY(0) scale(.98); box-shadow: none; }
.stButton > button:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.stButton > button:disabled { opacity: .4; cursor: not-allowed; transform: none; box-shadow: none; }
[data-testid="stSidebar"] .stButton > button:hover:not(:disabled) { border-color: rgba(248,113,113,.45); color: #fecaca; background: rgba(248,113,113,.08); }

/* ---------- Messages ---------- */
[data-testid="stChatMessage"] {
  background: var(--surface); border: 1px solid var(--border-subtle); border-radius: var(--r-card);
  padding: var(--s4); gap: var(--s4); box-shadow: var(--shadow-card);
  animation: msg-in .28s var(--ease) both;
  transition: border-color .2s var(--ease), background .2s var(--ease);
}
[data-testid="stChatMessage"]:hover { border-color: var(--border); background: var(--surface-hover); }
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) { background: var(--surface-user); border-color: rgba(129,140,248,.18); }
[data-testid="stChatMessageAvatarUser"], [data-testid="stChatMessageAvatarAssistant"] {
  border-radius: var(--r-control); border: 1px solid var(--border); background: rgba(255,255,255,.06); color: var(--text-2);
}
[data-testid="stChatMessageAvatarAssistant"] { color: var(--accent); background: rgba(99,102,241,.14); border-color: rgba(129,140,248,.3); }
.meta { display: flex; align-items: center; gap: var(--s2); font-size: 12px; color: var(--text-muted); margin-bottom: var(--s1); }
.meta b { font-weight: 600; color: var(--text-2); }
[data-testid="stChatMessage"] pre { border: 1px solid var(--border-subtle); border-radius: var(--r-control); background: rgba(0,0,0,.35); }
@keyframes msg-in { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }

/* ---------- Empty + error states ---------- */
.state { display: flex; flex-direction: column; align-items: center; text-align: center; gap: var(--s3); padding: 48px var(--s4) var(--s6); }
.state h2 { font-size: 20px; font-weight: 600; margin: 0; color: var(--text); letter-spacing: -.01em; }
.state p { font-size: 14px; color: var(--text-muted); margin: 0; max-width: 420px; line-height: 1.6; }
.state.error { border: 1px solid rgba(248,113,113,.28); background: rgba(248,113,113,.05); border-radius: var(--r-panel); padding: var(--s6); margin: var(--s4) 0; }
.state.error .badge { color: var(--danger); background: rgba(248,113,113,.1); border-color: rgba(248,113,113,.3); box-shadow: none; }
.state.error p { color: var(--text-2); word-break: break-word; }

/* ---------- Command-bar input ---------- */
[data-testid="stBottom"], [data-testid="stBottom"] > div, [data-testid="stBottomBlockContainer"] { background: transparent; }
[data-testid="stBottom"]::before { content: ""; position: absolute; inset: -48px 0 0; pointer-events: none;
  background: linear-gradient(180deg, transparent, var(--bg) 70%); z-index: -1; }
[data-testid="stChatInput"] > div {
  background: rgba(24,24,27,.72); -webkit-backdrop-filter: blur(12px); backdrop-filter: blur(12px);
  border: 1px solid var(--border); border-radius: var(--r-panel);
  box-shadow: 0 8px 32px -8px rgba(0,0,0,.6), 0 1px 0 rgba(255,255,255,.05) inset;
  transition: border-color .2s var(--ease), box-shadow .25s var(--ease), transform .2s var(--ease);
}
[data-testid="stChatInput"] > div:hover { border-color: rgba(255,255,255,.2); }
[data-testid="stChatInput"] > div:focus-within {
  border-color: rgba(129,140,248,.65);
  box-shadow: 0 0 0 4px rgba(99,102,241,.2), 0 12px 40px -8px rgba(99,102,241,.35);
  transform: translateY(-1px);
}
[data-testid="stChatInput"] textarea { color: var(--text); font-size: 15px; caret-color: var(--accent); }
[data-testid="stChatInput"] textarea::placeholder { color: var(--text-muted); opacity: 1; }
[data-testid="stChatInputSubmitButton"] { border-radius: var(--r-control); background: var(--accent-strong); color: #fff;
  transition: transform .15s var(--ease), box-shadow .2s var(--ease), background .2s var(--ease); }
[data-testid="stChatInputSubmitButton"]:hover:not(:disabled) { background: #7c7ff5; box-shadow: 0 0 16px rgba(99,102,241,.55); transform: translateY(-1px); }
[data-testid="stChatInputSubmitButton"]:active:not(:disabled) { transform: scale(.94); }
[data-testid="stChatInputSubmitButton"]:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
[data-testid="stChatInputSubmitButton"]:disabled { background: rgba(255,255,255,.06); color: var(--text-muted); cursor: not-allowed; }

/* ---------- Scrollbar + motion ---------- */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,.14); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,.26); }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; }
}
</style>
"""


def inject() -> None:
    st.markdown(CSS, unsafe_allow_html=True)


def model_chip(model: str) -> str:
    return f'<span class="chip"><span class="dot"></span>{model}</span>'


def sidebar_brand() -> str:
    return (f'<div class="brand"><span class="badge">{icon("zap")}</span><div>'
            '<div class="brand-name">Argus AI</div><div class="brand-sub"></div></div></div>')


def header(model: str) -> str:
    return (f'<div class="app-header"><div style="display:flex;align-items:center;gap:12px">'
            f'<span class="badge">{icon("zap")}</span><div><div class="app-title">Argus AI</div>'
            f'<div class="app-sub">Streaming chat with conversation memory</div></div></div>{model_chip(model)}</div>')


def empty_state() -> str:
    return (f'<div class="state"><span class="badge lg">{icon("message", 22)}</span>'
            '<h2>Start a conversation</h2>'
            '<p>Ask a question or pick a suggestion below. Your conversation stays in memory until you clear it.</p></div>')


def error_state(message: str, hint: str = "Check your connection and API key, then try again.") -> str:
    return (f'<div class="state error" role="alert"><span class="badge">{icon("alert")}</span>'
            f'<h2>Something went wrong</h2><p>{message}</p><p>{hint}</p></div>')


def meta(role: str, time: str, model: str) -> str:
    who = "You" if role == "user" else "Assistant"
    extra = f'<span>{model}</span><span>·</span>' if role == "assistant" else ""
    return f'<div class="meta"><b>{who}</b>{extra}<span>{time}</span></div>'
