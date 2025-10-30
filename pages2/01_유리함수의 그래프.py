import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="유리함수 교과서", layout="centered")

st.title("📘 유리함수 교과서 자동 생성기")
st.markdown("랜덤 유리함수를 보고, 직접 그래프를 분석해 보세요!")

# --- 1. 랜덤 유리함수 생성 ---
if 'a' not in st.session_state:
    st.session_state.a = random.randint(-5, 5)
    st.session_state.b = random.randint(-5, 5)
    st.session_state.c = random.randint(-5, 5)
    st.session_state.d = random.randint(-5, 5)

col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 새로운 유리함수 생성"):
        st.session_state.a = random.randint(-5, 5)
        st.session_state.b = random.randint(-5, 5)
        st.session_state.c = random.randint(-5, 5)
        st.session_state.d = random.randint(-5, 5)

a, b, c, d = st.session_state.a, st.session_state.b, st.session_state.c, st.session_state.d

st.subheader("랜덤으로 생성된 유리함수:")
st.latex(f"f(x) = \\frac{{{a}x + {b}}}{{{c}x + {d}}}")

# --- 2. 사용자 조정 ---
st.markdown("#### 그래프 조정")
col1, col2, col3 = st.columns(3)
user_a = col1.slider("a (분자 기울기)", -5, 5, a)
user_b = col2.slider("b (분자 절편)", -5, 5, b)
user_c = col3.slider("c (분모 기울기)", -5, 5, c)
user_d = st.slider("d (분모 절편)", -5, 5, d)

# --- 3. 그래프 그리기 ---
x = np.linspace(-10, 10, 1000)
# 분모가 0이 되는 점 제외
mask = (user_c * x + user_d) != 0
y = np.zeros_like(x)
y[mask] = (user_a * x[mask] + user_b) / (user_c * x[mask] + user_d)

fig, ax = plt.subplots()
ax.plot(x[mask], y[mask], label=f"f(x) = ({user_a}x+{user_b})/({user_c}x+{user_d})")
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_ylim(-10, 10)
ax.set_xlim(-10, 10)
ax.legend()
ax.grid(True)
st.pyplot(fig)

# --- 4. 요약 표시 ---
st.markdown("#### 📘 함수 분석 요약")
st.write(f"- 수직 점근선: x = {-user_d/user_c if user_c != 0 else '없음'}")
st.write(f"- 수평 점근선: y = {user_a/user_c if user_c != 0 else '없음'}")
