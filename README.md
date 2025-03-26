
# WebScrapingTrumpHarris

By Lisell Aare & Silvia Sanguinazzi

This repository contains a project designed to perform sentiment analysis on news articles about **Kamala Harris** and **Donald Trump**. The articles are web scraped using **The Guardian API**, and sentiment analysis is performed using **TextBlob**. The results are visualized in an interactive **Streamlit dashboard**.

## Table of Contents
1. [Task & Purpose](#task--purpose)
2. [Folder Structure](#folder-structure)
3. [Requirements](#requirements)
4. [How to Navigate](#how-to-navigate)

## Task & Purpose
- **Task:** Scrape news articles about Kamala Harris and Donald Trump from The Guardian API and perform sentiment analysis on them.
- **Purpose:** To analyze the **polarity** and **subjectivity** of articles, and visualize the results through engaging an dashboard.
- **Results:** The sentiment analysis is presented with:
  - **Polarity and subjectivity distributions**.
  - **Word clouds** highlighting keywords in the articles.
  - **Sentiment Comparison** between the two figures.

## Folder Structure

Here’s an overview of the project folder structure:

```
├── harris/
│   ├── scraping_harris.py          # Scrape articles about Kamala Harris
│   ├── nlp_harris.py               # Sentiment analysis 
│   └── main_harris.py              # Main file to run the extraction
├── trump/
│   ├── scraping_trump.py           # Scrape articles about Donald Trump
│   ├── nlp_trump.py                # Sentiment analysis 
│   └── main_trump.py               # Main file to run the extraction
├── analysis/  
│   ├── plots.py                    # Functions for generating visualizations
│   ├── compare.py                  # Comparison functions between Trump and Harris
│   ├── preprocessing.py            # Preprocessing functions for the analysis
│   └── tests/                      # Test folder containing unit tests
│       └── test_preprocessing.py   # Unit tests for preprocessing
├── main.py                         # Main file to run the streamlit app
├── requirements.txt                # List of required dependencies
└── README.md                       # Description of the project
```

## Requirements

To replicate this experiment, make sure you have Python 3 installed. You can install all the required dependencies by following these steps in the Terminal

### 1. Clone the repository
To be able to run the code locally you can clone the repository by using:
```
git clone https://github.com/sissisanguinazzi/WebScrapingNews-TrumpHarris.git
```
```
cd WebScrapingNews-TrumpHarris
```

### 2. Create and activate virtual environment
To avoid having conflicts with the packages versions create and activate a virtual environment:
```
python -m venv .venv
```

For macOs:
```
source .venv/bin/activate
```

For Windows:
```
.venv\Scripts\activate
```
### 3. Install dependencies
Then ensure that you intsall all the necessary dependencies by running:
```
pip install -r requirements.txt
```

### 4. Set up The Guardian API key
To scrape articles, you'll need an API key from **The Guardian**.

- Get your API key [here](https://open-platform.theguardian.com/access/).
- Set the API key as an environment variable in your terminal:
  
For macOS:
```
export API_KEY="your_guardian_api_key"
```
For Windows:
```
$env:API_KEY="your_guardian_api_key"
```
- Or you can set it directly in your code creating a ```.env``` file and adding ```API_KEY="your_guardian_api_key"```.

### 4. Run the Streamlit app
To run the code and see the results on the Streamlit dashboard use:
```
streamlit run main.py
```
If an error regarding the punkt package is returned, please try running the following in your terminal:
```
python -c "import nltk; nltk.download('punkt_tab')"
```

## How to Navigate
Once you have run the code you should be redirected to the page that contains the dashboards.  
From there you can navigate the different pages

1. Choose the Section (Trump, Harris, or Comparison):
In the sidebar of the Streamlit dashboard, you can select between:
- **Trump**: Displays sentiment analysis for articles about Donald Trump.
- **Harris**: Displays sentiment analysis for articles about Kamala Harris.
- **Comparison**: Compares the sentiment between articles about Trump and Harris.

2. Visualizations:
Trump and Harris section include:
- **Word Cloud**: Visualizes the most frequent words used in the articles.
- **Sentiment Distribution**: Shows histograms of polarity and subjectivity scores.
- **Sentiment Table**: Displays detailed sentiment scores for each article.

Comparisons section includes:
- **Polarity distribution boxplot**
- **Subjectivity distribution comparison**
- **Average sentiment scores bar plot**
- **Word clouds highlighting unique words for each figure**

3. Sentiment Classification:
Each article is classified based on:
- **Polarity**: Extremely positive, Significantly positive, Fairly positive, Slightly positive, Extremely negative, Significantly negative, Fairly negative, Slightly negative, Neutral.
- **Subjectivity**: Extremely subjective, Fairly subjective, Moderately subjective, Slightly subjective, Objective.
