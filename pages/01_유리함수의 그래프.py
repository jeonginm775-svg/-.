import streamlit as st
import sympy as sp
import random
import matplotlib.pyplot as plt
import numpy as np

st.title("📘 정수형 유리함수 교과서 생성기 (일반형 → 표준형 변환)")

# --- 1. 정수 조건을 만족하는 랜덤 생성 ---
def generate_integer_rational():
    while True:
        c = random.choice([1, 2, 3, -1, -2, -3])
        a = random.randint(-5, 5)
        q = random.randint(-5, 5)
        p = random.randint(-5, 5)
        A = random.randint(-5, 5)
        if A == 0 or c == 0:
            continue
        # 역변환: 표준형 → 일반형
        # y = A/(x - p) + q = (A + q(x - p)) / (x - p)
        # => y = (qx + (A - qp)) / (x - p)
        # 분모를 cx + d 형태로 만들기 위해 c 곱함
        d = -c * p
        b = (A - q * p) * c
        a = q * c
        if all(isinstance(v, int) for v in [a, b, c, d, p, q, A]):
            return a, b, c, d, p, q, A

a, b, c, d, p, q, A = generate_integer_rational()

x = sp.Symbol('x')
y_expr = (a*x + b) / (c*x + d)

# --- 2. 일반형 출력 ---
st.subheader("① 일반형 유리함수")
st.latex(rf"y = \frac{{{a}x + {b}}}{{{c}x + {d}}}")

# --- 3. 표준형으로 변환 과정 ---
st.subheader("② 표준형으로의 변환 과정")

st.markdown("**1단계:** 분모를 `c(x + d/c)` 형태로 바꿉니다.")
st.latex(rf"y = \frac{{{a}x + {b}}}{{{c}(x + {d/c:.0f})}}")

st.markdown("**2단계:** 분자를 분모의 형태로 맞춰 항등변형합니다.")
st.latex(rf"y = \frac{{a}}{{c}} + \frac{{ad - bc}}{{c^2(x + {d/c:.0f})}}")

st.markdown("**3단계:** `(x - p)` 형태로 바꾸고 정리합니다.")
st.latex(rf"y = \frac{{{A}}}{{x - ({p})}} + {q}")

# --- 4. 표준형 최종 결과 ---
st.subheader("③ 최종 표준형")
st.latex(rf"y = \frac{{{A}}}{{x - ({p})}} + {q}")

# --- 5. 그래프 그리기 ---
st.subheader("④ 그래프")

x_vals = np.linspace(p - 10, p + 10, 400)
y_vals = (a*x_vals + b) / (c*x_vals + d)

plt.figure()
plt.plot(x_vals, y_vals, label="유리함수", linewidth=2)
plt.axvline(p, color='r', linestyle='--', label=f'x = {p} (수직점근선)')
plt.axhline(q, color='g', linestyle='--', label=f'y = {q} (수평점근선)')
plt.title("유리함수 그래프 (정수형)")
plt.legend()
plt.ylim(q - 10, q + 10)
st.pyplot(plt)
