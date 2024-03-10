import pandas
from openai import OpenAI
import streamlit as st

def process_question(text_question):

    APIKEY = st.secrets['OPENAI']['APIKEY']
    client = OpenAI(api_key=APIKEY)

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {
      "role": "system",
      "content": "You are an intelligent AI model"
    },
    {
      "role": "user",
      "content": text_question
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
    )

    answer = response.choices[0].message.content
    st.write(answer)
