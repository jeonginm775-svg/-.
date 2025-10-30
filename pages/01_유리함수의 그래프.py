import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# --- 제목 ---
st.title("📘 유리함수 그래프 탐구 (슬라이드로 조절하기)")

# --- 변수 입력 (슬라이더) ---
st.sidebar.header("⚙️ 계수 조절하기")

a = st.sidebar.slider("a (분자 x 계수)", -10, 10, 2)
b = st.sidebar.slider("b (분자 상수항)", -10, 10, -3)
c = st.sidebar.slider("c (분모 x 계수)", -10, 10, 1)
d = st.sidebar.slider("d (분모 상수항)", -10, 10, 2)

# --- 유효성 검사 ---
if c == 0:
    st.warning("⚠️ 분모의 x계수 c는 0이 될 수 없습니다!")
else:
    x = sp.Symbol('x')
    y_expr = (a*x + b) / (c*x + d)

    # --- 1. 일반형 출력 ---
    st.subheader("① 일반형")
    st.latex(rf"y = \frac{{{a}x + {b}}}{{{c}x + {d}}}")

    # --- 2. 표준형으로 변환 ---
    # 변환식: y = (a/c) + (ad - bc) / [c^2 (x + d/c)]
    A = (a*d - b*c) // (c**2) if (a*d - b*c) % (c**2) == 0 else (a*d - b*c) / (c**2)
    p = -d / c
    q = a / c

    st.subheader("② 표준형으로 변환 과정")
    st.markdown("**1단계:** 분모를 `c(x + d/c)` 형태로 묶습니다.")
    st.latex(rf"y = \frac{{{a}x + {b}}}{{{c}(x + {d/c:.2f})}}")

    st.markdown("**2단계:** 분자를 분모의 형태로 나누어 항등변형합니다.")
    st.latex(rf"y = \frac{{a}}{{c}} + \frac{{ad - bc}}{{c^2(x + {d/c:.2f})}}")

    st.markdown("**3단계:** `(x - p)` 형태로 바꿔 표준형으로 정리합니다.")
    st.latex(rf"y = \frac{{{A}}}{{x - ({p:.2f})}} + {q:.2f}")

    st.subheader("③ 최종 표준형")
    st.latex(rf"y = \frac{{{A}}}{{x - ({p:.2f})}} + {q:.2f}")

    # --- 3. 그래프 그리기 ---
    st.subheader("④ 그래프")
    x_vals = np.linspace(p - 10, p + 10, 400)
    y_vals = (a*x_vals + b) / (c*x_vals + d)

    plt.figure()
    plt.plot(x_vals, y_vals, label="유리함수", linewidth=2)
    plt.axvline(p, color='r', linestyle='--', label=f'x = {p:.2f} (수직점근선)')
    plt.axhline(q, color='g', linestyle='--', label=f'y = {q:.2f} (수평점근선)')
    plt.ylim(q - 10, q + 10)
    plt.legend()
    plt.title(f"y = ({a}x + {b}) / ({c}x + {d})")
    st.pyplot(plt)

    # --- 4. 점근선과 y절편 정보 ---
    st.subheader("⑤ 그래프의 주요 특징")

    y_intercept = (a*0 + b) / (c*0 + d) if d != 0 else "정의되지 않음"
    st.markdown(f"**수직 점근선:** x = {p:.2f}")
    st.markdown(f"**수평 점근선:** y = {q:.2f}")
    st.markdown(f"**y절편:** {y_intercept}")

