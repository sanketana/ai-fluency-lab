# ============================================================================
#   THE ENGINE — you do NOT need to edit this file.
#
#   This is the same for every student. It reads your settings from
#   bot_config.py, connects to Google's Gemini AI, and runs the chat window.
#
#   Want to change how your bot behaves? Edit bot_config.py, not this file.
# ============================================================================

import os

import streamlit as st
from google import genai
from google.genai import types

import bot_config as bot


# ---------- Page setup ----------
st.set_page_config(page_title=bot.BOT_NAME, page_icon=bot.BOT_ICON)


# ---------- Find the secret API key ----------
# The key works both on Streamlit Cloud (Secrets) and on a local computer
# (an environment variable). The key is NEVER written in the code.
def get_api_key():
    try:
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass
    return os.environ.get("GEMINI_API_KEY")


API_KEY = get_api_key()
if not API_KEY:
    st.error(
        "🔑 No API key found.\n\n"
        "Add a secret named **GEMINI_API_KEY** in your Streamlit app settings "
        "(Settings → Secrets), then reboot the app."
    )
    st.stop()


# ---------- Connect to the AI ----------
@st.cache_resource
def make_client(api_key):
    return genai.Client(api_key=api_key)


client = make_client(API_KEY)


# ---------- Start a fresh chat (only the first time) ----------
def new_chat():
    return client.chats.create(
        model=bot.MODEL,
        config=types.GenerateContentConfig(
            system_instruction=bot.SYSTEM_PROMPT,
        ),
    )


if "chat" not in st.session_state:
    st.session_state.chat = new_chat()
    st.session_state.messages = []  # what we show on screen


# ---------- Sidebar ----------
with st.sidebar:
    st.header(f"{bot.BOT_ICON} {bot.BOT_NAME}")
    st.write(bot.BOT_TAGLINE)
    st.divider()
    if st.button("🔄 Start over"):
        st.session_state.chat = new_chat()
        st.session_state.messages = []
        st.rerun()
    st.caption("Made in AI Fluency Lab · powered by Google Gemini")


# ---------- Main chat area ----------
st.title(f"{bot.BOT_ICON} {bot.BOT_NAME}")
st.caption(bot.BOT_TAGLINE)


def ask_bot(user_text):
    """Send the user's message to the AI and show the reply."""
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)
    with st.chat_message("assistant", avatar=bot.BOT_ICON):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat.send_message(user_text)
                reply = response.text
            except Exception as error:
                reply = f"⚠️ Something went wrong talking to the AI:\n\n`{error}`"
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})


# Greeting + suggested questions (only before the conversation starts)
if not st.session_state.messages:
    with st.chat_message("assistant", avatar=bot.BOT_ICON):
        st.markdown(bot.BOT_GREETING)

    if bot.SUGGESTED_QUESTIONS:
        st.write("**Try asking:**")
        cols = st.columns(len(bot.SUGGESTED_QUESTIONS))
        for col, question in zip(cols, bot.SUGGESTED_QUESTIONS):
            if col.button(question):
                ask_bot(question)
                st.rerun()

# Show the conversation so far
for message in st.session_state.messages:
    avatar = bot.BOT_ICON if message["role"] == "assistant" else None
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# The text box at the bottom
prompt = st.chat_input(f"Message {bot.BOT_NAME}...")
if prompt:
    ask_bot(prompt)
    st.rerun()
