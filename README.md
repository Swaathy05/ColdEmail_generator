# Cold Email Generator

📧 **Cold Email Generator** is a Streamlit application designed to assist job seekers in generating personalized cold emails to potential employers. By extracting job details from specified URLs and leveraging a portfolio of skills, this app automates the email writing process.

## Features

- **URL Input**: Enter a URL from job listings to fetch job details.
- **Skill Extraction**: Automatically extracts required skills for each job.
- **Personalized Email Generation**: Generates tailored cold emails for job applications based on extracted data and user portfolio.
- **User-Friendly Interface**: Built using Streamlit for a seamless user experience.

## Technologies Used

- **Python**: The programming language for developing the application.
- **Streamlit**: For creating the web app interface.
- **LangChain Community**: For document loading and language model interactions.
- **ChromaDB**: For handling and querying portfolio data.
- **BeautifulSoup**: For parsing HTML content from web pages.

## Installation

To run the Cold Email Generator locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/cold-email-generator.git
   cd cold-email-generator
   

Make sure you have Python installed, then install the required packages using pip:

        pip install streamlit langchain-community langchain-groq chromadb beautifulsoup4

## Usage:

Enter Job URL:
Input the job listing URL in the provided text field and click "Submit".
View Generated Emails:
The application will process the data and display personalized cold emails for the jobs listed on the provided URL.

## Acknowledgements
Streamlit for the easy-to-use web application framework.
LangChain for enabling LLM functionalities.
ChromaDB for managing portfolio data.
