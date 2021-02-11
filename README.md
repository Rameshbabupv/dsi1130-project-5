# Project 5: Group Project
#### Authors: Adam Pardo, Brandon Bergeron, Eric Bayless, Ramesh Babu

DSI-113020 | 02.11.2021

## Problem Statement

The restaurant industry is extremely competitive with 80% of restaurants closing within their first 5 years of operation. This is important because restaurant closures can lead to job loss, which can hurt families both emotionally and financially. To avoid this, and to make sure that their restaurants succeed, owners take feedback from a variety of sources, and either resolve any negative critiques or focus on any areas of praise.  Looking solely at Yelp reviews, does the text in the review have any predictive power into whether or not a restaurant’s operating status is open or closed? 


## Project Directory
```
project-3
|__ code
|   |__ 01-Data_Collection.ipynb
|   |__ 02-EDA.ipynb
|   |__ 03-ML_Modeling.ipynb
|   |__ 04-NN_Model.ipynb
|__ data
|   |__ Las_Vegas_400.csv
|__ presentation
|   |--project_5_yelp_reviews.pdf
|   |__images
|      |__char_count_dist.png
|      |__custom_vocab_separate.png
|      |__importances.png
|      |__sentiment_per_business.png
|      |__star_rating_dist.png
|      |__top_10_words.png
|      |__top_20_bigrams.png
|      |__top_20_trigrams.png
|      |__word_count_dist.png
|__ README.md
```

## Executive Summary

This project consisted of 3 major phases: [Data Collection](https://github.com/Rameshbabupv/dsi1130-project-5#data-collection), [Data Cleaning and EDA](https://github.com/Rameshbabupv/dsi1130-project-5#data-cleaning-and-eda), and [Modeling](https://github.com/Rameshbabupv/dsi1130-project-5#modeling). 

The original dataset consisted of about 8 million reviews from businesses across North America. To build out an initial proof of concept, we decided to focus specifically on restaurants in the city that was most represented in the dataset: Las Vegas. We combined the reviews for each business into one body of text, and fit a wide variety of models to compare. 

## Data Collection

The Data Collection process involved downloading a large [Yelp reviews](https://www.kaggle.com/yelp-dataset/yelp-dataset) dataset from Kaggle that is updated by Yelp periodically. This dataset includes 5 separate json files of which we only used 2: The list of businesses and the individual reviews that we matched on business ids.

For instructions on how to download the data and where to store it in the repo, please refer to our first [notebook](https://github.com/Rameshbabupv/dsi1130-project-5/blob/main/code/01-Data_Collection.ipynb)

## Data Cleaning and EDA

Due to the volume of data, which could greatly increase processing time, a subset of the review data for Las Vegas was used to more quickly gain insights. First any missing reviews were dropped from the dataset. Then data was chosen by first selecting a random sample of 200 open and 200 closed restaurants in Las Vegas which had between 100 and 300 reviews total. This list of businesses was then joined to all the review data for those businesses. Using this process, a fairly equal number of reviews was obtained for both open and closed businesses (37,211 and 36,067 respectively).

In the analysis review ratings, character and word count; most frequent unigrams, bigrams, and trigrams; and review sentiment were all considered. The distributions of review ratings, as well as number of words and characters per review, were all similar between open and closed restaurants. When investigating term frequencies, it was found that the most frequent terms were mostly positive and there was a great amount of overlap between classes. Review sentiment was found to be mostly positive and similarly distributed between the classes which follows from the fact that it was strongly correlated to the review ratings, but not whether a restaurant was open or closed.

The conclusions from the analysis were that would be challenging to separate the classes based on the review text alone. If there is distinguishing text, it would not be at the top of the list in terms of frequency. However, this vocabulary could be discovered by using feature importances from modeling.

## Modeling

For modeling, we combined all reviews for individual businesses into one body of text as a singlar feature. Initially, 16 different models were fit to this data. We used 8 of some of the most popular sklearn algorithms, fit with both the CountVectorizer and TfidfVectorizer to compare performance. After this preliminary modeling, we searched accross the parameters of the 6 best models that out performed our initial baseline accuracy of 72%. Almost all of our models performances improved, but only by a couple percentage points. Our best ML model ended up being a GradientBoostingClassifier, with an accuracy score of 84.6% and a balanced accuracy score of 75.4%. 

We also explored a Neural Network model with parameter searching via Grid Search with KerasClassifier & TfidfVectorizer with 1000 features. The best parameters from this search were a layer with 128 units, 0.5 of Dropout, and L2 (ridge) regularization. With that model structure we got an accuracy score of 83.2% and a balanced accuracy score of 70.9%.

There were some computational limitations that prevented us from exploring more complex features or expanding our modeling to more restaurants, namely the word counts of the reviews when combining them. Migrating to a cloud computing platform would be a logical next step for further experimentation within the modeling domain.

## Data Limitations and Constraints

Our team had to work with a large dataset that was over 10GB. This made the data extraction process very time consuming by having to resolve a way to read-in all data and store it in an efficient way. Due to the size of the Yelp review file, the modeling was very time intensive and made EDA difficult. A majority of our time was spent on learning about the data, how to use it, and looking at the text found in the reviews. Due to the sheer volume of data, we only looked at restaurants that had between 100-300 reviews. Looking at restaurants with more reviews, and therefore more text, would take the models more than a day to process and run.

Another limitation is that our Yelp dataset only contained reviews up until December of 2019. Originally, we wanted to explore current reviews in the COVID-19 pandemic, but the limitations of the Yelp API made us change our original project scope. An important thing to note, the Yelp dataset is provided by Yelp itself, therefore it does not contain all restaurants and all reviews. We are unaware of what filtering or omissions Yelp does before making their dataset public.

## Future Work

We would like to explore more advanced Natural Language Processing (NLP) methods to have a better understanding of the text in the reviews. As mentioned above, we would like to explore features such as ‘customer service’ that may be driving restaurant closures. For our project, we only looked at restaurants that had between 100-300 reviews in Las Vegas. We would like to model on all restaurants in a given city if we had more computer power and time. Another area we would like to explore is model on business categories besides just limiting it to restaurants. While Las Vegas was used due to the high number of reviews, we would also like to expand our predictive models to other cities. Our code has the flexibility to deploy our modeling to other metropolitan areas. Finally, we would like to gather more recent reviews to observe the effect of COVID-19 on our models. When Yelp updates their publicly available dataset, we would like to return to the modeling process with restaurants reviews from 2020.


## Final Conclusions and Summary

While a lot can be learned from Yelp restaurant reviews, we found that they are not very effective predictors of whether or not a restaurant will close. There are numerous outside factors that affect a restaurants operating status. Therefore, we cannot accurately state that we can predict restaurant closures from Yelp reviews, but they are definitely worth looking into more. Initial modeling efforts led us to believe that customer service played an important role in driving closure predictions, something we think is worth looking into.