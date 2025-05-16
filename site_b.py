import streamlit as st
import re
import base64

st.title("Site B - AI 기반 이메일 난독화 게시판")

if "posts" not in st.session_state:
    st.session_state["posts"] = []

def obfuscate(text):
    # 이메일을 base64로 인코딩하여 난독화 처리
    return re.sub(
        r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})",
        lambda m: f"[보호됨: {base64.b64encode(m.group().encode()).decode()}]",
        text
    )

email = st.text_input("이메일 입력")
message = st.text_input("메시지 입력")

if st.button("게시"):
    protected_email = obfuscate(email)
    protected_message = obfuscate(message)
    post = f"이메일: {protected_email} / 메시지: {protected_message}"
    st.session_state["posts"].append(post)

st.subheader("📢 게시글 목록")
for post in st.session_state["posts"]:
    st.write(post)