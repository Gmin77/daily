import streamlit as st
from pyparsing import empty
import datetime as dt

st.set_page_config(layout="wide")

LEFTGAP = 0.2
RIGHTGAP = 0.2

left, con1, right = st.columns([0.3, 0.7, 0.3])
left, con2, right = st.columns([0.35, 0.7, 0.5])
left, con3, right = st.columns([0.3, 0.7, 0.3])

def date():
    st.subheader(':date:일정확인')
    if st.button("일정추가", type = 'primary') :
            d = st.text_input("일정 날자를 입력하세요!")
            st.write('추가 일정 날짜:', d)
            work = st.text_input('일정을 추가하세요!', placeholder='Input Daily Work!')
            st.write('일정 추가:', work)

def add_daily() :
    pass
def main():

    with left : 
        empty()

    with con1 :
        st.title(':balloon: Daily Table')
        st.divider()
   
    with con2:
        date()

    with con3:
      pass
    
main()