#pip install python-dotenv
#pip install langchain-openai
#pip install streamlit

#from dotenv import load_dotenv
#load_dotenv()

from langchain_openai import ChatOpenAI
chat_model=ChatOpenAI()

#subject = "AI"
#result = chat_model.invoke( subject + "에 대한 시를 써줘.")
#print(result.content)  # 실행 : python main.py

import streamlit as st # 웹 페이지를 자동 생성하고 생성된 웹페이지를 웹서버를 통해 제공하는 프레임워크
st.title("인공지능 시인") # 실행 : streamlit run main.py
subject=st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : "+ subject)

if st.button("시 작성"): # 눌렀을 때 true
    with st.spinner("시 작성 중.."):
        result = chat_model.invoke( subject + "에 대한 시를 써줘.")
        st.write(result.content)