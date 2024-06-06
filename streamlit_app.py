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

# セッション状態にメッセージリストがない場合は初期化
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# 既存のメッセージを表示
for msg in st.session_state.messages:
    # ここではシンプルなテキスト表示を使用
    st.text(f"{msg['role']}: {msg['content']}")

# ユーザー入力の取得
prompt = st.text_input("Your message:")

user_msg = st.chat_input("ここにメッセージを入力")
if user_msg:
    # 以前のチャットログを表示
    for chat in st.session_state.chat_log:
        avator = avator_img_dict.get(chat["name"], None)
        with st.chat_message(chat["name"], avatar=avator):
            st.write(chat["msg"])

    # 最新のメッセージを表示
    assistant_msg = "もう一度入力してください"
    moriage_yaku_msg = "アンコール！アンコール！"
    with st.chat_message(USER_NAME):
        st.write(user_msg)
    with st.chat_message(ASSISTANT_NAME):
        st.write(assistant_msg)
    with st.chat_message(MORIAGE_YAKU_NAME, avatar=avator_img_dict[MORIAGE_YAKU_NAME]):
        st.write(moriage_yaku_msg)

    # セッションにチャットログを追加
    st.session_state.chat_log.append({"name": USER_NAME, "msg": user_msg})
    st.session_state.chat_log.append({"name": ASSISTANT_NAME, "msg": user_msg})
    st.session_state.chat_log.append({"name": MORIAGE_YAKU_NAME, "msg": user_msg})
