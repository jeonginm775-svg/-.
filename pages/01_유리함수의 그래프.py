import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="유리함수 교과서 (정수 일반형 → 표준형 변환)", layout="centered")

st.title("📘 유리함수 교과서: 정수 일반형 → 표준형 변환")
st.markdown("모든 계수가 정수인 일반형 유리함수를 표준형으로 변환하는 과정을 단계별로 확인해보세요!")

# --------------------------
# 1️⃣ 정수 조건을 만족하는 일반형 생성
# --------------------------
def generate_integer_rational():
    c = random.choice([i for i in range(-5, 6) if i not in [0]])
    h = random.randint(-5, 5)
    k = random.randint(-5, 5)
    A = random.randint(-5, 5)

    d = -c * h
    a = c * k
    # bc - ad = A * c^2 → b = (A*c^2 + a*d) / c
    b = (A * c**2 + a * d) // c if (A * c**2 + a * d) % c == 0 else None

    # b가 정수로 딱 떨어질 때까지 반복
    while b is None:
        c = random.choice([i for i in range(-5, 6) if i not in [0]])
        h = random.randint(-5, 5)
        k = random.randint(-5, 5)
        A = random.randint(-5, 5)
        d = -c * h
        a = c * k
        if (A * c**2 + a * d) % c == 0:
            b = (A * c**2 + a * d) // c

    return a, b, c, d, A, h, k

# --------------------------
# 2️⃣ 세션 상태로 저장
# --------------------------
if "coeffs" not in st.session_state:
    st.session_state.coeffs = generate_integer_rational()

if st.button("🔄 새로운 유리함수 생성"):
    st.session_state.coeffs = generate_integer_rational()

a, b, c, d, A, h, k = st.session_state.coeffs

# --------------------------
# 3️⃣ 일반형 표시
# --------------------------
st.subheader("① 일반형 (General Form)")
st.latex(f"f(x) = \\frac{{{a}x + ({b})}}{{{c}x + ({d})}}")

# --------------------------
# 4️⃣ 표준형으로의 변환 과정
# --------------------------
st.subheader("② 표준형으로의 변환 과정")

st.markdown("일반형에서 표준형으로 변환하는 과정을 단계별로 보겠습니다:")

st.latex(r"""
\begin{align*}
f(x) &= \frac{ax + b}{cx + d} \\[4pt]
     &= \frac{a}{c} + \frac{bc - ad}{c(cx + d)} \\[4pt]
     &= \frac{a}{c} + \frac{bc - ad}{c^2\left(x + \frac{d}{c}\right)} \\[4pt]
     &= \frac{A}{x - h} + k
\end{align*}
""")

st.markdown("정수 조건을 이용하여 계산하면:")

st.latex(f"h = -\\frac{{d}}{{c}} = {h}")
st.latex(f"k = \\frac{{a}}{{c}} = {k}")
st.latex(f"A = \\frac{{bc - ad}}{{c^2}} = {A}")

st.markdown("따라서 표준형은 다음과 같습니다:")
st.latex(f"f(x) = \\frac{{{A}}}{{x - ({h})}} + {k}")

# --------------------------
# 5️⃣ 그래프 그리기
# --------------------------
x = np.linspace(-10, 10, 2000)
mask = (c * x + d) != 0
y = np.zeros_like(x)
y[mask] = (a * x[mask] + b) / (c * x[mask] + d)

fig, ax = plt.subplots()
ax.plot(x[mask], y[mask], label=f"f(x) = ({a}x+{b})/({c}x+{d})")
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.axvline(h, color='blue', linestyle='--', label=f"수직 점근선 x={h}")
ax.axhline(k, color='red', linestyle='--', label=f"수평 점근선 y={k}")

# y절편 표시
if (c * 0 + d) != 0:
    y0 = (a * 0 + b) / (c * 0 + d)
    ax.scatter(0, y0, color='green', s=60, zorder=5, label=f"y절편 = {int(y0)}" if y0.is_integer() else f"y절편 = {y0:.2f}")

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.legend()
ax.grid(True)
st.pyplot(fig)

# --------------------------
# 6️⃣ 요약
# --------------------------
st.markdown("#### 📘 함수의 특징 요약")
st.write(f"- **수직 점근선:** x = {h}")
st.write(f"- **수평 점근선:** y = {k}")
if (c * 0 + d) != 0:
    st.write(f"- **y절편:** (0, {round(y0, 2)})")

st.divider()
st.markdown("🧩 **요약:**")
st.markdown(f"""
- 일반형 계수: a = {a}, b = {b}, c = {c}, d = {d}  
- 표준형 계수: A = {A}, h = {h}, k = {k}  
""")
