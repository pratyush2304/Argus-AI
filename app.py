from datetime import datetime
from html import escape

import streamlit as st

import styles
from bot_core import ChatEngine

st.set_page_config(
    page_title="Argus AI",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded",
)
styles.inject()

AVATARS = {"user": ":material/person:", "assistant": ":material/bolt:"}
SUGGESTIONS = [
    ("Explain a concept", "Explain how neural networks learn, in simple terms."),
    ("Help with math", "Walk me through solving a quadratic equation step by step."),
    ("Draft a message", "Help me write a polite follow-up email."),
]

# ---------- State ----------
if "chat_engine" not in st.session_state:
    try:
        st.session_state.chat_engine = ChatEngine()
    except ValueError as e:
        st.markdown(
            styles.error_state(escape(str(e)), "Add GROQ_API_KEY to your .env file, then reload this page."),
            unsafe_allow_html=True,
        )
        st.stop()
st.session_state.setdefault("messages", [])
st.session_state.setdefault("pending_prompt", None)
st.session_state.setdefault("error", None)

engine = st.session_state.chat_engine
messages = st.session_state.messages

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown(styles.sidebar_brand(), unsafe_allow_html=True)
    st.markdown('<div class="label">Model</div>' + styles.model_chip(engine.model), unsafe_allow_html=True)
    st.markdown('<div class="label">Conversation</div>', unsafe_allow_html=True)
    if st.button("Clear conversation", use_container_width=True,
                 icon=":material/delete:", disabled=not messages):
        engine.reset_chat()
        st.session_state.messages = []
        st.session_state.error = None
        st.rerun()
    st.markdown(f'<div class="side-foot">{len(messages)} messages in memory</div>', unsafe_allow_html=True)

# ---------- Input (resolved first so stale states clear before rendering) ----------
prompt = st.chat_input("Ask anything…")
if st.session_state.pending_prompt:
    prompt = st.session_state.pending_prompt
    st.session_state.pending_prompt = None
if prompt:
    st.session_state.error = None


def render_message(msg: dict) -> None:
    with st.chat_message(msg["role"], avatar=AVATARS[msg["role"]]):
        st.markdown(styles.meta(msg["role"], msg["time"], engine.model), unsafe_allow_html=True)
        st.markdown(msg["content"])


# ---------- Feed ----------
st.markdown(styles.header(engine.model), unsafe_allow_html=True)

if not messages and not prompt:
    st.markdown(styles.empty_state(), unsafe_allow_html=True)
    cols = st.columns(len(SUGGESTIONS))
    for col, (label, text) in zip(cols, SUGGESTIONS):
        if col.button(label, use_container_width=True, key=f"sugg-{label}"):
            st.session_state.pending_prompt = text
            st.rerun()

for msg in messages:
    render_message(msg)

if st.session_state.error and not prompt:
    err = st.session_state.error
    st.markdown(styles.error_state(escape(err["message"])), unsafe_allow_html=True)
    retry, dismiss, _ = st.columns([1, 1, 3])
    if retry.button("Retry", icon=":material/refresh:", use_container_width=True, key="retry"):
        if messages and messages[-1]["role"] == "user":
            messages.pop()
        st.session_state.pending_prompt = err["prompt"]
        st.session_state.error = None
        st.rerun()
    if dismiss.button("Dismiss", use_container_width=True, key="dismiss"):
        st.session_state.error = None
        st.rerun()

# ---------- Handle a new prompt ----------
if prompt:
    user_msg = {"role": "user", "content": prompt, "time": datetime.now().strftime("%H:%M")}
    messages.append(user_msg)
    render_message(user_msg)

    failed = None
    with st.chat_message("assistant", avatar=AVATARS["assistant"]):
        now = datetime.now().strftime("%H:%M")
        st.markdown(styles.meta("assistant", now, engine.model), unsafe_allow_html=True)
        placeholder = st.empty()
        full_response = ""
        try:
            for token in engine.send_message_stream(prompt):
                full_response += token
                placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)
            if full_response:
                messages.append({"role": "assistant", "content": full_response, "time": now})
        except Exception as e:  # noqa: BLE001
            failed = str(e)

    if failed is not None:
        st.session_state.error = {"message": failed, "prompt": prompt}
        st.rerun()
