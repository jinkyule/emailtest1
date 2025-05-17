import streamlit as st

st.title("📧 Site A - 이메일 게시판 (그대로 노출)")

st.write("이곳은 이메일을 보호하지 않고 그대로 노출합니다.")

emails = [
    "test@example.com",
    "hello@company.com",
    "user123@domain.net"
]

for email in emails:
    st.write(email)