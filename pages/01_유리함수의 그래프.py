import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="유리함수 교과서", layout="centered")

st.title("📘 정수 점근선·절편 유리함수 교과서")
st.markdown("랜덤으로 생성된 유리함수를 보고 그래프를 탐구해보세요!")

# --------------------------
# 1️⃣ 유리함수 생성 함수
# --------------------------
def generate_rational():
    c = random.choice([i for i in range(-5, 6) if i != 0])  # 0 제외
    k = random.randint(-5, 5)  # 수직점근선 x = k
    m = random.randint(-5, 5)  # 수평점근선 y = m
    n = random.randint(-5, 5)  # y절편 = n

    a = c * m
    d = -c * k
    b = d * n
    return a, b, c, d, k, m, n

# --------------------------
# 2️⃣ 세션 상태로 저장
# --------------------------
if "coeffs" not in st.session_state:
    st.session_state.coeffs = generate_rational()

if st.button("🔄 새로운 유리함수 생성"):
    st.session_state.coeffs = generate_rational()

a, b, c, d, k, m, n = st.session_state.coeffs

st.subheader("랜덤으로 생성된 유리함수")
st.latex(f"f(x) = \\frac{{{a}x + {b}}}{{{c}x + {d}}}")

# --------------------------
# 3️⃣ 그래프 영역
# --------------------------
x = np.linspace(-10, 10, 2000)
mask = (c * x + d) != 0
y = np.zeros_like(x)
y[mask] = (a * x[mask] + b) / (c * x[mask] + d)

fig, ax = plt.subplots()
ax.plot(x[mask], y[mask], label=f"f(x) = ({a}x+{b})/({c}x+{d})")
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.axhline(m, color='red', linestyle='--', label=f"수평점근선 y={m}")
ax.axvline(k, color='blue', linestyle='--', label=f"수직점근선 x={k}")
ax.scatter(0, n, color='green', s=60, zorder=5, label=f"y절편 = {n}")
ax.set_ylim(-10, 10)
ax.set_xlim(-10, 10)
ax.legend()
ax.grid(True)
st.pyplot(fig)

# --------------------------
# 4️⃣ 요약
# --------------------------
st.markdown("#### 📘 함수의 성질 요약")
st.write(f"- **수직 점근선:** x = {k}")
st.write(f"- **수평 점근선:** y = {m}")
st.write(f"- **y절편:** (0, {n})")
