## Capstone Project - [Yummax](http://54.251.140.14)

### Introduction
This project relates to the food scene in Singapore and the Asia region. Rather than having to search through multiple food websites to find out what is happening, it provides a consolidated platform whereby aggregated web information can be obtained in a summarised form.

### Objectives and Approach
The project aims to fulfill 3 objectives:

* **Determine current food trends**
The approach used is Topic Modellng using gensim LDA. The topics identified signify the trends and summary of document most closely associated with the respective topics are presented.

* **Find out more about certain food topics or categories**
Key words from food topic or category supplied by user are used to search through the summaries list to identify the relevant ones.

* **Assess opinions of dining options and eateries**
Dining options and eateries key words supplied by user to select the relevant summaries. Sentiment analysis is then performed with Vader sentiment analyzer to determine the sentiment levels with their respective aggregated stats presented.

### Directories and Files
* [**Data Source - FoodBlogs**][data_source]
This directory contains the various notebooks in acquiring and cleaning data from the web. The [combine_notebook][combine_data] consolidates the collected information and performs EDA with the generation of wordcloud and Ngrams. It also provides a summary for each document.

* [**Amazon-Food-Review**][amazon]
The are several notebooks in this directory and the main purpose is to assess the performance of various Classifiers against the sentiment analyzers from TextBlob and Vader, using food review data from Amazon. 

* [**LDA&Sentiment_Analysis**][ldasa]
The [analysis_notebook][analysis] included utlises the cleaned data collected above and conduct Topic Modellng and Sentiment Analysis to meet the stated objectives. It generates 2 pickled files for use in the flask web application.

* [**Yummax**][yummax]
This directory contains [flask web app][flask] as well as the [HTML templates][html], [CSS/JS files][cssjs], icons and images used. The web app serves as UI for user query and model output presentation.

### Limitations 
The information gathered from the web is be exhaustive. As such, not all food categories and eateries in Singapore will be captured. The gensim summarizer does a quick and good job in summarizing the information. However, there is no control in prioritising what aspects to summarise. 

[data_source]: ../../../tree/master/Capstone-Project/Data-Source-FoodBlogs
[combine_data]: ../../../tree/master/Capstone-Project/Data-Source-FoodBlogs/FoodBlogs/Combine_allblogs-provide_summary-generate_wordcloud-ngrams.ipynb
[ldasa]: ../../../tree/master/Capstone-Project/LDA&Sentiment_Analysis
[analysis]: ../../../tree/master/Capstone-Project/LDA&Sentiment_Analysis/LDA-Sentiment_Analysis-Foodblogs.ipynb
[yummax]: ../../../tree/master/Capstone-Project/Yummax
[flask]: ../../../tree/master/Capstone-Project/Yummax/Scripts/Yummax.py
[html]: ../../../tree/master/Capstone-Project/Yummax/Scripts/templates
[cssjs]: ../../../tree/master/Capstone-Project/Yummax/Scripts/static
[amazon]: ../../../tree/master/Capstone-Project/Amazon-Food-Review
