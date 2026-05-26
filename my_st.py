import streamlit as st  

# 타이틀 텍스트 출력
st.title('첫번째 웹 어플 만들기 😜👋📺')

'- 이것은 첫번째 줄 입니다. ㅋㅋㅋ'

st.metric("Temperature", "70 °F", "1.2 °F") 

'#### :orange[지표(Metric)]'
col1, col2, col3,col4 = st.columns(4) # 3개의 컬럼 생성
col1.metric("Temperature", "70 °F", "1.2 °F") 
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
col4.metric("내 심리상태", "20  °Mind", "-60 °Mind") 

st.divider()  # 👈 구분선

'# :blue[Streamlit 그래프]'
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns=["a", "b", "c"]
    )

'#### :orange[st.area_chart()]'
st.area_chart(chart_data)

'#### :orange[st.line_chart()]'
st.line_chart(chart_data)

'#### :orange[st.bar_chart()]'
st.bar_chart(chart_data)

'#### :orange[st.scatter_chart()]'
st.scatter_chart(chart_data)

'#### :orange[st.map()]'
df = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [37.55, 126.92],
    columns=["lat", "lon"],
)
st.map(df)

st.divider()  # 👈 구분선


'# :blue[시각화 라이브러리]'

'#### :orange[Matplotlib: st.pyplot()]'
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig) # 👈 차트 출력
