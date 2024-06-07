import streamlit as st
import google.generativeai as genai
import os

# Streamlitのタイトルと説明
st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by Google AI")

# Google Generative AI（Gemini API）のAPIキー設定
API_KEY=os.environ.get("TEST_API_KEY")
genai.configure(api_key=API_KEY)

# Geminiモデルの設定
model = genai.GenerativeModel('gemini-pro')

# セッション状態にメッセージリストがない場合は初期化
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "Assistant", "content": "How can I help you?"}]

# 既存のメッセージを表示
for msg in st.session_state.messages:
    # ここではシンプルなテキスト表示を使用
    st.text(f"{msg['role']}: {msg['content']}")

# ユーザー入力の取得
prompt = st.text_input("Your message:")

