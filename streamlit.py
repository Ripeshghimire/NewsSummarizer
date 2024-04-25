import streamlit as st 
from transformers import pipeline 
st.title("News Summarization ")
user_input = st.text_input("Enter the text to summarize ",key = 'text')
text_generator =pipeline("summarization",model="Ripesh08/news_summarization")
generated_text = text_generator(user_input)
# Generate summary based on user input
if st.button("Summarize"):
    generated_text = text_generator(user_input, max_length=150, min_length=40, do_sample=False)[0]
    # Display the generated summary
    st.write("Generated Summary:")
    st.write(generated_text['summary_text'])