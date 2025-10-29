import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 페이지 기본 설정
st.set_page_config(page_title="이차함수의 그래프 기본형 (y=ax^2) 분석하기", layout="centered")

# 제목
st.title("이차함수의 그래프 기본형 (y = ax^2) 분석하기")

# 소개 문단
st.write("""
이 앱에서는 이차함수 **y = ax²**의 그래프를 다양한 `a` 값에 대해 관찰합니다.  
이를 통해 다음과 같은 사실을 스스로 탐구해 볼 수 있습니다.

1. `a`가 양수일 때와 음수일 때 그래프의 모양이 어떻게 달라지는가?  
2. `|a|`의 크기에 따라 그래프의 폭(넓이)이 어떻게 변하는가?
""")

# a 값 슬라이더
a = st.slider("a 값을 선택하세요", min_value=-5.0, max_value=5.0, value=1.0, step=0.1)

# x, y 데이터 생성
x = np.linspace(-5, 5, 300)
y = a * x**2

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, color="blue", label=f"y = {a}x²", linewidth=2)
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("y", fontsize=12)
ax.set_title(f"a = {a}", fontsize=14)
ax.legend()
ax.grid(True)

# 그래프 표시
st.pyplot(fig)

# 탐구 유도 문단
st.markdown("---")
st.subheader("그래프를 관찰하며 생각해보기")

st.write("""
- 그래프가 **위로 볼록한가, 아래로 볼록한가?**  
  → `a`의 부호(양수/음수)에 따라 그래프의 방향이 어떻게 달라지나요?

- 그래프의 **폭(넓이)**은 어떻게 변하나요?  
  → `|a|`의 크기가 커질수록 그래프가 **가파르게** 되는가, **완만하게** 되는가?

이 관찰을 통해 이차함수의 기본형 그래프와 계수 `a`의 관계를 스스로 발견할 수 있습니다.
""")

