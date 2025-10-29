import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ⚙️ 페이지 기본 설정
st.set_page_config(page_title='이차함수 그래프 분석', layout='centered')

# 📝 제목
st.title('이차함수의 그래프 기본형 ($y=ax^2$) 분석하기 🧐')
st.markdown("""
$y=ax^2$ 그래프에서 **$a$ 값**을 변경하며 그래프의 모양과 폭이 어떻게 바뀌는지 직접 확인해 보세요.
""")

st.markdown('---')

# 🎚️ a 값 입력 (슬라이더)
# a=0인 경우를 제외하고 설정
a_value = st.slider(
    '**$a$ 값 선택하기** (a는 0이 될 수 없습니다)', 
    min_value=-5.0, 
    max_value=5.0,  
    value=1.0,      
    step=0.1
)

# ⚠️ a=0 처리 (이차함수 조건)
if abs(a_value) < 0.001:
    st.warning("경고: $a$ 값이 0에 매우 가깝습니다. 이차함수의 조건을 위해 $a=1.0$으로 설정됩니다.")
    a = 1.0
else:
    a = a_value

#
