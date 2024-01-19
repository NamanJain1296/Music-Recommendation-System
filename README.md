# Music-Recommendation-System
The Personalized Music Recommendation System is an intelligent and user-centric application designed to enhance the music listening experience by suggesting personalized song recommendations based on user preferences and behavior. The system employs advanced machine learning algorithms to analyze a user's historical music interactions, such as listening history, and favorite genres to generate tailored song recommendations.

# Benefits:
1. Personalized Recommendations: The system provides personalized song recommendations based on both text (genre) and numeric features.
2. Diverse and Popular Recommendations: By combining text and numeric features, the recommendations aim to be diverse and consider the popularity of songs.
3. User Engagement: Encourages user engagement by recommending songs similar to the input, enhancing the overall user experience.
4. Improved Song Discovery: Removes duplicate songs and focuses on delivering a variety of popular and distinct songs.

# Implementation Technologies
- Programming Language: Python
- Data Manipulation and Analysis: Pandas for handling and analyzing data.
- Visualization: Matplotlib and Seaborn for creating visualizations.
- Machine Learning Libraries: Scikit-learn for implementing machine learning algorithms.
- Text Vectorization: CountVectorizer from Scikit-learn for converting text data into a numerical format.
- Dimensionality Reduction: t-Distributed Stochastic Neighbor Embedding (TSNE) for visualizing high-dimensional data.

# Evaluation Metrics
- Cosine Similarity: Used to measure the similarity between two vectors (both text and numeric features).
- Popularity: Leveraged in sorting recommendations to prioritize popular songs.
- Recommendation List: Manual inspection and user feedback on the generated song recommendations.

# Conclusion
The implemented music recommendation system combines text and numeric features to generate personalized and diverse song recommendations. Leveraging the cosine similarity metric, the system calculates the similarity between songs based on both genre (text) and numeric features. The inclusion of TSNE for dimensionality reduction allows for visualizing the distribution of songs in a lower-dimensional space. By prioritizing popular songs and removing duplicates, the system aims to enhance user engagement and provide an improved platform for discovering new and exciting music. Continuous user feedback and manual inspection of the recommendation list contribute to the system's refinement and effectiveness over time.
