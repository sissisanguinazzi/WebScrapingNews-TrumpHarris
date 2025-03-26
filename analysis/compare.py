import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st
from wordcloud import WordCloud
from analysis.preprocessing import preprocess_text


def compare_polarity(trump_polarities, harris_polarities):
    """
    Compare polarity distribution using a boxplot
    Parameters:
    - trump_polarities (list): List of polarity scores for Trump's articles
    - harris_polarities (list): List of polarity scores for Harris's articles
    Returns:
    - None: Displays the boxplot comparison using Streamlit
    """
    # Create a DataFrame with polarity data for both Trump and Harris
    data = pd.DataFrame({
        "Polarity": trump_polarities + harris_polarities,
        "Category": ["Trump"] * len(trump_polarities) + ["Harris"] * len(harris_polarities)
    })
    # Plot the boxplot
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="Category", y="Polarity", data=data, palette=["red", "blue"])
    plt.title("Polarity Distribution Comparison")
    st.pyplot(plt)


def compare_subjectivity(trump_subjectivities, harris_subjectivities):
    """
    Compare subjectivity scores using a Kernel Density Estimate (KDE) plot.
    Parameters:
    - trump_subjectivities (list): List of subjectivity scores for Trump's articles
    - harris_subjectivities (list): List of subjectivity scores for Harris's articles
    Returns:
    - None: Displays the KDE plot comparison using Streamlit
    """
    # Plot the KDE
    plt.figure(figsize=(8, 5))
    sns.kdeplot(trump_subjectivities, label="Trump", shade=True, color="red")
    sns.kdeplot(harris_subjectivities, label="Harris", shade=True, color="blue")
    plt.title("Subjectivity Distribution Comparison")
    plt.xlabel("Subjectivity Score")
    plt.legend()
    st.pyplot(plt)


def average_sentiment(trump_polarities, harris_polarities, trump_subjectivities, harris_subjectivities):
    """
    Compare average sentiment scores for polarity and subjectivity
    Parameters:
    - trump_polarities (list): List of polarity scores for Trump's articles
    - harris_polarities (list): List of polarity scores for Harris's articles
    - trump_subjectivities (list): List of subjectivity scores for Trump's articles
    - harris_subjectivities (list): List of subjectivity scores for Harris's articles
    Returns:
    - None: Displays the average sentiment bar chart using Streamlit
    """
    # Create a DataFrame with average sentiment scores for both Trump and Harris
    df = pd.DataFrame({
        "Category": ["Trump", "Harris"],
        "Avg Polarity": [sum(trump_polarities)/len(trump_polarities), sum(harris_polarities)/len(harris_polarities)],
        "Avg Subjectivity": [sum(trump_subjectivities)/len(trump_subjectivities), sum(harris_subjectivities)/len(harris_subjectivities)]
    })

    # Plot the bar chart
    df.set_index("Category").plot(kind="bar", figsize=(8, 5), colormap="coolwarm")
    plt.title("Average Polarity and Subjectivity")
    st.pyplot(plt)


def generate_wordcloud(text_data, title, base_color, highlight_color, highlight_words=None):
    """
    Generate a word cloud from text data with highlighting words unique to Harris and Trump
    Parameters:
    - text_data (list): List of text data (articles or sentences) to generate the word cloud
    - title (str): The title for the word cloud plot
    - base_color (str): The base color of the words in the word cloud
    - highlight_color (str): The color for words that are highlighted
    - highlight_words (list): List of words to highlight in the word cloud
    Returns:
    - fig (matplotlib.figure.Figure): The generated word cloud figure
    """
    # Function to highlight unique words
    def color_func(word, *args, **kwargs):
        return highlight_color if word in highlight_words else base_color

    # Generate the word cloud
    wordcloud = WordCloud(width=600, height=400, background_color="white", color_func=color_func, max_words=50).generate(" ".join(text_data))
 
    # Display the word cloud
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    ax.set_title(title)
    return fig


def get_unique_words(text_data1, text_data2):
    """
    Get unique words from two text datasets by comparing them
    Parameters:
    - text_data1 (list): The first dataset of text data
    - text_data2 (list): The second dataset of text data
    Returns:
    - unique_to_1 (set): Words that are unique to the first dataset
    - unique_to_2 (set): Words that are unique to the second dataset
    """
    # Split text data into words and create sets
    words1 = set(" ".join(text_data1).split())
    words2 = set(" ".join(text_data2).split())
    # Find words unique to each dataset
    unique_to_1 = words1 - words2
    unique_to_2 = words2 - words1
    return unique_to_1, unique_to_2


def display_comparisons(trump_polarities, harris_polarities, trump_subjectivities, harris_subjectivities, trump_texts, harris_texts):
    """
    Display all comparison visualizations (polarity, subjectivity, average sentiment, word clouds) in Streamlit
    Parameters:
    - trump_polarities (list), harris_polarities (list): Polarity scores for Trump and Harris
    - trump_subjectivities (list), harris_subjectivities (list): Subjectivity scores for Trump and Harris
    - trump_texts (list), harris_texts (list): Text data for Trump and Harris articles
    Returns:
    - None: Displays the comparison visualizations using Streamlit
    """
    st.header("Comparing Sentiment Between Trump and Harris Articles")
    
    # Polarity Comparison
    st.subheader("Polarity Comparison")
    compare_polarity(trump_polarities, harris_polarities)

    # Subjectivity Comparison
    st.subheader("Subjectivity Comparison")
    compare_subjectivity(trump_subjectivities, harris_subjectivities)

    # Average Sentiment Scores
    st.subheader("Average Sentiment Scores")
    average_sentiment(trump_polarities, harris_polarities, trump_subjectivities, harris_subjectivities)

    trump_texts = [preprocess_text(text) for text in trump_texts]
    harris_texts = [preprocess_text(text) for text in harris_texts]
    # Get unique words
    unique_to_trump, unique_to_harris = get_unique_words(trump_texts, harris_texts)

    # Create columns for side-by-side display
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Trump Word Cloud")
        trump_fig = generate_wordcloud(trump_texts, "Trump Word Cloud", "black", "red", highlight_words=unique_to_trump)
        st.pyplot(trump_fig)

    with col2:
        st.subheader("Harris Word Cloud")
        harris_fig = generate_wordcloud(harris_texts, "Harris Word Cloud", "black", "blue", highlight_words=unique_to_harris)
        st.pyplot(harris_fig)