import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import streamlit as st

def plot_word_cloud(article_texts):
    """
    Generate and display a word cloud from a list of article texts
    Parameters:
    - article_texts (list): List of article texts to generate the word cloud
    Returns:
    - None: Displays the word cloud using Streamlit
    """
    # Make sure that article_texts is not empty
    if not article_texts:
        print("No article texts available to generate word cloud.")
        return

    # Join all article texts into a single string
    text = ' '.join(article_texts)

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white',max_words=50).generate(text)
    print(wordcloud.words_)
    # Plot the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud)  
    plt.axis('off')  
    st.pyplot(plt)



def plot_sentiment_histograms(polarities, subjectivities):
    """
    Generate and display histograms for polarity and subjectivity distributions
    Parameters:
    - polarities (list): List of polarity scores for the articles
    - subjectivities (list): List of subjectivity scores for the articles
    Returns:
    - None: Displays the histograms using Streamlit
    """
    sns.set_style("whitegrid") 

    fig, axes = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'hspace': 0.4}) 

    # Polarity Histogram
    sns.histplot(polarities, bins=20, color='royalblue', alpha=0.7, edgecolor='black', ax=axes[0])
    axes[0].set_title("Polarity Distribution", fontsize=14, fontweight='bold', color='darkblue')
    axes[0].set_xlabel("Polarity", fontsize=12)
    axes[0].set_ylabel("Frequency", fontsize=12)
    axes[0].spines['top'].set_visible(True)  
    axes[0].spines['right'].set_visible(True)
    
    axes[0].set_xticks([-1, -0.5, 0, 0.5, 1])
    axes[0].set_xticklabels(["Negative", "-0.5", "0", "0.5", "Positive"], fontsize=11)

    # Subjectivity Histogram
    sns.histplot(subjectivities, bins=20, color='seagreen', alpha=0.7, edgecolor='black', ax=axes[1])
    axes[1].set_title("Subjectivity Distribution", fontsize=14, fontweight='bold', color='darkgreen')
    axes[1].set_xlabel("Subjectivity", fontsize=12)
    axes[1].set_ylabel("Frequency", fontsize=12)
    axes[1].spines['top'].set_visible(True)  
    axes[1].spines['right'].set_visible(True)

    axes[1].set_xticks([0, 0.25, 0.5, 0.75, 1])
    axes[1].set_xticklabels(["Objective", "0.25", "0.5", "0.75", "Subjective"], fontsize=11)

    plt.tight_layout()  
    st.pyplot(plt)




def plot_sentiment_table(article_titles, polarities, subjectivities, polarity_classes, subjectivity_classes):
    """
    Create and display a table with article titles, sentiment scores, and sentiment classifications
    Parameters:
    - article_titles (list): List of article titles
    - polarities (list): List of polarity scores
    - subjectivities (list): List of subjectivity scores
    - polarity_classes (list): List of classifications for polarity
    - subjectivity_classes (list): List of classifications for subjectivity
    Returns:
    - None: Displays the table using Streamlit
    """
    # Combine data into a list of rows for the table
    table_data = list(zip(article_titles, polarities, subjectivities, polarity_classes, subjectivity_classes))

    fig, ax = plt.subplots(figsize=(15, len(article_titles) * 0.4)) 
    ax.axis('tight')
    ax.axis('off')

    # Create the table
    table = ax.table(cellText=table_data,
                     colLabels=["Article Title", "Polarity Score", "Polarity", "Subjectivity Score", "Subjectivity",],
                     loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5)

    # Style the cells
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor("royalblue")
            cell.set_text_props(color="white", weight="bold", size=12)
        else:
            cell.set_facecolor("lavender")
            cell.set_text_props(color="black", size=10)
            if col == 0:
                cell.set_text_props(va='center', ha='center')

    # Set column widths
    column_widths = [0.35, 0.15, 0.15, 0.15, 0.2]  
    for i, width in enumerate(column_widths):
        table.auto_set_column_width([i])  
        table.get_celld()[(0, i)].set_width(width) 

    st.pyplot(plt)