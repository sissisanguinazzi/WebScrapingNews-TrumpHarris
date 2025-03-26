from harris.main_harris import articles_harris
from trump.main_trump import articles_trump
from analysis.plots import plot_sentiment_histograms, plot_sentiment_table, plot_word_cloud
from analysis.compare import display_comparisons
import streamlit as st
import pandas as pd
from analysis.preprocessing import preprocess_text

# Streamlit UI
st.title("Sentiment Analysis Dashboard")

# Sidebar navigation
st.sidebar.title("Select Analysis")
page = st.sidebar.radio("Go to", ["Trump", "Harris", "Comparison"])

# Page selection
if page == "Trump":
    st.write("Analyzing Trump articles...")
    # Convert the Trump articles data into a DataFrame
    selected_df = pd.DataFrame(articles_trump)

elif page == "Harris":
    st.write("Analyzing Harris articles...")
    # Convert the Harris articles data into a DataFrame
    selected_df = pd.DataFrame(articles_harris)

elif page == "Comparison":
    st.write("Comparing Trump and Harris articles...")

    # # Call the comparison function
    display_comparisons(
        [article["polarity"] for article in articles_trump],
        [article["polarity"] for article in articles_harris],
        [article["subjectivity"] for article in articles_trump],
        [article["subjectivity"] for article in articles_harris],
        [article["content"] for article in articles_trump],
        [article["content"] for article in articles_harris]
    )

# Call functions from the analysis file
if page in ["Trump", "Harris"]:
    st.header(f"{page} Articles")
    
    st.subheader("Word Cloud")
    plot_word_cloud(selected_df["content"].apply(preprocess_text).tolist())
    
    st.subheader("Sentiment Distribution")
    plot_sentiment_histograms(selected_df["polarity"], selected_df["subjectivity"])

    st.subheader("Sentiment Analysis Table")
    plot_sentiment_table(
        selected_df["title"],
        selected_df["polarity"].round(3),
        selected_df["polarity_class"],
        selected_df["subjectivity"].round(3),
        selected_df["subjectivity_class"]
    )