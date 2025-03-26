from analysis.preprocessing import clean_text, remove_stopwords,lemmatize_text,preprocess_text

def test_clean_text():
    assert clean_text("Donald's dog") == "donald dog"
    assert clean_text("hello! what's up?") == "hello what up"

def test_remove_stopwords():
    assert remove_stopwords("walk the dog") == "walk dog"  # "the" is a stopword
    assert remove_stopwords("walk s dog") == "walk dog"  # "s" is a stopword here
    assert remove_stopwords("U s dog") == "dog"  # "s" is a stopword here
    assert remove_stopwords("I am walking the dog") == "walking dog"  # "I", "am", "the" are stopwords

def test_lemmatize_text():
    assert lemmatize_text("walking dog") == "walking dog"  
    assert lemmatize_text("walks dog") == "walk dog"  

    
def test_preprocess_text():
    assert preprocess_text("walk the dog") == "walk dog"  # "the" is a stopword
    assert preprocess_text("walk s dog") == "walk dog"  # "s" is a stopword here
    assert preprocess_text("Donald's dog") == "donald dog"  # possessive 's' removed
    assert preprocess_text("I'm running faster") == "im running faster"  # lemmatization works on "running"
    assert preprocess_text("These are just some tests!") == "test" 
    assert preprocess_text(" donald u") == "donald" 
    assert preprocess_text("s") is None
    assert preprocess_text("ago cet") is None
    assert preprocess_text("US's") is None