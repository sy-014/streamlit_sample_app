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

if prompt:
    # ユーザー入力をセッション状態に追加
    st.session_state.messages.append({"role": "user", "content": prompt})

## OpenAIモデルをロードし、応答を取得する関数
def get_gemini_response(promt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(promt)
    return response.text

    # 応答をテキストとして取得（ここではresponse.textと仮定）
    assistant_response = response.text

    # 応答をセッション状態に追加し、表示
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    st.text(f"Assistant: {assistant_response}")


messages = [
  {"role":"system", "content": "Assistant is a large language model trained by OpenAI."},
  {"role":"user", "content":"本初子午線はいくつ？"}
  {"role":"assistant", "content":「本初子午線」とは、経度の基準となる子午線のことで、国際的にはグリニッジ子午線が本初子午線として採用されています。本初子午線の経度は0度です。これを基準に、東経と西経が決定され、経度180度の線が国際日付変更線となります。本初子午線は、イギリスのロンドン近郊のグリニッジ天文台を通っており、世界の時計（時刻）の標準である協定世界時（UTC）の基準ともなっています。}
  {"role":"user", "content":user_input}
]
