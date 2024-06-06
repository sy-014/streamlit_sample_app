import streamlit as st
import google.generativeai as genai
import os
import markdown


# Streamlitのタイトルと説明
st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by Google AI")

# Google Generative AI（Gemini API）のAPIキー設定
API_KEY=os.environ.get("TEST_API_KEY")
genai.configure(api_key=API_KEY)

# Geminiモデルの設定
model = genai.GenerativeModel('gemini-pro')

# チャット履歴を初期化する
if "messages" not in st.session_state:
	# 辞書形式で定義
    st.session_state["messages"] = []
	# 属性として定義
    # st.session_state.messages = []

# これまでのチャット履歴を全て表示する
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザーの入力が送信された際に実行される処理
if prompt := st.chat_input("What is up?"):

    # ユーザの入力を表示する
    with st.chat_message("user"):
        st.markdown(prompt)
    # ユーザの入力をチャット履歴に追加する
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # ChatBotの返答を表示する
    with st.chat_message("assistant"):
        st.markdown(response)
    # ChatBotの返答をチャット履歴に追加する
    st.session_state.messages.append({"role": "assistant", "content": response})
