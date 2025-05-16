import streamlit as st

st.title("Site A - 크롤링 가능한 이메일 게시판")

if "posts" not in st.session_state:
    st.session_state["posts"] = []

email = st.text_input("이메일 입력")
message = st.text_input("메시지 입력")

if st.button("게시"):
    post = f"이메일: {email} / 메시지: {message}"
    st.session_state["posts"].append(post)

st.subheader("📢 게시글 목록")
for post in st.session_state["posts"]:
    st.write(post)