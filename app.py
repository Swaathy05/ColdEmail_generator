import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# Function to add custom CSS for background image
def add_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://wallpaperaccess.com/full/5584502.png"); /* Replace this with your image URL */
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;  /* Ensure it takes the full height */
            width: 100%;     /* Ensure it takes the full width */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/?jobSearch=true&jsOffset=0&jsSort=posting_start_date&jsLanguage=en")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":    
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    
    add_background_image()  # Call to apply background image
    create_streamlit_app(chain, portfolio, clean_text)
