import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')

STOPWORDS = set(stopwords.words("english"))

# add custom stopwords 
CUSTOM_STOPWORDS = {"fullscreen", "image", "ago" , "cet", "US", "said", "view"}

NUMBERS_AS_WORDS = {
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety", "hundred", "thousand", "million", "billion"
}
STOPWORDS.update(word.lower() for word in CUSTOM_STOPWORDS)
STOPWORDS.update(NUMBERS_AS_WORDS)
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """Lowercase text, remove special characters"""
    text = text.lower()
    text = text.replace("’", "'")  # Normalize curly quotes
    text = re.sub(r"\b(\w+)'s\b", r"\1", text)  # Remove possessive 's'
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def remove_stopwords(text):
    """Remove predefined and custom stopwords."""
    words = text.split()
    filtered_words = [word for word in words if word not in STOPWORDS and len(word) > 1]
    return " ".join(filtered_words)

def lemmatize_text(text):
    """Lemmatize words in the text."""
    words = text.split()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return " ".join(lemmatized_words)

def preprocess_text(text):
    """Apply all preprocessing steps in the correct order."""
    text = clean_text(text)
    text = remove_stopwords(text)
    text = lemmatize_text(text)
    return text if text else None