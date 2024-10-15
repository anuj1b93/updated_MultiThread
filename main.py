import asyncio
from async_fetcher import fetch_and_parse
from multithread_cleaning import clean_text_multithreaded
from fine_tuner import fine_tune_model

def main():
    urls = [
        'https://www.thehindubusinessline.com',
        'https://bhaskarlive.in/india-to-make-digital-connectivity-affordable-for-emerging-economies-piyush-goyal/',
        'https://timesofindia.indiatimes.com/business/india-business'
    ]
    raw_html_texts = fetch_and_parse(urls)
    print("Fetched and parsed (from asynch_fetcher module) HTML content.")

    cleaned_texts = clean_text_multithreaded(raw_html_texts)
    print("Cleaned text data.")

    fine_tune_model(cleaned_texts)
    print("Fine-tuned the LLM with the cleaned text data.")

if __name__ == "__main__":
    asyncio.run(main())
