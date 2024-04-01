import streamlit as st
import datetime as dt
import csv
import pandas as pd

st.set_page_config(layout="centered")

# CSV 파일 경로
file_path = 'daily.csv'

# 현재 날짜
now = dt.datetime.now()

def add_daily(write_day, add_time,add_work):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([write_day, add_time ,add_work])

def day_list():
    daily = []

    # 7일간의 날짜 생성
    for i in range(7):
        day = now + dt.timedelta(days=i)
        write_day = day.strftime('%y-%m-%d')
        daily.append(write_day)

    add_date = st.date_input(label = '원하시는 날짜를 선택해주세요!')
    add_time = st.time_input('원하시는 시간을 선택해주세요!', value=None)
    add_work = st.text_input(label = ':calendar: 일정을 추가해주세요!', placeholder='Ex) Study', max_chars=255)
    add_button = st.button(label="일정추가", type='primary')
    if add_button :
        add_daily(add_date, add_time, add_work)
        st.write('추가된 일정 :', add_work) 

def db_frame() :
    data = pd.read_csv('daily.csv', encoding='cp949')
    data.columns =['Date', 'Time', 'Work']
    frame = pd.DataFrame(data)
    frame

def main():
    st.title(':balloon: 일정추가')
    st.divider()
    day_list()
    db_frame()


if __name__ == "__main__":
    main()
