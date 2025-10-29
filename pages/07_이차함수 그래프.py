import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(page_title="이차함수의 그래프 기본형 (y=ax²) 분석하기", layout="centered")

# 제목
st.title("📈 이차함수의 그래프 기본형 (y=ax²) 분석하기")

st.markdown("""
이 앱에서는 이차함수 **y = ax²**의 그래프를 다양한 `a` 값에 대해 관찰하며  
- **a의 부호**에 따라 그래프가 위로 또는 아래로 볼록해지는지  
- **|a|의 크기**에 따라 그래프의 폭이 어떻게 달라지는지  
직접 확인해 볼 수 있습니다.
""")

# a 값 슬라이더
a = st.slider("a 값을 선택하세요", min_value=-5.0, max_value=5.0, value=1.0, step=0.1)

# x, y 데이터 생성
x = np.linspace(-5, 5, 200)
y = a * x**2

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label=f"y = {a}x²", linewidth=2)
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linew
