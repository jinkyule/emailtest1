import streamlit as st
import json
import os

DATA_FILE = "posts.json"

# 저장된 게시글 불러오기
def load_posts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return []

# 게시글 저장하기
def save_posts(posts):
    with open(DATA_FILE, "w") as f:
        json.dump(posts, f)

st.title("Email 게시판")

posts = load_posts()

# 게시글 작성
new_email = st.text_input("새 이메일 입력")
if st.button("등록"):
    if new_email:
        posts.append(new_email)
        save_posts(posts)
        st.success("등록 완료!")

# 게시글 출력
st.subheader("등록된 이메일")
for email in posts:
    st.write(email)
