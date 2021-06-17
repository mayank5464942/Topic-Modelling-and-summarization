# Topic-Modelling-and-summarization
Natural Language Processing has major role to deal with understanding of text.

Task Description :- To be able to generate two line summary for a large corpus of reviews from Google Play Store about a particular app. Here, I choose SBI YONO app

Procedure:

Firstly, I have obtained 9 topics using Latent Dirichilet Allocation Multicore method of Topic Modelling using Gensim, with workers=2.
Keeping, the alpha parameter symmetric, I have divided the reviews into 9 clusters according to topics, which means 9 clusters are created for 9 topics.
Next, for every cluster I have obtained extractive summarization with tuning parameters as ratio of words or number of words in the summary.
Lastly, I have combined all the 9 summaries obtained from 9 clusters and pulledout summary. This Final summary consists of 2-3 lines.
Reviews scraping from playstore: 1000 Most Relevant Reviews for YONO app are scrapped using pip package google-play-scraper. Python code for review extraction is in review_scrap.py in this repo. Book1.csv is the scrapped reviews.

Why 9 topics ? I have choosen optimized no. of topics based on a plot describing the coherence score on y-axis and no. of topics on x-axis , which is 9.

Summarization Technique in step 3 and step 4 I have used Gensim summarization to extract summary.

Alternatives- In step3, Extractive summarization can be performed using Gensim In step4 , Abstractive summarization using Bert

This task is done for categories of news apps, payments apps, social media apps, food apps and clothing apps. This is done as a part of "Dusra 2.0" project during my intern at Higgle startup.
