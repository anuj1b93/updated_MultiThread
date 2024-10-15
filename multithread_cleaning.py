import threading
from cleaned_text import clean_text

def clean_text_multithreaded(texts):
    cleaned_texts = []
    threads = []
    
    def worker(text):
        cleaned_texts.append(clean_text(text))
    
    for text in texts:
        thread = threading.Thread(target=worker, args=(text,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return cleaned_texts

# cleaned_corpus = clean_text_multithreaded(cleaned_texts)
