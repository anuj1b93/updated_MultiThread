import re
import string
from textblob import TextBlob

def to_lowercase(text):
    return text.lower()

def remove_html_tags(text):
    pattern = re.compile('<.*?>')
    return pattern.sub(r'', text)

def remove_url(text):
    pattern = re.compile(r'https?://\S+|www\.\S+')
    return pattern.sub(r'', text)

exclude = string.punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', exclude))

# Handle chat slang conversion
chat_words = {
    "AFAIK": "As Far As I Know", "AFK": "Away From Keyboard", "ASAP": "As Soon As Possible", 
    "FYI": "For Your Information", "BRB": "Be Right Back", "BTW": "By The Way", 
    "OMG": "Oh My God", "IMO": "In My Opinion", "LOL": "Laugh Out Loud", 
    "TTYL": "Talk To You Later", "GTG": "Got To Go", "IDK": "I Don't Know", 
    "TMI": "Too Much Information", "IMHO": "In My Humble Opinion", "ICYMI": "In Case You Missed It", 
    "FAQ": "Frequently Asked Questions", "TGIF": "Thank God It's Friday", "FYA": "For Your Action"
}

def chat_conversion(text):
    words = text.split()
    new_words = [chat_words.get(word.upper(), word) for word in words]
    return " ".join(new_words)

# Handle incorrect words 
def handle_incorrect_text(text):
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text

stopwords = set([
    "a", "an", "the", "is", "in", "at", "on", "of", "and", "or", "as", "by", "for", "to", "with"
])

def remove_stopwords(text):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stopwords]
    return " ".join(filtered_words)

def clean_text(text):
    text = to_lowercase(text)
    text = remove_html_tags(text)
    text = remove_url(text)
    text = remove_punctuation(text)
    text = chat_conversion(text)
    text = handle_incorrect_text(text)  
    text = remove_stopwords(text)
    return text