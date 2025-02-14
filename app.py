import streamlit as st
import google.generativeai as ai

ai.configure(api_key="Enter Your API Key here")

sys_prompt = """You are a helpful Python Code Reviewer. 
You can resovle, review and give feedbacks on potential bugs along with suggessions for fixes.
In case if someone ask queries which are not relevant to Python or Python Code, politely tell them to ask relevant queries only."""

gemini_model = ai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=sys_prompt)

st.title("Code Reviewer")

user_input = st.text_input(label="Enter your query/issue")

btn_click = st.button("Check Here")

if btn_click == True:
    response = gemini_model.generate_content(user_input)
    st.write(response.text)
