import streamlit as st
import google.generativeai as genai
import os
import dotenv

# Streamlitのタイトルと説明
st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by Google AI")

# .envファイルから環境変数を読み込む
dotenv.load_dotenv()

def configure_api():
# Google Generative AI（Gemini API）のAPIキー設定
API_KEY = os.getenv("TEST_API_KEY")
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

if prompt:
    # ユーザー入力をセッション状態に追加
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Gemini APIを使って応答を生成
    response = model.generate_content(prompt)

    # 応答をテキストとして取得（ここではresponse.textと仮定）
    assistant_response = response.text

    # 応答をセッション状態に追加し、表示
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    st.text(f"Assistant: {assistant_response}")
